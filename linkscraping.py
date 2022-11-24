import snscrape.modules.twitter as sntwitter
import nltk
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_important_words(content: str):
    html = urlopen(content).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.text)


def get_image_content(link: str):
    raise NotImplementedError


def extract_content(tweetid: int | str):
    content = [i for i in sntwitter.TwitterTweetScraper(1387127854748602372).get_items()][0]
    print(content)
    isimage = True if len(content.media) > 0 else False
    if not isimage:
        return get_important_words(content)
    else:
        return get_image_content(content.media[0].fullUrl)


extract_content("https://t.co/W4zCnEsTTM")