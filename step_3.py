with open('data/kpk.kss45.ru_timetable.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# print(content)
content_items = content.split('<a ')
valid_refs = []
for el in content_items[1:]:
   ref_content = el.split('</a>')[0]
   if 'Расписание' not in ref_content or '.xls' not in ref_content:
     continue
   clean_ref_content = ref_content.split('href="')[1].split('"')[0]
   valid_refs.append(clean_ref_content)

# print(ref_content)
# print('-' * 80)

print(f'valid references {len(valid_refs)}')
print(*valid_refs, sep='\n\n')
