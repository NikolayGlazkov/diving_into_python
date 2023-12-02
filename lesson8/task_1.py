import os
import json

with open ("text_result.txt","r",encoding='utf-8') as f: # открыть файл тхт 
    new_dict = {}
    for line in f:
        name,number= line.split()
        new_dict[name.capitalize()] = number

with open("json_result", 'w', encoding='utf-8') as f:
    json.dump(new_dict, f,indent=2,ensure_ascii=False) # записать словарь в джисан пропускать русукие буквы