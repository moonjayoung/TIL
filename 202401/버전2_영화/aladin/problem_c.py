import json
from pprint import pprint


def books_info(books, categories):    


    Kcategory = []
    for n in range(len(books)) : 
        Kcategory2 = []
        for i in range(len(categories)) :
            if categories[i]['id'] in books[n]['categoryId'] :
                Kcategory2.append(categories[i]['name'])
                Kcategory.append(Kcategory2)   

    bookLst = []
    result = {} 

    for n in range(len(books)) : 

        result['author'] = books[n]['author']
        result['categoryName'] = Kcategory[n]
        result['cover'] = books[n]['cover']
        result['description'] = books[n]['description']
        result['id'] = books[n]['id']
        result['priceSales'] = books[n]['priceSales']
        result['title'] = books[n]['title']
        bookLst.append(result)
    
    return bookLst



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
