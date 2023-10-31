import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

headers =  {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

#url = "https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/"
#url = "https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina=2"
#url = "https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={pag}"

# criar um for que vai percorrer pelas paginas e vai pegar os dados das reclamações de cada pagina

#response = requests.get(url, headers = headers, timeout=2)


#parsed_html = BeautifulSoup(response.text, "html.parser")

#print(response.text)
#print(response.headers)
#print(parsed_html.div.text)


#print(parsed_html.div.text)

#produtos = parsed_html.select_one("#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-fULWyA.IJAiG.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL")
#teste = parsed_html.select_one("#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child(1)")


titulos = []
conteudo = []

'''
for i in range(2, 8):

    url = f"https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={i}"
    response = requests.get(url, headers = headers, timeout=2)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1, 11):
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child({j})")
        titulos.append(teste.h4.text)
        conteudo.append(teste.p.text)

'''

# filtro padrão 

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={i}&problema=0000000000000872"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)

# filtro internet para computador

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={i}&produto=0000000000000476"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)
    
 # filtro internet para casa

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={i}&produto=0000000000000478"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)


# filtro qualidade da internet para oi fibra

for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={i}&status=ANSWERED&problema=0000000000000872"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)

# filtro qualidade da internet para oi fibra avaliadas
for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={i}&status=EVALUATED&problema=0000000000000872"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)


# filtro internet para casa oi fibra avaliadas
for i in range(1, 51):
    url = f"https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina={i}&status=EVALUATED&produto=0000000000000478"
    response = requests.get(url, headers = headers)
    parsed_html = BeautifulSoup(response.text, "html.parser")

    for j in range(1,11):    
        teste = parsed_html.select_one(f"#__next > div.sc-1mzw716-0.fuvfGZ > div.sc-1mzw716-1.swJOp > div.wydd4i-0.bwxKmA > main > section.wydd4i-5.fUopBb > div.sc-hImiYT.golyQW.xh9b9g-0.eiNA-DU > div.sc-1sm4sxr-0.cCZuGL > div:nth-child({j})")

        try :
            titulos.append(teste.h4.text) if teste.h4.text not in titulos else titulos
            conteudo.append(teste.p.text) if teste.p.text not in conteudo else conteudo
            print("i", i)
            print("j", j)
        except AttributeError:
            print("deu none")
            pass
            print("j", j)
            print("i", i)


df = pd.DataFrame({
    "Titulos": [],
    "Conteudo": [],
    
})

for key, value in zip(titulos, conteudo):
    print(key)
    print("------------------------------------------------------")
    df = df._append({'Titulos': key,
                    'Conteudo': value},

                       ignore_index=True)



df.to_csv('oi.csv', index=False)

print(len(titulos))
print(len(conteudo))



