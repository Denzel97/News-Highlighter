from flask import render_template
from app import app
from .request import get_articles

# Views
@app.route('/article/<int:article_id>')
def arricle(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular article
    popular_articles = get_articles('popular')
    upcoming_article = get_articles('upcoming')
    now_showing_article = get_articles('now_playing')
    title = 'Home - Welcome to The best Article Review Website Online'
    return render_template('index.html', title = title, popular = popular_articles, upcoming = upcoming_article, now_showing = now_showing_movie )
