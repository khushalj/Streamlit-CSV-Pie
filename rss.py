import streamlit as st
import requests
import xml.etree.ElementTree as ET
import importlib

def check_requirements(requirements_file):
    with open(requirements_file, 'r') as file:
        requirements = file.read().splitlines()
    
    not_installed = []
    for requirement in requirements:
        try:
            importlib.import_module(requirement)
        except ImportError:
            not_installed.append(requirement)
    
    return not_installed

def parse_rss_feed(feed_url):
    response = requests.get(feed_url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        feed_entries = []
        
        for item in root.iter("item"):
            entry = {
                "title": item.find("title").text,
                "summary": item.find("description").text,
                "published": item.find("pubDate").text,
                "link": item.find("link").text
            }
            feed_entries.append(entry)
        
        return feed_entries
    else:
        return None

def main():
    st.title("RSS Feed Reader")
    
    # Check required packages
    missing_packages = check_requirements('requirements.txt')
    if missing_packages:
        st.error(f"The following required packages are missing: {', '.join(missing_packages)}")
        return
    
    # Input field for the RSS feed URL
    feed_url = st.text_input("Enter RSS Feed URL", "http://feeds.feedburner.com/TheHackersNews")
    
    if st.button("Fetch"):
        if feed_url:
            feed_entries = parse_rss_feed(feed_url)
            if feed_entries:
                st.header(feed_entries[0]["title"])
                for entry in feed_entries:
                    st.subheader(entry["title"])
                    st.write(entry["summary"])
                    st.write(f"Published on: {entry['published']}")
                    st.write(f"Link: {entry['link']}")
            else:
                st.warning("Error fetching or parsing the RSS feed.")
        else:
            st.warning("Please enter a valid RSS Feed URL and click 'Fetch'.")

if __name__ == "__main__":
    main()
