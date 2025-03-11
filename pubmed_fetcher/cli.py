import argparse
from .fetch_papers import fetch_pubmed_pmids, fetch_paper_details
from .process_papers import extract_company_authors, save_to_csv

def main():
    """Command-line interface for PubMed paper fetcher."""
    
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description="Fetch research papers from PubMed, filter those with non-academic (company) authors, and save results to a CSV file."
    )
    parser.add_argument(
        "-q", "--query", 
        type=str, 
        required=True, 
        help="Search query for PubMed (e.g., \"cancer research\"). Required."
    )
    parser.add_argument(
        "-f", "--file", 
        type=str, 
        default="filtered_papers.csv", 
        help="Filename to save results (default: filtered_papers.csv)."
    )
    parser.add_argument(
        "-d", "--debug", 
        action="store_true", 
        help="Enable debug mode to print raw API responses for troubleshooting."
    )
    args = parser.parse_args()
    
    # Fetch PMIDs based on user query
    print(f"\n🔍 Searching PubMed for: {args.query}")
    pmid_list = fetch_pubmed_pmids(args.query, retmax=2, debug=args.debug)  # Pass debug flag

    if not pmid_list:
        print("❌ No PMIDs found. Exiting.")
        return

    print("\nFound PMIDs:")
    for pmid in pmid_list:
        print(f"- PMID: {pmid} | Link: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

    # Fetch full paper details
    paper_details = fetch_paper_details(pmid_list, debug=args.debug)  # Pass debug flag

    # Filter for non-academic authors
    print("\nFiltering Non-Academic Authors...")
    filtered_papers = extract_company_authors(paper_details)

    # Save results to CSV with user-specified filename
    if filtered_papers:
        print(f"\nTotal Papers with Company Authors: {len(filtered_papers)}")
        for paper in filtered_papers:
            print("-" * 50)
            print(f"Title: {paper['Title']}")
            print(f"Publication Date: {paper['Publication Date']}")
            print(f"Company Authors: {paper['Non-academic Authors']}")
        print("-" * 50)
    else:
        print("\nNo papers found with company authors.")

    save_to_csv(filtered_papers, args.file)
    print(f"\n✅ Results saved to {args.file}")

if __name__ == "__main__":
    main()