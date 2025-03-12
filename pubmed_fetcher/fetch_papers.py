try:
    import requests
except ImportError:
    print("Error: 'requests' package not found. Please install it using 'pip install requests'")
    import sys
    sys.exit(1)
import random
from typing import List, Dict, Any, Optional, Union

def fetch_pubmed_pmids(query: str, retmax: int = 10, debug: bool = False) -> List[str]:
    """Grab PMIDs from PubMed based on search query"""
    base_url: str = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params: Dict[str, Union[str, int]] = {
        "db": "pubmed",      
        "term": query,       
        "retmode": "json",   
        "retmax": retmax     
    }

    try:
        response: requests.Response = requests.get(base_url, params=params)
        response.raise_for_status()  

        data: Dict[str, Any] = response.json()

        if debug:
            print("\n🛠 DEBUG MODE: Raw PubMed Search Response\n", data)

        # Extract just the IDs from the response
        pmids: List[str] = data.get("esearchresult", {}).get("idlist", [])
        return pmids
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def fetch_paper_details(pmids: List[str], debug: bool = False) -> List[Dict[str, Any]]:
    """Get full paper details using PMIDs"""
    if not pmids:
        print("No PMIDs provided.")
        return []

    # Using efetch API to get XML data with full details
    base_url: str = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params: Dict[str, str] = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
        "rettype": "abstract"
    }

    try:
        response: requests.Response = requests.get(base_url, params=params)
        response.raise_for_status()

        if debug:
            print("\n🛠 DEBUG MODE: Raw Paper Details Response\n", response.text[:1000])

        from xml.etree import ElementTree as ET
        root: ET.Element = ET.fromstring(response.content)

        paper_details: List[Dict[str, Any]] = []
        for article in root.findall(".//PubmedArticle"):
            # Extract basic paper info
            pmid_element: Optional[ET.Element] = article.find(".//PMID")
            pmid: str = pmid_element.text if pmid_element is not None and pmid_element.text else "Unknown PMID"

            title_element: Optional[ET.Element] = article.find(".//ArticleTitle")
            title: str = title_element.text if title_element is not None and title_element.text else "No Title Available"

            # Parse publication date
            pub_date: Optional[ET.Element] = article.find(".//PubDate")
            year: Optional[ET.Element] = pub_date.find("Year") if pub_date is not None else None
            month: Optional[ET.Element] = pub_date.find("Month") if pub_date is not None else None
            day: Optional[ET.Element] = pub_date.find("Day") if pub_date is not None else None
            
            date_parts: List[str] = []
            if year is not None and year.text:
                date_parts.append(year.text)
            if month is not None and month.text:
                date_parts.append(month.text)
            if day is not None and day.text:
                date_parts.append(day.text)
            
            pub_date_str: str = " ".join(date_parts) if date_parts else "No Date Available"

            # Get author info with affiliations
            authors: List[str] = []
            author_list: List[ET.Element] = article.findall(".//Author")
            
            for author in author_list:
                # Build author name
                last_name: Optional[ET.Element] = author.find("LastName")
                fore_name: Optional[ET.Element] = author.find("ForeName")
                name_parts: List[str] = []
                if last_name is not None and last_name.text:
                    name_parts.append(last_name.text)
                if fore_name is not None and fore_name.text:
                    name_parts.append(fore_name.text)
                author_name: str = " ".join(name_parts) if name_parts else "Unknown Author"

                # Get all affiliations for this author
                affiliations: List[str] = []
                for aff in author.findall(".//Affiliation"):
                    if aff.text:
                        affiliations.append(aff.text.strip())
                
                # Format author with affiliations
                if affiliations:
                    authors.append(f"{author_name} ({'; '.join(affiliations)})")
                else:
                    authors.append(f"{author_name} (Unknown Affiliation)")

            # Add this paper to our results
            paper_details.append({
                "PMID": pmid,
                "Title": title,
                "Publication Date": pub_date_str,
                "Authors": authors
            })

        return paper_details

    except requests.exceptions.RequestException as e:
        print("Error fetching paper details:", e)
        return []
    except ET.ParseError as e:
        print("Error parsing XML response:", e)
        return []