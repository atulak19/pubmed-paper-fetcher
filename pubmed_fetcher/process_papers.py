import re
import csv
from typing import List, Dict, Any, Optional

def extract_company_authors(papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filter papers to only include those with company/industry affiliations"""
    # Keywords that suggest company/industry affiliation
    company_keywords: List[str] = ['Inc', 'Ltd', 'LLC', 'Corp', 'Limited', 'Company', 
                       'Pharma', 'Pharmaceuticals', 'Biotech', 'Industries',
                       'GmbH', 'AG', 'SA', 'NV', 'Pfizer', 'Merck', 'Novartis',
                       'AstraZeneca', 'Roche', 'Sanofi']
    
    filtered_papers: List[Dict[str, Any]] = []
    
    for paper in papers:
        company_authors: List[str] = []
        
        # Look through each author's affiliation for company keywords
        for author in paper.get('Authors', []):
            if any(keyword.lower() in author.lower() for keyword in company_keywords):
                company_authors.append(author)
        
        # Only keep papers that have at least one company author
        if company_authors:
            filtered_paper: Dict[str, Any] = {
                'Title': paper['Title'],
                'Publication Date': paper['Publication Date'],
                'PMID': paper['PMID'],
                'Non-academic Authors': company_authors
            }
            filtered_papers.append(filtered_paper)
    
    return filtered_papers


def save_to_csv(filtered_papers: List[Dict[str, Any]], filename: str = "filtered_papers.csv") -> None:
    """Save filtered papers to a CSV file"""
    if not filtered_papers:
        print("No papers to save.")
        return

    # Define CSV columns
    headers: List[str] = ["PMID", "Title", "Publication Date", "Company Authors"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            # Write each paper as a row
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

