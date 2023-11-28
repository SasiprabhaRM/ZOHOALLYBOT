from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import helper
import os

app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    # main page
    return render_template('index.html',
                                title_text=helper.messages['index'],
                                title=helper.titles['index'],
                                id="index",
                                blog=helper.blog_posts,
                                project=helper.projects
                                )








@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    # get the title content for the portfolio page
    title_text = helper.messages['portfolio']
    title = helper.titles['portfolio']

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title=title,
                            id="portfolio",
                            projects=helper.projects,)

@app.route('/apps', methods=['POST', 'GET'])
def dashboards():
    # get the title content for the portfolio page
    title_text = helper.messages['apps']
    title = helper.titles['apps']

    return render_template('/apps.html',
                            title_text=title_text,
                            title=title,
                            id="portfolio",
                            projects=helper.apps,) # dictionary grab from module

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    # get the title content for the portfolio page
    title_text = helper.messages['blog']
    title = helper.titles['blog']

    return render_template('/blog.html',
                            title_text=title_text,
                            title=title,
                            id="portfolio",  # used in css
                            blogs=helper.blog_posts,)






@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run()