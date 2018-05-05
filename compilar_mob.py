from bs4 import BeautifulSoup
import requests, re, pickle, webbrowser
url = "http://www.hardmob.com.br/educacao-and-profissoes/585514-clube-da-luta-contra-a-procrastinacao.html"
topico = requests.get(url)
soup = BeautifulSoup(topico.text, 'html.parser')
posts = soup.find_all('li', class_="postcontainer")
documento = []
for post in posts:
    soup = BeautifulSoup(str(post), 'html.parser')
    texto_verdinhas = soup.find('div', class_="vbseo_liked")
    verdinhas = re.search(r'mais (.*?)</a>', str(texto_verdinhas))
    if verdinhas != None:
        verdinhas = int(verdinhas.group(1))+3
        if verdinhas > 10:
            autor = str( soup.find('a', class_="username").find('strong').text )            
            data = str( soup.find('span', class_="date").text)
            link = str(soup.find('span', class_="nodecontrols").find('a'))
            cabecalho = 'Autor: {autor} Verdinhas: {verdinhas} Data: {data}'.format(autor=autor, verdinhas=verdinhas, data=data)
            texto_post = str(soup.find('div', class_="content"))
            html = '{cabecalho}<br>{link}<br>{post}'.format(cabecalho=cabecalho, link=link, post=texto_post)
            documento.append(html)

with open('documento.html', 'wb') as doc:
    pickle.dump(documento, doc)
webbrowser.open("documento.html")    
            #print(texto_post)
    #mais 18</a
    #print(texto_verdinhas)
    #print(post)