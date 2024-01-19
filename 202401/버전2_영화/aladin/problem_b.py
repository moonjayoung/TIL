import json
from pprint import pprint


def book_info(book, categories):
    Kcategory = []
    for i in range(len(categories)) :
        if categories[i]['id'] in book['categoryId'] :
            Kcategory.append(categories[i]['name'])
    
    result = {}
    result['author'] = book['author']
    result['categoryName'] = Kcategory
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

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
