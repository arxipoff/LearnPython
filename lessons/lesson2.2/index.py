import chardet

arr = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt'] # список файлов с новостями

def sorted_files(file):
    # ищем слова больше 6 символов и повторяющиеся больше одного раза
    sorted_file = []

    for i in file:
        if len(i) > 6 and file.count(i) > 1:
            sorted_file.append(i)

    return sorted_file


def search_top(file):
    # ищем топ слов и делаем сортировку
    arr = []
    arr_two = []

    for n, i in enumerate(file):
        if i not in arr_two:
            arr.append([file.count(i), i])
            arr_two.append(i)

    sort_arr = sorted(arr)[::-1]

    return sort_arr[0:10:]


for doc in arr:
    with open(doc, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        file = data.decode(result['encoding'])
        file = sorted_files(file.split())
        top_ten = search_top(file)

        print('Файл "{}", топ 10:'.format(doc))
        for n, i in enumerate(top_ten):
            print('{} место, слово "{}" ({} повторений)'.format(n + 1, i[1], i[0]))
