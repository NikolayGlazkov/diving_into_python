# import json
# import csv
# from typing import Iterator

my_dict = {
    "id": 1,
    "name": "Глазков Николай",
    "username": "Antonette",
    "email": ["Shanna@melissa.tv", "antonette@howel.com"],
    "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "geo": {"lat": "-43.9509", "lng": "-34.4618"},
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains",
    },
}

# # with open('temp.json', 'w') as f: #записали
# # #     json_file = json.dump(d,f,ensure_ascii=False)
# # with open("temp.json", "r", encoding="utf-8") as f:  # скачали
# #     new_dict = json.load(f)
# # print(new_dict)


# my_dikt = {
#     "id": 1,
#     "name": "Глазков Николай",
#     "username": "Antonette",
#     "email": ["Shanna@melissa.tv", "antonette@howel.com"],
#     "address": {"street": "krestianskay", "city": "volgograd", "zipcode": "9056"},
#     "phone": "89377419582",
# }

# # res = json.dumps(my_dikt,indent=2,separators=(',',':'),ensure_ascii=False)
# # print(res)

# # mystr = "hello wold!"

# # b ={key:value for key,value in enumerate(mystr)}
# # print(json.dumps(b,indent=3,separators=(',',':'),ensure_ascii=False))


# # with open('/Users/nikolay/Documents/diving_into_python/lesson8/ biostats.csv', 'r', newline='') as f:
# #     csv_file = csv.reader(f, dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC)
# #     for line in csv_file:
# #         print(line)
# # print(type(line))
# # with open('biostats_tab.csv', 'r', newline='') as f:
# #     csv_file = csv.reader(f, dialect='excel-tab',
# #     quoting=csv.QUOTE_NONNUMERIC)
# #     for line in csv_file:
# #         print(line)
# # print(type(line))

# with (
# open('biostats_tab.csv', 'r', newline='') as f_read,
# open('biostats_new.csv', 'w', newline='', encoding='utf-8')
# as f_write
# ):
#     csv_read: Iterator[dict] = csv.DictReader(f_read,fieldnames=["name", "sex", "age", "height", "weight", "office"],restval="MainOffice", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    
#     csv_write = csv.DictWriter(f_write, fieldnames=["id", "name","office", "sex", "age", "height", "weight"],dialect='excel-tab',quoting=csv.QUOTE_ALL)
#     csv_write.writeheader()
#     all_data = []
#     for i, dict_row in enumerate(csv_read):
#         if i != 0:
#             dict_row['id'] = i
#             # dict_row['age'] += 1
#             all_data.append(dict_row)
#         csv_write.writerows(all_data)

import pickle
res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.") # ноль в консоли
print(res)

res = pickle.dumps(d, protocol=pickle.DEFAULT_PROTOCOL) # словарь в виде хз чего
print(f'{res = }')

def func(a, b, c):
    return a + b + c
my_dict = {
    "numbers": [42, 4.1415, 7+3j],
    "functions": (func, sum, max),
    "others": {True, False, 'Hello world!'},
}
with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)

data =b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\
x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'
new_dict = pickle.loads(data)
print(f'{new_dict = }')


def func(a, b, c):
return a * b * c
with open('my_dict.pickle', 'rb') as f:
new_dict = pickle.load(f)
print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')