from app import app
import urllib.request,json
from .models import article

Article = article.Article

# Getting api key
api_key = app.config['ARTICLE_API_KEY']

# Getting the article base url
base_url = app.config["ARTICLES_API_BASE_URL"]

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        title = article_item.get('original_title')
        overview = article_item.get('overview')
        poster = article_item.get('poster_path')
        vote_average = article_item.get('vote_average')
        vote_count = article_item.get('vote_count')

        if poster:
            article_object = Article(id,title,overview,poster,vote_average,vote_count)
            article_results.append(article_object)

    return article_results
