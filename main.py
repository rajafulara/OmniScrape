import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urlparse, urljoin
import base64
import re

# --- Page Configuration (Must be first) ---
st.set_page_config(
    page_title="OmniScrape - Professional Web Scraper",
    page_icon="🕷️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Beauty and Engagement ---
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ce3b3b;
        color: white;
        border-color: #ce3b3b;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    h1 {
        color: #1E1E1E;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h2, h3 {
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# --- Helper Functions ---

def get_download_link(df, filename, text):
    """Generates a link to download the dataframe as a CSV file."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href

def convert_df(df):
    """Converts dataframe to CSV for st.download_button"""
    return df.to_csv(index=False).encode('utf-8')

def validate_url(url):
    """Ensures URL has http/https schema."""
    if not url.startswith(('http://', 'https://')):
        return 'https://' + url
    return url

def extract_emails(text):
    """Extracts emails using regex."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return list(set(re.findall(email_pattern, text)))

# --- The Scraper Class ---

class WebScraper:
    def __init__(self, url, user_agent_type="Desktop"):
        self.url = url
        self.soup = None
        self.response = None
        self.data = {}
        
        # User Agents to mimic real browsers
        user_agents = {
            "Desktop": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mobile": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1",
            "Tablet": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"
        }
        self.headers = {'User-Agent': user_agents.get(user_agent_type, user_agents["Desktop"])}

    def fetch(self):
        try:
            with st.spinner(f"Connecting to {self.url}..."):
                self.response = requests.get(self.url, headers=self.headers, timeout=10)
                self.response.raise_for_status()
                self.soup = BeautifulSoup(self.response.content, 'html.parser')
            return True, self.response.status_code
        except requests.exceptions.RequestException as e:
            return False, str(e)

    def scrape_metadata(self):
        if not self.soup: return None
        return {
            "Title": self.soup.title.string if self.soup.title else "No Title",
            "Description": self.soup.find("meta", attrs={"name": "description"})["content"] if self.soup.find("meta", attrs={"name": "description"}) else "No Description",
            "Charset": self.response.encoding,
            "Server": self.response.headers.get('Server', 'Unknown')
        }

    def scrape_links(self):
        if not self.soup: return []
        links = []
        for a in self.soup.find_all('a', href=True):
            href = a['href']
            full_url = urljoin(self.url, href)
            links.append({
                "Text": a.text.strip()[:50] + "..." if len(a.text.strip()) > 50 else a.text.strip(),
                "URL": full_url,
                "Type": "Internal" if urlparse(full_url).netloc == urlparse(self.url).netloc else "External"
            })
        return pd.DataFrame(links).drop_duplicates()

    def scrape_images(self):
        if not self.soup: return []
        images = []
        for img in self.soup.find_all('img', src=True):
            src = img['src']
            full_url = urljoin(self.url, src)
            alt = img.get('alt', 'No Alt Text')
            images.append({"Alt Text": alt, "Source URL": full_url})
        return pd.DataFrame(images).drop_duplicates()

    def scrape_tables(self):
        if not self.soup: return []
        tables = []
        # Use pandas to extract tables directly
        try:
            dfs = pd.read_html(str(self.soup))
            for i, df in enumerate(dfs):
                df['Table ID'] = f"Table {i+1}"
                tables.append(df)
        except:
            pass # No tables found or parsing error
        return tables

    def scrape_text_content(self, tags=['p', 'h1', 'h2', 'h3', 'li']):
        if not self.soup: return ""
        text_data = []
        for tag in tags:
            elements = self.soup.find_all(tag)
            for el in elements:
                text_data.append({"Tag": tag, "Content": el.get_text(strip=True)})
        return pd.DataFrame(text_data)

# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Configuration")
    user_agent = st.selectbox("User Agent", ["Desktop", "Mobile", "Tablet"])
    target_tags = st.multiselect("Target Tags for Text", ['p', 'h1', 'h2', 'h3', 'h4', 'span', 'li', 'div'], default=['h1', 'h2', 'p'])
    st.divider()
    st.markdown("### 💡 About")
    st.info("This is a universal web scraper built with Python & Streamlit. It handles headers, parses DOM elements, and exports structured data.")
    st.markdown("Made by **Gemini**")

# --- Main Interface ---

col1, col2 = st.columns([3, 1])
with col1:
    st.title("🕷️ OmniScrape")
    st.markdown("### The Automatic, One-Click Web Extractor")

with col2:
    # Just a visual placeholder for status
    st.empty()

url_input = st.text_input("Enter Website URL", placeholder="https://example.com", help="Enter the full URL of the website you want to scrape.")

if st.button("🚀 Start Scraping"):
    if not url_input:
        st.error("Please enter a valid URL.")
    else:
        valid_url = validate_url(url_input)
        scraper = WebScraper(valid_url, user_agent)
        
        # Scrape Progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("Connecting to server...")
        success, status_msg = scraper.fetch()
        progress_bar.progress(30)
        
        if success:
            status_text.text("Parsing DOM content...")
            time.sleep(0.5) # User experience delay
            progress_bar.progress(60)
            
            # Perform Extractions
            metadata = scraper.scrape_metadata()
            df_links = scraper.scrape_links()
            df_images = scraper.scrape_images()
            df_text = scraper.scrape_text_content(target_tags)
            raw_emails = extract_emails(scraper.soup.get_text())
            df_emails = pd.DataFrame(raw_emails, columns=["Found Emails"])
            
            tables = scraper.scrape_tables()
            
            progress_bar.progress(100)
            status_text.text("Scraping Complete!")
            time.sleep(0.5)
            status_text.empty()
            progress_bar.empty()

            # --- Results Display ---
            
            # Metrics Row
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Links Found", len(df_links))
            m2.metric("Images Found", len(df_images))
            m3.metric("Tables Found", len(tables))
            m4.metric("Status Code", status_msg)

            st.divider()

            # Tabs for different data types
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔗 Links", "🖼️ Images", "📝 Text Content", "📊 Tables", "ℹ️ Metadata"])

            with tab1:
                st.subheader("Extracted Links")
                if not df_links.empty:
                    st.dataframe(df_links, use_container_width=True)
                    csv_links = convert_df(df_links)
                    st.download_button("Download Links CSV", csv_links, "links.csv", "text/csv")
                else:
                    st.warning("No links found.")

            with tab2:
                st.subheader("Extracted Images")
                if not df_images.empty:
                    st.dataframe(df_images, use_container_width=True)
                    
                    # Gallery Preview (First 4 images)
                    st.write("Image Preview (First 4):")
                    img_cols = st.columns(4)
                    for i, col in enumerate(img_cols):
                        if i < len(df_images):
                            try:
                                col.image(df_images.iloc[i]['Source URL'], caption=f"Img {i+1}", use_column_width=True)
                            except:
                                col.warning("Load Failed")
                    
                    csv_images = convert_df(df_images)
                    st.download_button("Download Image Data CSV", csv_images, "images.csv", "text/csv")
                else:
                    st.warning("No images found.")

            with tab3:
                st.subheader("Text Content")
                if not df_text.empty:
                    st.dataframe(df_text, use_container_width=True)
                    csv_text = convert_df(df_text)
                    st.download_button("Download Text CSV", csv_text, "content.csv", "text/csv")
                
                if not df_emails.empty:
                    st.divider()
                    st.subheader("📧 Discovered Emails")
                    st.dataframe(df_emails)
                    csv_emails = convert_df(df_emails)
                    st.download_button("Download Emails CSV", csv_emails, "emails.csv", "text/csv")

            with tab4:
                st.subheader("Tabular Data")
                if tables:
                    for i, table in enumerate(tables):
                        st.markdown(f"**Table {i+1}**")
                        st.dataframe(table)
                        csv_table = convert_df(table)
                        st.download_button(f"Download Table {i+1} CSV", csv_table, f"table_{i+1}.csv", "text/csv", key=f"dl_table_{i}")
                        st.divider()
                else:
                    st.info("No HTML tables found on this page.")

            with tab5:
                st.subheader("Page Metadata")
                st.json(metadata)
                st.subheader("Raw HTML Preview (Top 1000 chars)")
                st.code(str(scraper.soup.prettify())[:1000], language='html')

        else:
            st.error(f"Failed to scrape URL. Error: {status_msg}")

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>OmniScrape Tool v1.0 | Use responsibly. Respect robots.txt</div>", unsafe_allow_html=True)