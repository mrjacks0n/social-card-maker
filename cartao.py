from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image 
from PIL import ImageFont 
from PIL import ImageDraw 
import sys
import urllib.request
import requests

def padrao():
    n = input('seu nome: ')
    nl = input('nome no letterboxd: ')
    cp = input('comida preferida: ')
    sfa = input('personagem cujo se identifica: ')
    url = 'https://letterboxd.com/' + nl

    bannr = 'https://www.bing.com/images/search?q=' + sfa
    banner = bannr.replace(' ', '+')
    response3 = urlopen(banner)
    html3 = response3.read()
    soup3 = BeautifulSoup(html3, 'html.parser')
    bann= soup3.find('img', attrs={'class': 'mimg'}).get('src')

    response2 = urlopen(url)
    html2 = response2.read()
    soup2 = BeautifulSoup(html2, 'html.parser')
    fp = soup2.find('img').get('src')

    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    nlr = soup.find('h4').get_text()

    img = Image.open("carteira.png") 
    draw = ImageDraw.Draw(img) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((180, 180), (cp), (0, 0, 0), font=font) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((70, 160), (n), (0, 0, 0), font=font) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((230, 170), (nlr), (0, 0, 0), font=font) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((240, 193), (sfa), (0, 0, 0), font=font) 
    img.save('sample.png')

    img_data = requests.get(fp).content
    with open('buceta.jpg', 'wb') as handler:
        handler.write(img_data)

    height = 102
    width = 130
    img2 = Image.open('buceta.jpg')
    ns = img2.resize((102, 130), Image.ANTIALIAS)
    ns.save('buceta.jpg')
    img.paste(ns, (17,28))
    img.save('sample.png')

    img_data = requests.get(bann).content
    with open('buceta2.jpg', 'wb') as handler:
        handler.write(img_data)

    height = 102
    width = 130
    img3 = Image.open('buceta2.jpg')
    ns = img3.resize((184, 93), Image.ANTIALIAS)
    ns.save('buceta2.jpg')
    img.paste(ns, (184,48))
    img.save('sample.png')
    img.show('sample.png')

def mclovin():
    n = input('nome no letterboxd: ')
    dn = input('data de nascimento: ')
    cc = input('cidade "nome(sigla da região)": ')
    s = input('sexo (y/m)?: ')
    
    img = Image.open("mclovin-carteira.png") 
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial-black.ttf", 10) 
    draw.text((0, 145), (n), (0, 0, 0), font=font) 
    font = ImageFont.truetype("arial-black.ttf", 10)
    draw.text((0, 155), (cc), (0, 0, 0), font=font)
    font = ImageFont.truetype("arial-black.ttf", 12)
    draw.text((133, 60), (dn), (0, 0, 0), font=font)
    font = ImageFont.truetype("arial-black.ttf", 8)
    draw.text((244, 93), (s), (0, 0, 0), font=font)
    img.save('sample-mclovin.png')
    
    url = 'https://letterboxd.com/' + n
    response2 = urlopen(url)
    html2 = response2.read()
    soup2 = BeautifulSoup(html2, 'html.parser')
    fp = soup2.find('img').get('src')
    img_data = requests.get(fp).content
    with open('buceta.jpg', 'wb') as handler:
        handler.write(img_data)
    height = 102
    width = 130
    img2 = Image.open('buceta.jpg')
    ns = img2.resize((102, 126), Image.ANTIALIAS)
    ns.save('buceta.jpg')
    img.paste(ns, (0, 0))
    img.save('sample-mclovin.png')
    img.show('sample-mclovin.png')

def padraop():
    n = input('seu nome: ')
    nl = input('nome no letterboxd: ')
    cp = input('comida preferida: ')
    sfa = input('personagem cujo se identifica: ')
    url = 'https://letterboxd.com/' + nl

    bannr = 'https://www.bing.com/images/search?q=' + sfa
    banner = bannr.replace(' ', '+')
    response3 = urlopen(banner)
    html3 = response3.read()
    soup3 = BeautifulSoup(html3, 'html.parser')
    bann= soup3.find('img', attrs={'class': 'mimg'}).get('src')

    response2 = urlopen(url)
    html2 = response2.read()
    soup2 = BeautifulSoup(html2, 'html.parser')
    fp = soup2.find('img').get('src')

    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    nlr = soup.find('h4').get_text()

    img = Image.open("carteirap.png") 
    draw = ImageDraw.Draw(img) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((180, 180), (cp), (255, 255, 255), font=font) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((70, 160), (n), (255, 255, 255), font=font) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((230, 170), (nlr), (255, 255, 255), font=font) 

    font = ImageFont.truetype("ComicSansMS3.ttf", 20) 
    draw.text((240, 193), (sfa), (255, 255, 255), font=font) 
    img.save('sample-preto.png')
    img.show('sample-preto.png')

    img_data = requests.get(fp).content
    with open('buceta.jpg', 'wb') as handler:
        handler.write(img_data)

    height = 102
    width = 130
    img2 = Image.open('buceta.jpg')
    ns = img2.resize((102, 130), Image.ANTIALIAS)
    ns.save('buceta.jpg')
    img.paste(ns, (17,28))
    img.save('sample-preto.png')

    img_data = requests.get(bann).content
    with open('buceta2.jpg', 'wb') as handler:
        handler.write(img_data)

    height = 102
    width = 130
    img3 = Image.open('buceta2.jpg')
    ns = img3.resize((184, 93), Image.ANTIALIAS)
    ns.save('buceta2.jpg')
    img.paste(ns, (184,48))
    img.save('sample-preto.png')

def carteirame():
    n = input('seu nome: ')
    nl = input('nome no letterboxd: ')
    cp = input('comida preferida: ')
    sfa = input('personagem cujo se identifica: ')
    url = 'https://letterboxd.com/' + nl

    bannr = 'https://www.bing.com/images/search?q=' + sfa
    banner = bannr.replace(' ', '+')
    response3 = urlopen(banner)
    html3 = response3.read()
    soup3 = BeautifulSoup(html3, 'html.parser')
    bann= soup3.find('img', attrs={'class': 'mimg'}).get('src')

    response2 = urlopen(url)
    html2 = response2.read()
    soup2 = BeautifulSoup(html2, 'html.parser')
    fp = soup2.find('img').get('src')

    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    nlr = soup.find('h4').get_text()

    img = Image.open("carteiramenes.png") 
    draw = ImageDraw.Draw(img) 

    font = ImageFont.truetype("ackno.ttf", 18) 
    draw.text((190, 190), (cp), (255, 0, 0), font=font) 

    font = ImageFont.truetype("ackno.ttf", 20) 
    draw.text((70, 160), (n), (255, 0, 0), font=font) 

    font = ImageFont.truetype("ackno.ttf", 20) 
    draw.text((235, 175), (nlr), (255, 0, 0), font=font) 

    font = ImageFont.truetype("ackno.ttf", 10) 
    draw.text((240, 205), (sfa), (255, 0, 0), font=font) 
    img.save('sample-menes.png')

    img_data = requests.get(fp).content
    with open('buceta.jpg', 'wb') as handler:
        handler.write(img_data)

    height = 102
    width = 130
    img2 = Image.open('buceta.jpg')
    ns = img2.resize((102, 130), Image.ANTIALIAS)
    ns.save('buceta.jpg')
    img.paste(ns, (17,28))
    img.save('sample-menes.png')

    img_data = requests.get(bann).content
    with open('buceta2.jpg', 'wb') as handler:
        handler.write(img_data)

    height = 102
    width = 130
    img3 = Image.open('buceta2.jpg')
    ns = img3.resize((184, 93), Image.ANTIALIAS)
    ns.save('buceta2.jpg')
    img.paste(ns, (184,48))
    img.save('sample-menes.png')
    img.show('sample-menes.png')


esc = input('''
escolha o modelo:

01 - padrão
02 - padrão preto
03 - mclovin
04 - menes 2015

$-''')

if esc == '01':
    padrao()
elif esc == '02':
    padraop()
elif esc == '03':
    mclovin()
elif esc == '04':
    carteirame()
else:
    print('voce = monkey')
