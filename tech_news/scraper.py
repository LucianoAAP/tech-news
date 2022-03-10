import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None

    if response.status_code == 200:
        return response.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(
        'h3 a::attr(href)'
        ).getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    url = selector.css('.tec--btn::attr(href)').get()
    return url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css('head link::attr(href)').getall()[-2]
    title = selector.css('.tec--article__header__title::text').get()
    timestamp = selector.css('time::attr(datetime)').get()
    writer = selector.css('.z--font-bold *::text').get().strip()
    shares_count = selector.css('.tec--toolbar__item::text').re_first(r'\d+')
    if not shares_count:
        shares_count = 0
    else:
        shares_count = int(shares_count)
    comments_count = int(selector.css(
        '#js-comments-btn::attr(data-count)'
        ).re_first(r'\d+'))
    summary = Selector(text=selector.css('.tec--article__body p').get())
    summary_text = ''.join(summary.css('*::text').getall())
    sources = list(selector.css('.z--mb-16 a::text').getall())
    for index in range(len(sources)):
        sources[index] = sources[index].strip()
    categories = list(selector.css('#js-categories a::text').getall())
    for index in range(len(categories)):
        categories[index] = categories[index].strip()
    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'shares_count': shares_count,
        'comments_count': comments_count,
        'summary': summary_text,
        'sources': sources,
        'categories': categories
        }


# Requisito 5
def get_tech_news(amount):
    url = 'https://www.tecmundo.com.br/novidades'
    news_urls = []
    news_urls_helper = []
    news = []
    while len(news_urls) < amount:
        html_content = fetch(url)
        scraped_urls = scrape_novidades(html_content)
        news_urls_helper.extend(scraped_urls)
        if len(news_urls_helper) < amount:
            url = scrape_next_page_link(html_content)
        if len(news_urls_helper) > amount:
            news_urls_helper = news_urls_helper[:amount]
        news_urls = news_urls_helper

    for news_url in news_urls:
        html_content = fetch(news_url)
        news.append(scrape_noticia(html_content))

    create_news(news)
    return news
