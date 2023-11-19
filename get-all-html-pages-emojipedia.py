import requests
import pandas as pd

# import list of CLDRS 
df = pd.read_csv('full-emoji-list-and-skincolors-ranked-2019-2021.csv')
list_of_cldrs = df["CLDR"].tolist()
# Exemples of cleaning :
#🫨shaking-face => shaking-face
#couple with heart: man, man, medium-light skin tone ==> couple-with-heart-man-man-medium-skin-tone-medium-light-skin-tone
for i in range(len(list_of_cldrs)):
    list_of_cldrs[i] = ''.join(ch for ch in list_of_cldrs[i] if (ch.isalnum() or ch =='-' or ch ==' '))
    list_of_cldrs[i] = list_of_cldrs[i].replace(':','').replace(',','').replace(' ','-')
    if list_of_cldrs[i][0] == '-':
        list_of_cldrs[i] = list_of_cldrs[i][1:]

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
with open('errors.txt', 'w', encoding='utf-8') as f:
    for e in errors:
        f.write(e + '\n')