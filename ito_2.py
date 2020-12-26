#  f = open('data/fairy_tail.txt', 'r', encoding='utf-8')
#  content = f.read()
#  f.close()

with open('data/fairy_tail.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# print(content)

# task 1 -> найти уникальные слова в тексте  и подсчитать их количество
# task 1 -> отсортировать  слова в тексте по частоте
# task 1 -> найти перевод  TOP-100

text_items = content.split()
text_items_cnt = len(text_items)
# print('слов в тексте', text_items)
print(f'слов в тексте {text_items_cnt}')

text_items_counter = {}
for el in text_items:
    el = el.lower()
    if el not in text_items_counter:
        text_items_counter[el] = 0
    text_items_counter[el] += 1

print(f'уникальных слов в тексте {len(text_items_counter)}')
print(text_items_counter)




