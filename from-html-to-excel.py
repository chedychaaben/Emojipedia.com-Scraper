import pandas as pd
from bs4 import BeautifulSoup
import os


htmls = os.listdir('Emojipedia')

df = pd.DataFrame({
    'CLDR' : [],
    'epd - Meaning' : [],
    'epd - Note' : [],
    'epd - Unicode' : [],
    'epd - Additional informations' : []
})

for file_counter in range(len(htmls)):
    html = htmls[file_counter]
    print("Working on ", html)
    with open (f'Emojipedia_text/{html}', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        paragraphs = soup.find('section', {'class':'description'}).find_all('p')
        meaning_paragraphs = []
        note_paragraphs = []
        unicode_paragraphs = []
        additional_info_paragraphs = []
        found_note = False
        found_unicode = False
        found_additional_info = False

        for i in range(len(paragraphs)):
            p = paragraphs[i].text
            if ('ZWJ' in p) or ('Zero Width Joiner' in p ) or ('Note:' in p ) or ('These display as a single emoji on supported platforms.' in p):
                found_note = True
            if ('was added to' in p) or ('was approved' in p ) or ('as a part of Unicode' in p ):
                found_unicode = True
            if '🚩' in p:
                found_additional_info = True
            # Appending
            if not found_note and not found_unicode and not found_additional_info:
                meaning_paragraphs.append(p)
            elif found_note and not found_unicode and not found_additional_info:
                note_paragraphs.append(p)
            elif found_unicode and not found_additional_info:
                unicode_paragraphs.append(p)
            elif found_additional_info:
                additional_info_paragraphs.append(p)


            # Combining sentences of a list
            meaning_sentence = ' '.join(sent.replace('\n','') for sent in meaning_paragraphs)
            note_sentence = ' '.join(sent.replace('\n','') for sent in note_paragraphs)
            unicode_sentence = ' '.join(sent.replace('\n','') for sent in unicode_paragraphs)
            additional_info_sentence = ' '.join(sent.replace('\n','') for sent in additional_info_paragraphs)
            # Appending from lists to dataframe finale
            name_of_this_emoji = html[:-5]
            df.loc[file_counter] = [name_of_this_emoji, meaning_sentence, note_sentence, unicode_sentence, additional_info_sentence]

df.to_csv("Emojipedia.csv", index=False) 
# DONT FORGET THAT HTML FILE ARE .lower() THAT THE CRDL in EXCEL so do excel.lower()