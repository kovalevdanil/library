from flask import Blueprint, render_template, url_for, request
from lib.models import Author, Book, Genre

explore = Blueprint('explore', __name__, template_folder = 'templates')

@explore.route('/explore')
def index():
    if request.method == 'GET':
        books = Book.query.all()
        return render_template('explore.html', title = 'EXPLORE_TITLE', books = books)
   
    return 'Get request'
