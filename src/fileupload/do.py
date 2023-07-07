import csv
import json


def deserialize(file_name):
    with open(f"{file_name}") as file:
        data = json.loads(file.read())
        list_1 = []
        header_items = []
        if isinstance(data, dict):
            data = [data]
        temp = data[0]
        get_header_items(header_items, temp)
        list_1.append(header_items)

        for obj in data:
            d = []
            add_items_to_data(d, obj)
            list_1.append(d)

        # with open('output.csv', 'w') as output_file:
        #     for l in list_1:
        #         output_file.write(','.join(map(str, l)) + '\r')

        with open(f"{file_name}.csv", 'w', newline="") as output_file:
            writer = csv.writer(output_file)  # delimiter=";"
            writer.writerows(list_1)

        return f"{file_name}.csv"


def get_header_items(items, obj):
    for el in obj:  # for key, value in obj.items():
        # Перевіряємо чи є наша змінна словником, якщо так, то розбираємо його ще раз так само.
        if isinstance(obj[el], dict):
            print(obj[el])
            items.append(el)
            get_header_items(items, obj[el])
        # if isinstance(obj[el], list):
        #     items.append(el)
        #     for e in obj[el]:
        #         get_header_items(items, e)
        else:
            items.append(el)


def add_items_to_data(items, obj):
    for el in obj:
        # Перевіряємо чи є наша змінна словником, якщо так, то розбираємо його ще раз так само.
        if isinstance(obj[el], dict):
            items.append('')
            add_items_to_data(items, obj[el])
        # if isinstance(obj[el], list):
        #     items.append('')
        #     for e in obj[el]:
        #         add_items_to_data(items, e)
        else:
            items.append(obj[el])

    #     src = json.load(file)
    #     print(src)
    #
    # # Заберемо з нього всі ордери на продажу за ключем аскс(спочатку звертаємося за ключем дата)
    # asks = src["data"]["xrp_usd"]["asks"]
    # # print(asks)
    # # Щоб дізнатися результат помножимо вартість на кількість
    # for a in asks:
    #     price = a[0]
    #     coin_count = a[1]
    #     amount = price * coin_count
    #     # print(f"[INFO] Price: {price} | Coin count: {coin_count} | Amount: {amount}")
    #     with open(f"{file_name}.csv", "a", encoding="cp1251",
    #               newline="") as file:  # До раніше створеного із заголовками csv файлу з кожною ітерацією
    #         # дописуватимемо рядок
    #         writer = csv.writer(file, delimiter=";")
    #         writer.writerow(
    #             (
    #                 price,
    #                 coin_count,
    #                 amount
    #             )
    #         )
    # return f"{file_name}.csv"
