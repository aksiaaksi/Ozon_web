from app.lib import create_book, add_book, search_books
from flask import Flask, render_template, request

def main():
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
            result = search_books(container,search_lowercased)
            return render_template('index.html', books = result , search=search_lowercased)

        return render_template('index.html', books = container)

    app.run(port=9876, debug=True)


if __name__ == '__main__':
    main()