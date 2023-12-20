import requests
from bs4 import BeautifulSoup
import time

def scrape_news_headlines(url):
     try:
         response = requests.get(url)
         response.raise_for_status()
        
         soup = BeautifulSoup(response.text, 'html.parser')
        
         # Extract news headlines
         headlines = [headline.text.strip() for headline in soup.find_all('h2')]
        
         return headlines
     except Exception as e:
         print(f"Error: {e}")
         return []

def main():
     news_url = 'https://example-news-website.com'
    
     while True:
         headlines = scrape_news_headlines(news_url)
        
         if headlines:
             print("Latest News Headlines:")
             for idx, headline in enumerate(headlines, start=1):
                 print(f"{idx}. {headline}")
         else:
             print("No headlines found.")
        
         # Periodic request every 1 hour (can be configured at your discretion)
         time.sleep(3600)

if __name__ == "__main__":
     main()
