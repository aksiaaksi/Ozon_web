import os


import waitress

from app.lib import create_book, add_book, search_books, search_book_by_id, remove_book_by_id, create_empty_book,parse_taglines
from flask import Flask, render_template, request, redirect, url_for, app


def start():
    app = Flask(__name__)

    container = []
    wp = create_book('War and Peace', 'Tolstoy', 100, True, {'#Мир', '#Толстой', '#Наполеон'})
    ak = create_book('Anna Karenina', 'Toltoy', 50, True, {'#Толстой', '#Любовь'})

    container = add_book(container, wp)
    container = add_book(container, ak)

    @app.route('/')
    def index():
        search = request.args.get('search')

        if search:
            search_lowercased = search.strip().lower()
            result = search_books(container, search_lowercased)
            return render_template('index.html', books=result, search=search_lowercased)

        return render_template('index.html', books=container)

    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(container,book_id)
        return render_template('book-details.html', book = result)

    @app.route('/books/<book_id>/edit')
    def book_edit(book_id):
        book = None
        if book_id == 'new':
            book = create_empty_book()

        else:
            book = search_book_by_id(container, book_id)


        return render_template('book-edit.html', book=book)



    @app.route('/books/<book_id>/remove', methods=['POST'])
    def book_remove(book_id):
        nonlocal container
        container = remove_book_by_id(container, book_id)
        return redirect(url_for('index'))

    @app.route('/books/<book_id>/save', methods=['POST'])
    def book_save(book_id):
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        availability = request.form['availability']
        hashtag = parse_taglines(request.form['hashtag'])


        if book_id == 'new':
            book = create_book(title=title, author=author, price=price, availability=availability, hashtag=hashtag)
            add_book(container, book)
        else:
            book = search_book_by_id(container, book_id)
            book['title'] = title
            book['author'] = author
            book['price'] = price
            book['availability'] = availability
            book['hashtag'] = hashtag




        return redirect(url_for('book_details', book_id=book['id']))

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)



if __name__ == '__main__':
    start()


