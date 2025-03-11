import requests
import random

def fetch_pubmed_pmids(query, retmax=10, debug=False):
    """
    Fetches PMIDs (PubMed IDs) based on a search query.

    :param query: The search term (e.g., "cancer research").
    :param retmax: The maximum number of PMIDs to retrieve.
    :param debug: If True, prints raw API response.
    :return: A list of PMIDs or an empty list if an error occurs.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",      
        "term": query,       
        "retmode": "json",   
        "retmax": retmax     
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  

        data = response.json()

        if debug:
            print("\n🛠 DEBUG MODE: Raw PubMed Search Response\n", data)

        pmids = data.get("esearchresult", {}).get("idlist", [])
        return pmids
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def fetch_paper_details(pmids, debug=False):
    """
    Fetches detailed information about research papers from PubMed using their PMIDs.

    :param pmids: List of PubMed IDs (PMIDs)
    :param debug: If True, prints raw API response.
    :return: List of dictionaries containing paper details
    """
    if not pmids:
        print("No PMIDs provided.")
        return []

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"  # Using efetch instead of esummary
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",    # XML format provides more detailed information
        "rettype": "abstract"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        if debug:
            print("\n🛠 DEBUG MODE: Raw Paper Details Response\n", response.text[:1000])  # Show first 1000 chars

        # Parse XML response
        from xml.etree import ElementTree as ET
        root = ET.fromstring(response.content)

        paper_details = []
        for article in root.findall(".//PubmedArticle"):
            # Extract PMID
            pmid = article.find(".//PMID").text

            # Extract title
            title = article.find(".//ArticleTitle").text or "No Title Available"

            # Extract publication date
            pub_date = article.find(".//PubDate")
            year = pub_date.find("Year")
            month = pub_date.find("Month")
            day = pub_date.find("Day")
            
            date_parts = []
            if year is not None and year.text:
                date_parts.append(year.text)
            if month is not None and month.text:
                date_parts.append(month.text)
            if day is not None and day.text:
                date_parts.append(day.text)
            
            pub_date_str = " ".join(date_parts) if date_parts else "No Date Available"

            # Extract authors with affiliations
            authors = []
            author_list = article.findall(".//Author")
            
            for author in author_list:
                # Get author name
                last_name = author.find("LastName")
                fore_name = author.find("ForeName")
                name_parts = []
                if last_name is not None and last_name.text:
                    name_parts.append(last_name.text)
                if fore_name is not None and fore_name.text:
                    name_parts.append(fore_name.text)
                author_name = " ".join(name_parts) if name_parts else "Unknown Author"

                # Get affiliations
                affiliations = []
                for aff in author.findall(".//Affiliation"):
                    if aff.text:
                        affiliations.append(aff.text.strip())
                
                # Format author string
                if affiliations:
                    authors.append(f"{author_name} ({'; '.join(affiliations)})")
                else:
                    authors.append(f"{author_name} (Unknown Affiliation)")

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