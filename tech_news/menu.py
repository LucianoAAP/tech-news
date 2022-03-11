import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def top_5_analizer(option):
    if option == '5':
        return print(top_5_news())
    if option == '6':
        return print(top_5_categories())


def count_analizer(option):
    if option == '0':
        next_option = input('Digite quantas notícias serão buscadas:')
        return print(get_tech_news(next_option))


def search_analyzer(option):
    if option == '1':
        next_option = input('Digite o título:')
        return print(search_by_title(next_option))
    if option == '2':
        next_option = input('Digite a data no formato aaaa-mm-dd:')
        return print(search_by_date(next_option))
    if option == '3':
        next_option = input('Digite a fonte:')
        return print(search_by_source(next_option))
    if option == '4':
        next_option = input('Digite a categoria:')
        return print(search_by_category(next_option))


# Requisito 12
def analyzer_menu():
    print('Selecione uma das opções a seguir:\n'
          ' 0 - Popular o banco com notícias;\n'
          ' 1 - Buscar notícias por título;\n'
          ' 2 - Buscar notícias por data;\n'
          ' 3 - Buscar notícias por fonte;\n'
          ' 4 - Buscar notícias por categoria;\n'
          ' 5 - Listar top 5 notícias;\n'
          ' 6 - Listar top 5 categorias;\n'
          ' 7 - Sair.', end='')

    option = input()
    if option not in ['0', '1', '2', '3', '4', '5', '6', '7']:
        sys.stderr.write("Opção inválida\n")
    if option == '7':
        return print('Encerrando script\n')
    top_5_analizer(option)
    count_analizer(option)
    search_analyzer(option)
