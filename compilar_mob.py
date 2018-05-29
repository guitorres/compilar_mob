from bs4 import BeautifulSoup
import requests, re, pickle, webbrowser, sys
from optparse import OptionParser
#argumentos
parser = OptionParser()
parser.add_option("-t", "--topico")
parser.add_option("-v", "--verdinhas", default=10)
parser.add_option("-f", "--fonte", default=18)                  
parser.add_option("-b", "--pagina_inicial", default=1)
parser.add_option("-e", "--pagina_final", default=0)
(options, args) = parser.parse_args()

topico = requests.get(options.topico)
paginas = int(options.pagina_final)
if paginas == 0:
    paginas =int(re.search('1 de (.*?)</a>', topico.text).group(1))


arquivo = 'saida.html'
arquivo_saida = open(arquivo, 'w')
arquivo_saida.write('<!DOCTYPE html> <html> <head><meta charset="UTF-8"/> <title>Teste</title> <style> *{{font-size:{fonte}pt}} </style></head>'.format(fonte=options.fonte))

for pagina in range(int(options.pagina_inicial), paginas+1):
    url_pagina = options.topico.replace('.html', '-{}.html'.format(pagina) )
    posts = BeautifulSoup(requests.get(url_pagina).text, 'html.parser').find_all('li', class_="postcontainer")
    melhores_posts = []
    for post in posts:
        soup = BeautifulSoup(str(post), 'html.parser')
        texto_verdinhas = soup.find('div', class_="vbseo_liked")
        verdinhas = re.search(r'mais (.*?)</a>', str(texto_verdinhas))        

        if (texto_verdinhas == None):
                verdinhas = 0
        elif (verdinhas == None):
            verdinhas = texto_verdinhas.find_all('a')
            verdinhas = len(verdinhas)
        else:
            verdinhas = int(verdinhas.group(1))+3

        autor = soup.find('a', class_="username")
        if (verdinhas >= int(options.verdinhas)) and (autor != None):            
            autor = autor.find('strong').text
            cabecalho = '<p><b>Autor:</b> {autor} <b>Verdinhas:</b> {verdinhas}</p>'.format(autor=autor, verdinhas=verdinhas)

            paragrafo_post = '<p>{}</p>'.format(soup.find('div', class_="content"))
            html = '<hr> {cabecalho} {post}'.format(cabecalho=cabecalho, post=paragrafo_post)
            melhores_posts.append(html)                

    for post in melhores_posts:            
        arquivo_saida.write("{}\n".format(post))

arquivo_saida.write("</html>")        
webbrowser.open(arquivo)      