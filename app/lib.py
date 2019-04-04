import uuid
def create_book(title, author, price, availability, hashtag):
    return {
        'id':str(uuid.uuid4()),
        'title': title,
        'author': author,
        'price': price,
        'available': availability,
        'hashtag': hashtag
    }

def create_empty_book():
    return {
        'id': uuid.UUID(int=0),
        'title': '',
        'author': '',
        'price': '',
        'available': '',
        'hashtag': ''

    }


def add_book(container, book):  # не чистая функция
    copy = container[:]
    copy.append(book)
    return copy
    # return container # TODO: вернуться к этому вопросу позже


def list_books(container, page, page_size):
    # page_size = 50
    start = (page - 1) * page_size  # для первой страницы стартуем с 0
    finish = start + page_size
    return container[start:finish]


def search_books(container, search):  # search - строка поиска
    search_lowercased = search.strip().lower()  # 1. search.strip() 2. (результат search.strip()).lower()
    result = []

    if search_lowercased == '':
        result.append()
    for book in container:

        if search_lowercased in book['title'].lower():
            result.append(book)
            continue  # не даёт идти дальше на 30 строку

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue  # пока не нужно, но на будущее пригодиться, если будем добавлять новые возможности

        for i in book['hashtag']:
            if search_lowercased == i.lower():
                result.append(book)
                continue

    return result

def search_book_by_id(container,book_id):
    for book in container:
       if book['id'] == book_id:
           return book

def remove_book_by_id(container,book_id):
    result = []
    for book  in  container:
        if book['id'] != book_id:
            result.append(book)
    return result


