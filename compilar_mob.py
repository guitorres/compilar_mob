# coding: iso-8859-1
from bs4 import BeautifulSoup
import requests, re, pickle, webbrowser, sys
url = sys.argv[1]
topico = requests.get(url)
pagina_pattern = '<a href="javascript://" class="popupctrl">Página 1 de (.*?)</a>'.decode('iso-8859-1')
paginas =int(re.search(pagina_pattern, topico.text.encode('iso-8859-1')).group(1))
arquivo_saida = open('documento.html', 'w')
verdinhas_corte = int(sys.argv[2])
for pagina in range(1, paginas+1):
    url_pagina = url.replace('.html', '-{}.html'.format(pagina) )
    topico = requests.get(url_pagina)
    soup = BeautifulSoup(topico.text, 'html.parser')
    posts = soup.find_all('li', class_="postcontainer")    
    melhores_posts = []
    for post in posts:
        soup = BeautifulSoup(str(post), 'html.parser')
        texto_verdinhas = soup.find('div', class_="vbseo_liked")
        verdinhas = re.search(r'mais (.*?)</a>', str(texto_verdinhas))
        if verdinhas != None:
            verdinhas = int(verdinhas.group(1))+3
            if verdinhas > verdinhas_corte:
                autor = soup.find('a', class_="username").find('strong').text.encode('iso-8859-1')            
                data_post = soup.find('span', class_="date").text.encode('iso-8859-1')
                cabecalho = '<p><b>Autor:</b> {autor} <b>Verdinhas:</b> {verdinhas} <b>Data:</b> {data_post}</p>'\
                            .format(autor=autor, verdinhas=verdinhas, data_post=data_post)

                texto_post = soup.find('div', class_="content").encode('iso-8859-1')
                html = '{cabecalho}<p>{post}</p>'.format(cabecalho=cabecalho, post=texto_post)
                melhores_posts.append(html)
    for post in melhores_posts:            
        arquivo_saida.write("%s\n" % post)
webbrowser.open("documento.html")      