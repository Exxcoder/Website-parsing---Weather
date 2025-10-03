import re

# Чтение исходных данных из txt
with open('test_data.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print('-----------------Домены-----------------') # Разделение вывода
domains = re.findall(r'\b\w+\.(?:com|ru)\b', text) # Поиск доменов с .ru и .com
for domain in domains:
    print(domain)

print('-----------------Телефоны-----------------') # Разделение вывода
phones = re.findall(r'\b[78]9?916\d{7}\b', text)
for phone in phones:
    print(phone)

print('-----------------Поиск-содержания-----------------') # Разделение вывода
lines = text.split('\n')
for line in lines:
    if '16.png' in line:
        print(line)
        break