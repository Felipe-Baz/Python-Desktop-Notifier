# This python file loads the top news headlines of the day in Base_url, and parse this news in XML format 

import requests
import xml.etree.ElementTree as ET

#Url do provedor de noticias
BASE_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def load_news():
    '''
    utility function to load RSS_Feed
    '''
    # Make http request response object of BASE_URL
    response = requests.get(BASE_URL)

    # Return the context of HTTP GET in BASE_URL
    return response.content


def news_items(rss):
    '''
    utility function to parse XML format
    '''

    # Create element tree root object
    root = ET.fromstring(rss)

    # Create empty list for news items
    news_items = []

    # iterate in news items
    for item in root.findall('./channel/item'):
        # Create empty dict for news
        news = {}

        # iterate in child elements of item
        for child in item:
            # Special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

        news_items.append(news)
    
    # Return news items list
    return news_items


def top_stories():
    '''
    main function to generate and return news items
    '''

    # Load News Feed
    news = load_news()

    # Parse and return news in XML format
    return news_items(news)
