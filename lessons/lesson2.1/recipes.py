cook_book = {}


def get_array_from_file(file):

    final_arr = []
    arr = []

    for line in file:
        if line.strip() != "":
            arr.append(line.strip())
        else:
            final_arr.append(arr)
            arr = []

    final_arr.append(arr)
    return final_arr


def get_final_cook_book(array):

    for i in array:
        name = i[0].lower()
        cook_book[name] = []
        for x, item in enumerate(i):
            if x != 0 and x != 1:
                cook_book[name].append({
                    'ingridient_name': item.split(' |')[0].lower(),
                    'quantity': int(item.split('|')[1]),
                    'measure': item.split('| ')[2]
                })


with open('recipes.txt') as file:
    array = get_array_from_file(file)
    get_final_cook_book(array)


def get_shop_list_by_dishes(dishes, person_count):

  shop_list = {}
  
  for dish in dishes:
    for ingridient in cook_book[dish]:

      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count

      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']

  return shop_list


def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))


def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)


create_shop_list()
