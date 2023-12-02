# # Напишите функцию, которая в бесконечном
# # цикле запрашивает имя, личный идентификатор
# # и уровень доступа (от 1 до 7).
# # После каждого ввода добавляйте новую информацию в JSON файл.
# # Пользователи группируются по уровню доступа.
# # Идентификатор пользователя выступает ключём для имени.
# # Убедитесь, что все идентификаторы уникальны
# # независимо от уровня доступа. При перезапуске функции
# # уже записанные в файл данные должны сохраняться.
# import json
# import os


# def func(file_name):
#     store_id = set()
#     if os.path.exists(file_name):
#         with open(file_name, "r", encoding='utf-8') as f:
#             new_dict = json.load(f)
#             for _, value in new_dict():
#     else:
#         new_dict = {i:{} for i in range(1,8)}
#     while True:
#         name = input("Введите имя")
#         if name == "help":
#             break
#         if not name:
#             print("имя недолжно бть пустым")
#             continue
#         _id = int(input("Введите id"))
#         if _id in store_id:
#             print(f"данный пользователь с {_id} id  уже добавлен")
#             continue
#         level = int(input("Ведите"))
#         if level not in new_dict:
#             print(" lдолжен быть 1 до 7")
#             continue
#         store_id.add(id)
#         new_dict[level].update({_id: name})
#         print(new_dict)
#         with open(file_name, 'w', encoding='utf-8') as f:
#             json.dump(new_dict, f,indent=2,ensure_ascii=False) # записать словарь в джисан пропускать русук

# func()