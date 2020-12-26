with open('data/fairy_tail.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# task 1 -> найти уникальные слова в тексте  и подсчитать их количество
# task 1 -> отсортировать  слова в тексте по частоте
# task 1 -> найти перевод  TOP-100

text_items = content.split()
text_items_cnt = len(text_items)
print(f'слов в тексте {text_items_cnt}')

short_text_items_counter = 5
short_text_items_counter = {}
text_items_counter = {}
for el in text_items:
   el = el.lower().strip(',.')
   if not el:
       continue
   if el not in short_text_items_counter:
           short_text_items_counter[el] = 0
           short_text_items_counter[el] += 1
   else:
       if el not in text_items_counter:
           text_items_counter[el] = 0
           text_items_counter[el] += 1

print(f'уникальных слов в тексте/ коротких слов {len(text_items_counter)}/ {len(short_text_items_counter)}')

text_items_counter_ordered = dict(
    sorted(text_items_counter.items(), key=lambda x: x[1], reverse=True)[:100]
)
short_text_items_counter_ordered = dict(
    sorted(short_text_items_counter.items(), key=lambda x: x[1], reverse=True)[:100]
     )
print(f'TOP-{len(text_items_counter_ordered)}')
print(text_items_counter_ordered)
print(f'\nshort words TOP-{len(text_items_counter_ordered)}')
print(short_text_items_counter_ordered)







