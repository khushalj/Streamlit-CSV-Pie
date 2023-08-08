import streamlit as st
import feedparser

def main():
    st.title("RSS Feed Reader")
    
    # Input field for the RSS feed URL
    feed_url = st.text_input("Enter RSS Feed URL", "http://feeds.feedburner.com/TheHackersNews")
    
    if st.button("Fetch"):
        if feed_url:
            # Fetch the RSS feed using feedparser
            feed = feedparser.parse(feed_url)
            
            if 'title' in feed.feed:
                st.header(feed.feed.title)
            
            # Display the feed entries
            for entry in feed.entries:
                st.subheader(entry.title)
                st.write(entry.summary)
                st.write(f"Published on: {entry.published}")
                st.write(f"Link: {entry.link}")
        else:
            st.warning("Please enter a valid RSS Feed URL and click 'Fetch'.")

if __name__ == "__main__":
    main()
