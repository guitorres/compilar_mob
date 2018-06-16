# compilar_mob

Scritp Python para compilar os melhores posts de tópicos no forum http://hardmob.com.br/

# Instalação

1) Instale o python 3.x https://www.python.org/downloads/

2) Instale o beautifulsoup4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

3) Instale o requests http://docs.python-requests.org/en/master/user/install/#install

# Utilização

Basta chamar o script com o comando **python compilar_mob.py** utilizando os parâmetros:

**-t** url do tópico a ser compilado

**-v** quantidade de verdinhas mínima do post (opcional, default 10)

**-f** tamanho da fonte de saída (opcional, default 18)

**-b** página inicial (opcional, default 1)

**-e** página final (opcional, default última página)

Será gerado um arquivo com o nome saida.html.

Pode-se abrir o arquivo com o Microsoft Word ou então imprimir para o formato PDF.

# Exemplos

**python compilar_mob.py** -t http://www.hardmob.com.br/educacao-and-profissoes/566412-voce-estuda.html -v 10 -f 20

**python compilar_mob.py** -t http://www.hardmob.com.br/dinheiro-and-negocios/517074-topico-oficial-de-renda-fixa.html -v 10 -f 20 -b 500 -e 520