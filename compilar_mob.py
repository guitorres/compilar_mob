from bs4 import BeautifulSoup
import requests, re, pickle, webbrowser, sys
from optparse import OptionParser
#argumentos
parser = OptionParser()
parser.add_option("-t", "--topico", dest="topico")
parser.add_option("-v", "--verdinhas", default=10)
parser.add_option("-f", "--fonte", default=18)                  
(options, args) = parser.parse_args()

topico = requests.get(options.topico)
paginas =int(re.search('1 de (.*?)</a>', topico.text).group(1))

arquivo = 'documento.html'
arquivo_saida = open(arquivo, 'w')
arquivo_saida.write('<!DOCTYPE html> <html> <head><meta charset="UTF-8"/> <title>Teste</title> <style> *{{font-size:{fonte}pt}} </style></head>'\
    .format(fonte=options.fonte))

for pagina in range(1, paginas+1):
    url_pagina = options.topico.replace('.html', '-{}.html'.format(pagina) )
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
            if verdinhas >= int(options.verdinhas):
                autor = soup.find('a', class_="username").find('strong').text
                cabecalho = '<p><b>Autor:</b> {autor} <b>Verdinhas:</b> {verdinhas}</p>'\
                            .format(autor=autor, verdinhas=verdinhas)

                texto_post = soup.find('div', class_="content")
                print(texto_post)
                html = '{cabecalho}<p>{post}</p>'.format(cabecalho=cabecalho, post=texto_post)
                melhores_posts.append(html)                
    for post in melhores_posts:            
        arquivo_saida.write("{}\n".format(post))

arquivo_saida.write("</html>")        
webbrowser.open(arquivo)      