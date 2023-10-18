import requests
from bs4 import BeautifulSoup

def get_news_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.content, 'html.parser')

        news_links = []
        div_with_news = soup.find('div', class_='news')
        if div_with_news:
            links = div_with_news.find_all('a', href=True)
            for link in links:
                news_links.append(link['href'])

        return news_links
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    url = "http://www.i.ua/"
    news_links = get_news_links(url)

    if news_links:
        print("News links found:")
        for link in news_links:
            print(link)
    else:
        print("No news links found.")
