from bs4 import BeautifulSoup
import requests, re, pickle, webbrowser
url = "http://www.hardmob.com.br/educacao-and-profissoes/585514-clube-da-luta-contra-a-procrastinacao.html"
topico = requests.get(url)
soup = BeautifulSoup(topico.text, 'html.parser')
posts = soup.find_all('li', class_="postcontainer")
lista_posts = []
#teste = re.search(r'^Pagina 1 de [0-9]+$', posts.text.encode('iso-8859-1'))
#print(teste)
for post in posts:
    soup = BeautifulSoup(str(post), 'html.parser')
    texto_verdinhas = soup.find('div', class_="vbseo_liked")
    verdinhas = re.search(r'mais (.*?)</a>', str(texto_verdinhas))
    if verdinhas != None:
        verdinhas = int(verdinhas.group(1))+3
        if verdinhas > 10:
            autor = soup.find('a', class_="username").find('strong').text.encode('iso-8859-1')            
            data = soup.find('span', class_="date").text.encode('iso-8859-1')
            #link = soup.find('span', class_="nodecontrols").find('a').get('href').encode('iso-8859-1')

            cabecalho = '<p><b>Autor:</b> {autor} <b>Verdinhas:</b> {verdinhas} <b>Data:</b> {data}</p>'\
                        .format(autor=autor, verdinhas=verdinhas, data=data)

            texto_post = soup.find('div', class_="content").encode('iso-8859-1')
            html = '{cabecalho}<p>{post}</p>'.format(cabecalho=cabecalho, post=texto_post)
            lista_posts.append(html)

documento_html = open('documento.html', 'w')
for post in lista_posts:
  documento_html.write("%s\n" % post)
webbrowser.open("documento.html")      
#with open('documento.html', 'wb') as doc:
#    pickle.dump(documento, doc)
            #print(texto_post)
    #mais 18</a
    #print(texto_verdinhas)
    #print(post)
#Página 1 de 13    