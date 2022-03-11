from typing import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_links = []
    news = find_news()
    formated_news = []
    for news_data in news:
        popularity = news_data['shares_count'] + news_data['comments_count']
        formated_news.append({
            'title': news_data['title'],
            'url': news_data['url'],
            'popularity': popularity})

    sorted_news = sorted(
        formated_news, key=lambda row: (-row['popularity'], row['title']))

    for news_data in sorted_news:
        news_link = (news_data['title'], news_data['url'])
        news_links.append(news_link)
    return news_links[:5]


# Requisito 11
def top_5_categories():
    categories_helper = []
    categories = []
    news = find_news()
    for news_data in news:
        categories_helper.extend(news_data['categories'])
    categories_instances = Counter(categories_helper).most_common()
    for instance in categories_instances:
        categories.append(instance[0])
    categories.sort()
    return categories[:5]
