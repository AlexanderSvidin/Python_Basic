shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

def details_status(detail):
    count_detail = 0
    detail_cost = 0

    for product in shop:
        if product[0].casefold() == detail.casefold():
            count_detail += 1
            detail_cost += product[1]

    print('\nКоличество деталей:', count_detail)
    print('Общая стоимость:', detail_cost)

detail_name = input('Введите название детали: ')

details_status(detail_name)