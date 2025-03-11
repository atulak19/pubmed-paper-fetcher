import re
import csv

def extract_company_authors(papers):
    """
    Filter papers to include only those with company/industry affiliations.
    
    :param papers: List of paper details from fetch_paper_details
    :return: List of papers with company authors
    """
    company_keywords = ['Inc', 'Ltd', 'LLC', 'Corp', 'Limited', 'Company', 
                       'Pharma', 'Pharmaceuticals', 'Biotech', 'Industries',
                       'GmbH', 'AG', 'SA', 'NV', 'Pfizer', 'Merck', 'Novartis',
                       'AstraZeneca', 'Roche', 'Sanofi']
    
    filtered_papers = []
    
    for paper in papers:
        company_authors = []
        
        # Check each author's affiliation for company keywords
        for author in paper.get('Authors', []):
            if any(keyword.lower() in author.lower() for keyword in company_keywords):
                # Extract just the author name and affiliation
                company_authors.append(author)
        
        # If we found any company authors, add this paper to our results
        if company_authors:
            filtered_paper = {
                'Title': paper['Title'],
                'Publication Date': paper['Publication Date'],
                'PMID': paper['PMID'],
                'Non-academic Authors': company_authors
            }
            filtered_papers.append(filtered_paper)
    
    return filtered_papers



def save_to_csv(filtered_papers, filename="filtered_papers.csv"):
    """
    Saves the filtered research papers to a CSV file.

    :param filtered_papers: List of dictionaries containing paper details.
    :param filename: Name of the output CSV file (default: "filtered_papers.csv").
    """
    if not filtered_papers:
        print("No papers to save.")
        return

    headers = ["PMID", "Title", "Publication Date", "Company Authors"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()  # Write column headers

            for paper in filtered_papers:
                writer.writerow({
                    "PMID": paper["PMID"],
                    "Title": paper["Title"],
                    "Publication Date": paper["Publication Date"],
                    "Company Authors": "; ".join(paper["Non-academic Authors"])
                })

        print(f"\n✅ Results saved to {filename}")

    except Exception as e:
        print(f"❌ Error saving CSV file: {e}")

