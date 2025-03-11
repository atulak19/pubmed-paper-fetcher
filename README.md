# 📄 PubMed Paper Fetcher  

This is a simple command-line tool that helps you **search for research papers on PubMed**, filter papers that have **company-affiliated authors**, and save the results as a CSV file for easy reference.  

## 🚀 Why Use This?  
- 🔍 **Easily search PubMed** for research papers.  
- 🏢 **Filter papers with non-academic authors** (e.g., from pharmaceutical or biotech companies).  
- 💾 **Export results to a CSV file** for easy use in reports or analysis.  
- ⚡ **Simple command-line tool** that works right away!  

---

## 📌 Installation  

### 1️⃣ Install via TestPyPI  
To install this tool from TestPyPI, run:  
```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-paper-fetcher

 Verify Installation
 get-papers-list -h

 How to Use
🔍 Search for Research Papers & Save to CSV
get-papers-list -q "cancer research" -f "cancer_results.csv"
This will fetch relevant papers from PubMed, filter the ones with company-affiliated authors, and save the results in cancer_results.csv.

🛠 Enable Debug Mode (For Troubleshooting)
get-papers-list -q "biotechnology" -f "biotech_results.csv" -d
With -d, the tool will print raw API responses for debugging.

What’s Inside?
pubmed-paper-fetcher/
│── pubmed_fetcher/
│   │── fetch_papers.py      # Handles API requests to PubMed
│   │── process_papers.py    # Filters & processes author affiliations
│   └── cli.py               # Handles command-line arguments
│── tests/                   # Contains test cases
│── README.md                # This documentation
│── main.py                  # Main entry point
│── pyproject.toml           # Poetry configuration
└── .gitignore               # Files to ignore in Git

Want to Contribute?
If you’d like to improve this project, feel free to fork the repository and create a pull request!

Fork the repo on GitHub
Clone your fork
git clone https://github.com/your-username/pubmed-paper-fetcher.git
Make changes and test locally
Create a pull request

 License
This project is open-source under the AK License.

---



