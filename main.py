# # from pubmed_fetcher.fetch_papers import fetch_pubmed_pmids

# # def main():
# #     """Main function to fetch and display PMIDs from PubMed"""
# #     query = "cancer research"  # Example search query
# #     print(f"\nSearching PubMed for: '{query}'...")
    
# #     pmid_list = fetch_pubmed_pmids(query)  # Fetch PMIDs
    
# #     if pmid_list:
# #         print(f"\nFound {len(pmid_list)} PMIDs:")
# #         for i, pmid in enumerate(pmid_list, 1):
# #             print(f"{i}. PMID: {pmid}")
# #             print(f"   Link: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
# #     else:
# #         print("\nNo PMIDs found or an error occurred.")

# # if __name__ == "__main__":
# #     main()

# # from pubmed_fetcher.fetch_papers import fetch_pubmed_pmids, fetch_paper_details

# # def main():
# #     """Main function to fetch and display research papers from PubMed."""
# #     query = "cancer research"  # Example search query
# #     pmid_list = fetch_pubmed_pmids(query, retmax=5)  # Fetch 5 PMIDs

# #     print("\nFound PMIDs:")
# #     for pmid in pmid_list:
# #         print(f"- PMID: {pmid} | Link: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

# #     # Fetch full paper details using PMIDs
# #     paper_details = fetch_paper_details(pmid_list)

# #     print("\nPaper Details:")
# #     for paper in paper_details:
# #         print(f"Title: {paper['Title']}")
# #         print(f"Publication Date: {paper['Publication Date']}")
# #         print(f"PMID: {paper['PMID']}")
# #         print("-" * 50)

# # # Run the script
# # if __name__ == "__main__":
# #     main()

# from pubmed_fetcher.fetch_papers import fetch_pubmed_pmids, fetch_paper_details
# from pubmed_fetcher.process_papers import extract_company_authors
# from pubmed_fetcher.fetch_papers import fetch_pubmed_pmids, fetch_paper_details
# from pubmed_fetcher.process_papers import extract_company_authors, save_to_csv


# def main():
#     """Main function to fetch, process, and filter research papers."""
#     query = "cancer research"  # Example search query
#     pmid_list = fetch_pubmed_pmids(query, retmax=2)  # Fetch 2 PMIDs for example

#     print("\nFound PMIDs:")
#     for pmid in pmid_list:
#         print(f"- PMID: {pmid} | Link: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

#     # Fetch full paper details
#     paper_details = fetch_paper_details(pmid_list)

#     print("\nFiltering Non-Academic Authors...")
#     filtered_papers = extract_company_authors(paper_details)

#     print(f"\nTotal Papers with Company Authors: {len(filtered_papers)}")
#     for paper in filtered_papers:
#         print("-" * 50)
#         print(f"Title: {paper['Title']}")
#         print(f"Publication Date: {paper['Publication Date']}")
#         print(f"Company Authors: {paper['Non-academic Authors']}")
#     if filtered_papers:
#         print("-" * 50)
        
# def main():
#     """Main function to fetch, process, and filter research papers."""
#     query = "cancer research"  # Example search query
#     pmid_list = fetch_pubmed_pmids(query, retmax=10)  # Fetch 10 PMIDs

#     print("\nFound PMIDs:")
#     for pmid in pmid_list:
#         print(f"- PMID: {pmid} | Link: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

#     # Fetch full paper details
#     paper_details = fetch_paper_details(pmid_list)

#     print("\nFiltering Non-Academic Authors...")
#     filtered_papers = extract_company_authors(paper_details)

#     print(f"\nTotal Papers with Company Authors: {len(filtered_papers)}")
#     for paper in filtered_papers:
#         print(f"Title: {paper['Title']}")
#         print(f"Publication Date: {paper['Publication Date']}")
#         print(f"Company Authors: {paper['Non-academic Authors']}")
#         print("-" * 50)

#     # Save results to CSV
#     save_to_csv(filtered_papers)
# # Run the script
# if __name__ == "__main__":
#     main()

# import argparse
# from pubmed_fetcher.fetch_papers import fetch_pubmed_pmids, fetch_paper_details
# from pubmed_fetcher.process_papers import extract_company_authors, save_to_csv

# def main():
#     """Main function to fetch, process, and filter research papers."""
    
#     # Setup argument parser
#     parser = argparse.ArgumentParser(description="Fetch and filter PubMed research papers with non-academic authors.")
#     parser.add_argument("-q", "--query", type=str, required=True, help="Search query for PubMed.")
#     parser.add_argument("-f", "--file", type=str, default="filtered_papers.csv", help="Filename to save results (default: filtered_papers.csv).")
#     parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode to print raw API responses.")
#     args = parser.parse_args()
    
#      # Fetch PMIDs based on user query
#     print(f"\n🔍 Searching PubMed for: {args.query}")
#     pmid_list = fetch_pubmed_pmids(args.query, retmax=10)  # Fetch 10 PMIDs

#     if not pmid_list:
#         print("❌ No PMIDs found. Exiting.")
#         return

#     print("\nFound PMIDs:")
#     for pmid in pmid_list:
#         print(f"- PMID: {pmid} | Link: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

#     # Fetch full paper details
#     paper_details = fetch_paper_details(pmid_list)

#     # Filter for non-academic authors
#     print("\nFiltering Non-Academic Authors...")
#     filtered_papers = extract_company_authors(paper_details)

#     print(f"\nTotal Papers with Company Authors: {len(filtered_papers)}")
#     for paper in filtered_papers:
#         print(f"Title: {paper['Title']}")
#         print(f"Publication Date: {paper['Publication Date']}")
#         print(f"Company Authors: {paper['Non-academic Authors']}")
#         print("-" * 50)

#     # Save results to CSV with user-specified filename
#     save_to_csv(filtered_papers, args.file)

# # Run the script
# if __name__ == "__main__":
#     main()

import argparse
from pubmed_fetcher.fetch_papers import fetch_pubmed_pmids, fetch_paper_details
from pubmed_fetcher.process_papers import extract_company_authors, save_to_csv

def main():
    """Main function to fetch, process, and filter research papers."""
    
    # Setup argument parser with improved help messages
    parser = argparse.ArgumentParser(
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
    args = parser.parse_args()

    # Fetch PMIDs based on user query
    print(f"\n🔍 Searching PubMed for: {args.query}")
    pmid_list = fetch_pubmed_pmids(args.query, retmax=10, debug=args.debug)  # Pass debug flag

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

    print(f"\nTotal Papers with Company Authors: {len(filtered_papers)}")
    for paper in filtered_papers:
        print(f"Title: {paper['Title']}")
        print(f"Publication Date: {paper['Publication Date']}")
        print(f"Company Authors: {paper['Non-academic Authors']}")
        print("-" * 50)

    # Save results to CSV with user-specified filename
    save_to_csv(filtered_papers, args.file)

# Run the script
if __name__ == "__main__":
    main()
