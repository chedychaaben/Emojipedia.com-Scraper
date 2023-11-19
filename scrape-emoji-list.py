from bs4 import BeautifulSoup
import pandas as pd
import pygsheets


df = pd.DataFrame({
    'Number' : [],
    'Code' : [],
    'Emoji' : [],
    'CLDR' : [],
    'AppleSVG' : [],
    'GoogleSVG' : [],
    'FacebookSVG' : [],
    'WindSVG' : [],
    'TwitterSVG' : [],
    'JoySVG' : [],
    'SamsungSVG' : [],
    'GmailSVG' : [],
    'SbSVG' : [],
    'DcmSVG' : [],
    'KddiSVG' : [],
})

def getSVG(e):
    try:
        return e.find('img')['src']
    except:
        return ''
the_real_line = 0
'''
with open('full-emoji-list.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    table = soup.find('table')
    lines = table.find_all('tr')
    for i in range(len(lines)):
        line = lines[i]
        try:
            # Testing if it's possible to have this unique thing
            line.find_all('td', {'class':'rchars'})[0].text
            # Test ok then go and do
            this_line = line.find_all('td')
            # if it has 15 elements of columns then this
            if len(this_line) == 15:
                id = this_line[0].text
                code = this_line[1].text
                emoji = this_line[2].text
                apple= getSVG(this_line[3])
                google= getSVG(this_line[4])
                facebook= getSVG(this_line[5])
                wind= getSVG(this_line[6])
                twitter= getSVG(this_line[7])
                joy= getSVG(this_line[8])
                samsung= getSVG(this_line[9])
                gmail= getSVG(this_line[10])
                sb= getSVG(this_line[11])
                dcm= getSVG(this_line[12])
                kddi= getSVG(this_line[13])
                Cldr = this_line[14].text
                df.loc[the_real_line+i] = [id, code, emoji, Cldr, apple, google, facebook, wind, twitter, joy, samsung, gmail, sb, dcm, kddi]
            elif len(this_line) == 5:
                id = this_line[0].text
                code = this_line[1].text
                emoji = this_line[2].text
                apple= ''
                google= getSVG(this_line[3])
                facebook= ''
                wind= ''
                twitter= ''
                joy= ''
                samsung= ''
                gmail= ''
                sb= ''
                dcm= ''
                kddi= ''
                Cldr = this_line[4].text
                df.loc[the_real_line+i] = [id, code, emoji, Cldr, apple, google, facebook, wind, twitter, joy, samsung, gmail, sb, dcm, kddi]

            if i == len(lines)-1:
                the_real_line = i
        except:
            pass
'''
with open('full-emoji-modifiers.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    table = soup.find('table')
    lines = table.find_all('tr')
    for i in range(len(lines)):
        line = lines[i]
        try:
            # Testing if it's possible to have this unique thing
            line.find_all('td', {'class':'rchars'})[0].text
            # Test ok then go and do
            this_line = line.find_all('td')
            # if it has 15 elements of columns then this
            if len(this_line) == 15:
                id = this_line[0].text
                code = this_line[1].text
                emoji = this_line[2].text
                apple= getSVG(this_line[3])
                google= getSVG(this_line[4])
                facebook= getSVG(this_line[5])
                wind= getSVG(this_line[6])
                twitter= getSVG(this_line[7])
                joy= getSVG(this_line[8])
                samsung= getSVG(this_line[9])
                gmail= getSVG(this_line[10])
                sb= getSVG(this_line[11])
                dcm= getSVG(this_line[12])
                kddi= getSVG(this_line[13])
                Cldr = this_line[14].text
                df.loc[the_real_line+i] = [id, code, emoji, Cldr, apple, google, facebook, wind, twitter, joy, samsung, gmail, sb, dcm, kddi]
            elif len(this_line) == 5:
                id = this_line[0].text
                code = this_line[1].text
                emoji = this_line[2].text
                apple= ''
                google= getSVG(this_line[3])
                facebook= ''
                wind= ''
                twitter= ''
                joy= ''
                samsung= ''
                gmail= ''
                sb= ''
                dcm= ''
                kddi= ''
                Cldr = this_line[4].text
                df.loc[the_real_line+i] = [id, code, emoji, Cldr, apple, google, facebook, wind, twitter, joy, samsung, gmail, sb, dcm, kddi]

            if i == len(lines)-1:
                the_real_line = i
        except:
            pass

df.to_csv("full-emoji-modifiers.csv", index=False) #-and-modifiers