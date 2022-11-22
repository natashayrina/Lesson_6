# Словарь клиент. ФИО - словарь из полей имя фамилия отчество,
# email - список из 2-х email-ов(первый основной, второй дополнительный),
# sale - размер персональной скидки,
# покупки - словарь из покупок за 3 месяца(январь, февраль, март),
# к каждому месяцу значение - список покупок в этом месяце

dict_1 = {"FIO":{"surname": "Ivanov", "name": "Ivan", "midlename":"Ivanovich"}, "e-mail":["osnovnoy", "dop"], "sale": 0.15,
          "pokupki":{"jan":[10000, 20000,35000],"febr":[25000,6500,89000], "mar":[25000,35000,12000]}}

# 1)Вывести максимальную покупку за январь
# 2)Посчитать суммарную стоимость покупок за февраль с учетом персональной скидки
# 3)Если общая сумма покупок за все три месяца превышает 100000 - увеличить скидку клиента до 20%

# print(max(dict_1["pokupki"]["jan"]))

# total_sum = sum(dict_1["pokupki"]["febr"])
# total_sale = total_sum * dict_1["sale"]
# print(total_sale)
# print(total_sum)
# print(total_sum - total_sale)

total_jan = sum(dict_1["pokupki"]["jan"])
print("Январь", total_jan)
total_febr = sum(dict_1["pokupki"]["febr"])
print("Февраль", total_febr)
total_mar = sum(dict_1["pokupki"]["mar"])
print("Март", total_mar)
total_sum = total_mar+total_febr+total_jan
print(total_sum)
if total_sum>100000:
    dict_1["sale"] = 0.20
print(dict_1)