import argparse
from typing import List, Dict, Any, Optional
from pubmed_fetcher.fetch_papers import fetch_pubmed_pmids, fetch_paper_details
from pubmed_fetcher.process_papers import extract_company_authors, save_to_csv

def main() -> None:
    """Main script for running the PubMed paper fetcher directly"""
    # Parse command line arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Fetch research papers from PubMed, filter those with non-academic (company) authors, and save results to a CSV file."
    )
    parser.add_argument(
        "-q", "--query", type=str, required=True,
        help="Search query for PubMed (e.g., 'cancer research'). Required."
    )
    parser.add_argument(
        "-f", "--file", type=str, default="filtered_papers.csv",
        help="Filename to save results (default: filtered_papers.csv)."
    )
    parser.add_argument(
        "-d", "--debug", action="store_true",
        help="Enable debug mode to print raw API responses for troubleshooting."
    )
    args: argparse.Namespace = parser.parse_args()

    # Fetch papers from PubMed - using higher retmax for more results
    print(f"\n🔍 Searching PubMed for: {args.query}")
    pmid_list: List[str] = fetch_pubmed_pmids(args.query, retmax=10, debug=args.debug)

    if not pmid_list:
        print("❌ No PMIDs found. Exiting.")
        return

    # Display found PMIDs
    print("\nFound PMIDs:")
    for pmid in pmid_list:
        print(f"- PMID: {pmid} | Link: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

    # Get full details for each paper
    paper_details: List[Dict[str, Any]] = fetch_paper_details(pmid_list, debug=args.debug)

    # Filter to only include papers with company authors
    print("\nFiltering Non-Academic Authors...")
    filtered_papers: List[Dict[str, Any]] = extract_company_authors(paper_details)

    # Show results
    print(f"\nTotal Papers with Company Authors: {len(filtered_papers)}")
    for paper in filtered_papers:
        print(f"Title: {paper['Title']}")
        print(f"Publication Date: {paper['Publication Date']}")
        print(f"Company Authors: {paper['Non-academic Authors']}")
        print("-" * 50)

    # Save to CSV file
    save_to_csv(filtered_papers, args.file)
    print(f"\n✅ Results saved to {args.file}")

if __name__ == "__main__":
    main()
