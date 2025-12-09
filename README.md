# NY Assembly Transcript API Documentation

Official documentation for the NY Assembly Transcript API - a comprehensive database of New York State Assembly floor transcripts, members, and legislative interactions.

## 
**Live Documentation**: https://ny-assembly-api-docs.readthedocs.io

**API Base URL**: http://nyassembly.duckdns.org:8888

**Demo API Key**: `drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU`

## 🚀 Quick Start

```python
import requests

API_KEY = "drt7AfZlJqLxrVtNXBNxSd03rJzqNXkPinTDWEfn0IU"
BASE_URL = "http://nyassembly.duckdns.org:8888"

# Get all members
response = requests.get(f"{BASE_URL}/members", params={"key": API_KEY})
data = response.json()

print(f"Total members: {data['total']}")
```

## 📖 Documentation Contents

- **Getting Started**: First steps with the API
- **Authentication**: How to use API keys
- **Rate Limits**: Understanding request limits
- **Endpoints**:
  - Members: Assembly member information
  - Transcripts: Full floor transcripts
  - Segments: Parsed individual statements
  - Interactions: Member-to-member interactions
- **Response Format**: Understanding API responses
- **Error Handling**: How to handle errors
- **Examples**: Complete code examples
- **Data Updates**: How the database is updated

## 🔧 Building Documentation Locally

### Prerequisites

- Python 3.8+
- Sphinx documentation generator

### Installation

```bash
# Clone this repository
git clone https://github.com/yourusername/ny-assembly-api-docs.git
cd ny-assembly-api-docs

# Install dependencies
pip install -r requirements.txt
```

### Build HTML Documentation

```bash
cd docs
make html
```

The built documentation will be in `docs/_build/html/`.

Open `docs/_build/html/index.html` in your browser to view.

### Clean Build

```bash
cd docs
make clean
make html
```

## 📝 Contributing

Contributions to improve documentation are welcome!

### How to Contribute

1. Fork this repository
2. Create a feature branch (`git checkout -b improve-docs`)
3. Make your changes to the `.rst` files in the `docs/` directory
4. Build locally to test (`make html`)
5. Commit your changes (`git commit -am 'Improve authentication docs'`)
6. Push to the branch (`git push origin improve-docs`)
7. Create a Pull Request

### Documentation Style Guide

- Use clear, concise language
- Include code examples for all concepts
- Test all code examples before submitting
- Follow existing formatting patterns
- Use proper RST syntax

## 🏗️ Documentation Structure

```
ny-assembly-api-docs/
├── docs/
│   ├── conf.py              # Sphinx configuration
│   ├── index.rst            # Main documentation page
│   ├── getting-started.rst  # Getting started guide
│   ├── authentication.rst   # Auth documentation
│   ├── rate-limits.rst      # Rate limit docs
│   ├── response-format.rst  # Response structure
│   ├── error-handling.rst   # Error handling
│   ├── examples.rst         # Code examples
│   ├── data-updates.rst     # ETL and updates
│   ├── endpoints/           # Endpoint documentation
│   │   ├── members.rst
│   │   ├── transcripts.rst
│   │   ├── segments.rst
│   │   └── interactions.rst
│   └── _static/
│       └── custom.css       # Custom styling
├── .readthedocs.yaml        # Read the Docs config
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔗 Related Links

- **API GitHub Repository**: https://github.com/yourusername/DiDa-Capstone
- **Report Issues**: https://github.com/yourusername/DiDa-Capstone/issues
- **NY Assembly Website**: https://nyassembly.gov

## 📧 Contact

For questions about the documentation:
- Open an issue in this repository
- Contact the API maintainer

For questions about the API itself:
- See the main [API repository](https://github.com/yourusername/DiDa-Capstone)

## 📄 License

This documentation is licensed under [MIT License](LICENSE).

The API and data are subject to their own licenses.

## 🙏 Acknowledgments

- New York State Assembly for providing public transcript data
- FastAPI for the excellent framework
- Read the Docs for documentation hosting
- Sphinx for documentation generation
