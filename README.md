# 🕷️ OmniScrape - Professional Web Scraper

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.52+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**A powerful, user-friendly web scraping tool built with Python and Streamlit**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Screenshots](#screenshots) • [Contributing](#contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration Options](#configuration-options)
- [Data Export](#data-export)
- [Technical Details](#technical-details)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 🎯 Overview

**OmniScrape** is a comprehensive web scraping application that provides an intuitive interface for extracting structured data from websites. Built with Streamlit, it offers real-time scraping, data visualization, and easy export capabilities—all without writing a single line of code.

Perfect for:
- 📊 Data analysts gathering web data
- 🔬 Researchers collecting online information
- 💼 Business professionals conducting competitive analysis
- 🎓 Students learning web scraping techniques

---

## ✨ Features

### Core Capabilities

- **🔗 Link Extraction**: Automatically identifies and categorizes internal and external links
- **🖼️ Image Discovery**: Extracts all images with alt text and source URLs
- **📝 Text Content Parsing**: Captures text from customizable HTML tags (h1, h2, p, li, etc.)
- **📊 Table Extraction**: Detects and converts HTML tables to structured data
- **📧 Email Discovery**: Uses regex to find email addresses on pages
- **ℹ️ Metadata Collection**: Gathers page title, description, encoding, and server info

### User Experience

- **🎨 Beautiful UI**: Clean, modern interface with responsive design
- **⚡ Real-time Progress**: Live progress indicators and status updates
- **📱 Multi-Device Support**: Simulates Desktop, Mobile, and Tablet user agents
- **💾 Export Options**: Download data as CSV files for further analysis
- **🔍 Image Preview**: Visual gallery of discovered images
- **🛠️ Customizable**: Configure target tags and user agents

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone or Download the Project

```bash
cd "Python Web Scraper"
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies include:**
- `streamlit` - Web application framework
- `requests` - HTTP library for making web requests
- `beautifulsoup4` - HTML/XML parsing
- `pandas` - Data manipulation and analysis
- `lxml` - Fast XML/HTML parser

---

## 💻 Usage

### Running the Application

1. **Activate your virtual environment** (if not already active):
   ```bash
   # Windows
   .\venv\Scripts\Activate.ps1
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Start the Streamlit server**:
   ```bash
   streamlit run main.py
   ```

3. **Access the application**:
   - The app will automatically open in your default browser
   - Default URL: `http://localhost:8501`

### Quick Start Guide

1. **Enter URL**: Type or paste the website URL you want to scrape
2. **Configure Settings** (Sidebar):
   - Select user agent (Desktop/Mobile/Tablet)
   - Choose target HTML tags for text extraction
3. **Click "Start Scraping"**: Begin the extraction process
4. **View Results**: Browse through different tabs to see extracted data
5. **Download Data**: Export any dataset as CSV for analysis

---

## ⚙️ Configuration Options

### User Agent Selection

Choose how your scraper identifies itself:
- **Desktop**: Standard desktop browser (Chrome)
- **Mobile**: iPhone Safari
- **Tablet**: iPad Chrome

### Target Tags for Text Extraction

Customize which HTML elements to extract text from:
- `h1`, `h2`, `h3`, `h4` - Headers
- `p` - Paragraphs
- `li` - List items
- `span` - Inline text
- `div` - Division elements

---

## 📥 Data Export

All extracted data can be downloaded as CSV files:

| Data Type | File Name | Contents |
|-----------|-----------|----------|
| Links | `links.csv` | Link text, URL, type (internal/external) |
| Images | `images.csv` | Alt text, source URL |
| Text | `content.csv` | HTML tag, text content |
| Emails | `emails.csv` | Discovered email addresses |
| Tables | `table_1.csv` | Extracted table data |

---

## 🔧 Technical Details

### Architecture

```
OmniScrape/
│
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── venv/                  # Virtual environment (created locally)
```

### Key Components

**WebScraper Class**
- Handles HTTP requests with custom headers
- Parses HTML using BeautifulSoup
- Extracts and structures data
- Manages errors and timeouts

**Streamlit Interface**
- Responsive layout with sidebar controls
- Tabbed data visualization
- Progress tracking and status updates
- Download functionality

### Technologies Used

- **Python 3.13+**: Core programming language
- **Streamlit**: Web application framework
- **Beautiful Soup 4**: HTML parsing
- **Pandas**: Data manipulation
- **Requests**: HTTP client
- **lxml**: Fast HTML/XML processing

---

## 📌 Best Practices

### Ethical Scraping

✅ **DO:**
- Check and respect `robots.txt` files
- Add delays between requests for large-scale scraping
- Use appropriate user agents
- Comply with website Terms of Service
- Cache data to minimize repeated requests

❌ **DON'T:**
- Overload servers with rapid requests
- Scrape personal or sensitive data
- Ignore copyright and data protection laws
- Use scraped data for malicious purposes

### Performance Tips

- Start with smaller pages to test
- Use mobile user agent for faster responses
- Limit target tags to reduce processing time
- Clear browser cache if running into issues

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: "Failed to scrape URL" error
- **Solution**: Check if the URL is accessible in your browser, verify internet connection, try different user agent

**Problem**: No data extracted
- **Solution**: The website might use JavaScript to load content (requires Selenium/Playwright for dynamic content)

**Problem**: Streamlit won't start
- **Solution**: Ensure virtual environment is activated and all dependencies are installed

**Problem**: Execution policy error (Windows)
- **Solution**: Run PowerShell as Administrator and execute:
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### Getting Help

If you encounter issues:
1. Check the terminal output for error messages
2. Verify all dependencies are correctly installed
3. Ensure you're using Python 3.8+
4. Try running with a simple, well-known website first

---

## 📄 License

This project is licensed under the MIT License - feel free to use, modify, and distribute as needed.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- HTML parsing by [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- Data handling with [Pandas](https://pandas.pydata.org/)

---

## 📞 Contact & Support

For questions, suggestions, or contributions:
- Open an issue on the repository
- Submit a pull request with improvements

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ using Python & Streamlit

</div>
