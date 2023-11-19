import requests
import pandas as pd

list_of_cldrs = []
with open('errors.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        line = line[23:-1].lower()
        list_of_cldrs.append(line)


errors = []
for cldr in list_of_cldrs:
    url = f'https://emojipedia.org/{cldr}/'
    r = requests.get(url)
    if r.status_code == 200:
        with open(f'Emojipedia/{cldr}.html', 'w', encoding='utf8') as fp:
            fp.write(r.text)
    else:
        errors.append(url)

# Save Errors to txt 
with open('errors_2.txt', 'w', encoding='utf-8') as f:
    for e in errors:
        f.write(e + '\n')