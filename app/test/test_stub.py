from app.lib import create_book, add_book, create_empty_book, search_books, search_book_by_id, remove_book_by_id


def test_create_empty_book():

    wp = create_empty_book()

    result = create_empty_book()

    assert wp == result


def test_add_book():

    container = []
    wp = create_book('War and Peace', 'Tolstoy', 100, True, {'#Мир', '#Толстой', '#Наполеон'})

    expected = add_book(container, wp)

    result = add_book(container,wp)

    assert expected ==  result


def  test_search_book():

    container = [{ 'title':'War and Peace', 'author':'Tolstoy','price': 100, 'available': True, 'hashtag': {'#Мир', '#Толстой', '#Наполеон'}}, {'title':'Anna Karenina', 'author':'Tolstoy','price': 200, 'available': True, 'hashtag': {'#Мир', '#Толстой'}}]
    search = 'War and Peace'
    expected = search_books(container, search)

    result =  search_books(container, search)

    assert expected == result


def test_search_book_id():

    container=[]
    wp = create_book('War and Peace', 'Tolstoy', 100, True, {'#Мир', '#Толстой', '#Наполеон'})
    ak = create_book('Anna Karenina', 'Toltoy', 50, True, {'#Толстой', '#Любовь'})

    add_book(container,wp)
    add_book(container,ak)

    expected = [{ 'title':'War and Peace', 'author':'Tolstoy','price': 100, 'available': True,
                  'hashtag': {'#Мир', '#Толстой', '#Наполеон'}}]
    result= search_book_by_id(container, '122324235345')

    assert expected != result


def test_remove_book_by_id():

    container = []
    wp = create_book('War and Peace', 'Tolstoy', 100, True, {'#Мир', '#Толстой', '#Наполеон'})
    ak = create_book('Anna Karenina', 'Toltoy', 50, True, {'#Толстой', '#Любовь'})

    add_book(container, wp)
    add_book(container, ak)

    expected = [{'title': 'War and Peace', 'author': 'Tolstoy', 'price': 100, 'available': True,
      'hashtag': {'#Мир', '#Толстой', '#Наполеон'}},
     {'title': 'Anna Karenina', 'author': 'Tolstoy', 'price': 200, 'available': True,
      'hashtag': {'#Мир', '#Толстой'}}]

    result = remove_book_by_id(container, '21324235435534')

    assert  expected != result



















