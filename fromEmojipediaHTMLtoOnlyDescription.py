import pandas as pd
from bs4 import BeautifulSoup
import os


htmls = os.listdir('Emojipedia')


for html in htmls:
    print("Working on ", html)
    with open (f'Emojipedia/{html}', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        desc = soup.find('section', {'class':'description'})
        with open (f'Emojipedia_text/{html}', 'w', encoding='utf-8') as ff:
            ff.write(str(desc))