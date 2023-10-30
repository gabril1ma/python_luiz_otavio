import requests
from bs4 import BeautifulSoup


headers =  {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

#url = "https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/"
url = "https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina=2"
#url = "https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={pag}"

# criar um for que vai percorrer pelas paginas e vai pegar os dados das reclamações de cada pagina

response = requests.get(url, headers = headers)


parsed_html = BeautifulSoup(response.text, "html.parser")

#print(response.text)s
#print(response.headers)
print(parsed_html.title)


produtos = parsed_html.select_one("#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child(2)")

print(produtos.a.text)
print(produtos.p.text)

