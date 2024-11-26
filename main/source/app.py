import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Set up the tabs
tab1, tab2 = st.tabs(["Web Scraping", "File Upload"])

# Web Scraping Tab
with tab1:
    st.header("Web Scraping")
    url = st.text_input("Enter the URL to scrape:")
    if st.button("Scrape"):
        if url:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Example: Scrape all links
                links = [a['href'] for a in soup.find_all('a', href=True)]

                st.write("Found Links:")
                st.write(links)

                # Optional: Allow download of scraped links
                df = pd.DataFrame({"Links": links})
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Links as CSV",
                    data=csv,
                    file_name="scraped_links.csv",
                    mime="text/csv"
                )
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a valid URL.")

# File Upload Tab
with tab2:
    st.header("File Upload")
    uploaded_file = st.file_uploader("Upload your file here", type=["csv", "txt", "xlsx", "json"])
    if uploaded_file is not None:
        st.success(f"File uploaded: {uploaded_file.name}")
        try:
            # Display content based on file type
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
                st.write("File Contents:")
                st.dataframe(df)
            elif uploaded_file.name.endswith(".txt"):
                content = uploaded_file.read().decode("utf-8")
                st.write("File Contents:")
                st.text(content)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
                st.write("File Contents:")
                st.dataframe(df)
            elif uploaded_file.name.endswith(".json"):
                df = pd.read_json(uploaded_file)
                st.write("File Contents:")
                st.dataframe(df)
            else:
                st.error("Unsupported file format.")
        except Exception as e:
            st.error(f"Error reading file: {e}")
