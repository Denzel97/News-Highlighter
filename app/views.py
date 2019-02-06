from flask import render_template
from app import app
from .request import get_articles

# Views
# @app.route('/article/<int:article_id>')
# def arricle(article_id):
#
#     '''
#     View article page function that returns the article details page and its data
#     '''
#     return render_template('article.html',id = article_id)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular article
    general_articles = get_articles('article')

    title = 'Home - Welcome to The best Article Review Website Online'
    return render_template('index.html', title = title, article = general_articles)
