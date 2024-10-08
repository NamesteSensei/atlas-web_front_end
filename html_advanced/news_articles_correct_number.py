#!/usr/bin/env python3
from bs4 import BeautifulSoup

# Open and read the HTML file
with open('6-index.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the 'Latest news' section
latest_news_section = soup.find_all('section', text='Latest news section')

if latest_news_section:
    # Find all 'article' tags within the 'Latest news' section
    latest_news_articles = latest_news_section[0].find_all('article')

    # Check if there are exactly 3 'article' tags
    if len(latest_news_articles) == 3:
        print("3")
    else:
        print(f"incorrect number of sections: {len(latest_news_articles)}")
else:
    print("Latest news section not found")
