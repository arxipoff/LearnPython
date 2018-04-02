
import os
import glob
import os.path

migrations = 'Migrations'

files = glob.glob(os.path.join(migrations, "*.sql"))

for file in files:
    print(file)



# 1) запросить input
# 2) пройтись по всем sql файлам
# 3) отобрать файлы где встречается запрос из input
# 4) вывести их названия и кол-во

# 5) записать их в прошедшие первый отбор файлы
