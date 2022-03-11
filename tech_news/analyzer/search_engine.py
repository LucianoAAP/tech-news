from tech_news.database import search_news, find_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
