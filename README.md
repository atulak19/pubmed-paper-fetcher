# 📄 PubMed Paper Fetcher

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A command-line tool that helps researchers **search for papers on PubMed**, filter those with **company-affiliated authors**, and export results to CSV format.

## 🚀 Features

- 🔍 **PubMed Integration**: Search the PubMed database using custom queries
- 🏢 **Company Author Filter**: Automatically identify papers with non-academic authors
- 💾 **CSV Export**: Save filtered results in a structured format for analysis
- ⚡ **Simple CLI**: Easy-to-use command-line interface with helpful options

## 📋 Table of Contents

- [Installation](#-installation)
- [Usage](#-usage)
- [Code Organization](#-code-organization)
- [Project Structure](#-project-structure)
- [Dependencies](#-dependencies)
- [Tools Used](#-tools-used)
- [Contributing](#-contributing)
- [License](#-license)

## 📥 Installation

### Install from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ ak19-pubmed-paper-fetcher
```

### Install from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/atulak19/pubmed-paper-fetcher.git
   cd pubmed-paper-fetcher
   ```

2. Install using Poetry (recommended):
   ```bash
   # Install Poetry if you don't have it
   pip install poetry
   
   # Install dependencies and the package
   poetry install
   ```

3. Or install using pip:
   ```bash
   pip install -e .
   ```

### Verify Installation

```bash
get-papers-list -h
```

## 🖥️ Usage

### Basic Search

Search for papers and save results to CSV:

```bash
get-papers-list -q "cancer research" -f "cancer_results.csv"
```

### Debug Mode

Enable debug mode to see API responses:

```bash
get-papers-list -q "biotechnology" -f "biotech_results.csv" -d
```

### Command Options

| Option | Description |
|--------|-------------|
| `-q`, `--query` | Search query for PubMed (required) |
| `-f`, `--file` | Filename to save results (default: filtered_papers.csv) |
| `-d`, `--debug` | Enable debug mode for troubleshooting |

## 🧩 Code Organization

The codebase follows a modular structure with clear separation of concerns:

1. **Data Fetching Layer** (`fetch_papers.py`):
   - Handles all interactions with the PubMed API
   - Manages HTTP requests and response parsing
   - Extracts paper metadata and author information

2. **Data Processing Layer** (`process_papers.py`):
   - Filters papers based on author affiliations
   - Identifies company/industry authors using keyword matching
   - Prepares data for export

3. **Command Line Interface** (`cli.py`):
   - Parses command-line arguments
   - Orchestrates the workflow between fetching and processing
   - Handles user feedback and output formatting

4. **Entry Points**:
   - Package-level CLI via Poetry scripts
   - Direct execution through `main.py`

## 📁 Project Structure

```
pubmed-paper-fetcher/
│
├── pubmed_fetcher/
│   ├── __init__.py         # Package exports
│   ├── fetch_papers.py     # PubMed API integration
│   ├── process_papers.py   # Author filtering logic
│   └── cli.py              # Command-line interface
│
├── tests/                  # Test cases
├── main.py                 # Direct script entry point
├── README.md               # Documentation
├── pyproject.toml          # Poetry configuration
└── .gitignore              # Git ignore rules
```

## 📦 Dependencies

This project relies on the following Python packages:

- **requests** (^2.28.0): For making HTTP requests to the PubMed API
- **typing** (^3.7.4): For type annotations
- **argparse**: For command-line argument parsing (standard library)
- **csv**: For CSV file operations (standard library)
- **xml.etree.ElementTree**: For parsing XML responses (standard library)

To install all dependencies:

```bash
# Using Poetry
poetry install

# Using pip
pip install requests typing
```

## 🛠️ Tools Used

This project was developed with the assistance of:

- **[ChatGPT](https://chat.openai.com)**: Used for code assistance, documentation generation, and troubleshooting
- **[Poetry](https://python-poetry.org/)**: For dependency management and packaging
- **[PubMed E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25500/)**: For accessing research paper data
- **[GitHub](https://github.com)**: For version control and project hosting
- **[TestPyPI](https://test.pypi.org)**: For package distribution testing

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/pubmed-paper-fetcher.git
   ```
3. **Install development dependencies**:
   ```bash
   cd pubmed-paper-fetcher
   poetry install
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
5. **Make your changes** and test them
6. **Commit your changes**:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
7. **Push to your branch**:
   ```bash
   git push origin feature/amazing-feature
   ```
8. **Create a Pull Request** on GitHub

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by [Atul](https://github.com/atulak19) | [Report Issues](https://github.com/atulak19/pubmed-paper-fetcher/issues)



