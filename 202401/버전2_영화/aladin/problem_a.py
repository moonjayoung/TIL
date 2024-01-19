import json
from pprint import pprint


def book_info(book):
    
    result = {}
    result['author'] = book['author']
    result['categoryId'] = book['categoryId']
    result['cover'] = book['cover']
    result['description'] = book['description']
    result['id'] = book['id']
    result['priceSales'] = book['priceSales']
    result['title'] = book['title']
    
    return result
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    pprint(book_info(book))
