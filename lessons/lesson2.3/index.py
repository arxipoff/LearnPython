import json
from pprint import pprint


arr = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json'] # список файлов с новостями


def sorted_files(f):
    # ищем слова больше 6 символов и повторяющиеся больше одного раза
    sorted_file = []

    for i in f:
        if len(i) > 6 and f.count(i) > 1:
            sorted_file.append(i)

    return sorted_file


def search_top(f):
    # ищем топ слов и делаем сортировку
    arr = []
    arr_two = []

    for n, i in enumerate(f):
        if i not in arr_two:
            arr.append([f.count(i), i])
            arr_two.append(i)

    sort_arr = sorted(arr)[::-1]

    return sort_arr[0:10:]


def get_news_text(f):
    # dытаскиваем сами статьи из json файла
    string = ''
    obj = f['rss']['channel']['items']

    for key in obj:
        string += (key['description'])

    return string.split(' ')


for doc in arr:
    with open(doc) as f:
        news_arr = get_news_text(json.load(f))
        finale_step = sorted_files(news_arr)
        top_ten = search_top(finale_step)

        print('Файл "{}", топ 10:'.format(doc))
        for n, i in enumerate(top_ten):
            print('{} место, слово "{}" ({} повторений)'.format(n + 1, i[1], i[0]))
