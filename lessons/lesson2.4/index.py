
import os
import glob
import os.path


search_list = []

def get_files_name(files):
    array = files
    search_list = []
    search_name = input('Введите текст для поиска: ')

    for file in array:
        with open(file) as f:
            if search_name in f.read():
                search_list.append(f.name)
                print('{}'.format(f.name.split('Migrations/')[1]))

    print('Кол-во файлов: {}'.format(len(search_list)))
    get_files_name(search_list)





migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, "*.sql"))
get_files_name(files)



# 1) запросить input
# 2) пройтись по всем sql файлам
# 3) отобрать файлы где встречается запрос из input
# 4) вывести их названия и кол-во

# 5) записать их в прошедшие первый отбор файлы
