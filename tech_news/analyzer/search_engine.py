from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_links = []
    news = search_news({'title': {'$regex': title, '$options': 'i'}})
    for news_data in news:
        news_link = (news_data['title'], news_data['url'])
        news_links.append(news_link)
    return news_links


# Requisito 7
def search_by_date(date):
    news_links = []
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')
    news = search_news({'timestamp': {'$regex': date}})
    for news_data in news:
        news_link = (news_data['title'], news_data['url'])
        news_links.append(news_link)
    return news_links


# Requisito 8
def search_by_source(source):
    news_links = []
    news = search_news({'sources': {'$regex': source, '$options': 'i'}})
    for news_data in news:
        news_link = (news_data['title'], news_data['url'])
        news_links.append(news_link)
    return news_links


# Requisito 9
def search_by_category(category):
    news_links = []
    news = search_news({'categories': {'$regex': category, '$options': 'i'}})
    for news_data in news:
        news_link = (news_data['title'], news_data['url'])
        news_links.append(news_link)
    return news_links
