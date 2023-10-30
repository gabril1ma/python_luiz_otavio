from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

navegador = webdriver.Firefox()
url = "https://www.reclameaqui.com.br"
agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
navegador.get(url)
time.sleep(3)
caminho = navegador.find_element(By.CSS_SELECTOR, '.gap-16 > div:nth-child(1) > a:nth-child(2) > img:nth-child(1)')
navegador.execute_script("arguments[0].scrollIntoView();", caminho)
time.sleep(3)
moda = navegador.find_element(By.CSS_SELECTOR, 'button.inline:nth-child(2)')
moda.click()
df = pd.DataFrame({
    'Empresa': [],
    'Reclamacoes Respondidas': [],
    'Voltaria a Fazer Negocio': [],
    'Indice de Solucao': [],
    'Nota do Consumidor': []
})

def melhoresEmpresas():


    global df
    for i in range(2, 5):
        melhoresEmp = navegador.find_element(By.CSS_SELECTOR, f'div.min-h-\[616px\]:nth-child(1) > a:nth-child({i})')
        melhoresEmp.click()
        time.sleep(2)
        empNome = navegador.find_element(By.CSS_SELECTOR, '.short-name' )
        respondidas = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(2) > span:nth-child(2)')
        fazerNegocio = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(4) > span:nth-child(2)')
        indiceSolucao = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(6) > span:nth-child(2)')
        notaConsumidor = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(8) > span:nth-child(2)')
        df = df._append({'Empresa': empNome.text,
                        'Reclamacoes Respondidas': respondidas.text,
                        'Voltaria a Fazer Negocio': fazerNegocio.text,
                        'Indice de Solucao': indiceSolucao.text,
                        'Nota do Consumidor': notaConsumidor.text},
                       ignore_index=True)

        navegador.back()
        moda = navegador.find_element(By.CSS_SELECTOR, 'button.inline:nth-child(2)')
        caminho = navegador.find_element(By.CSS_SELECTOR, '.gap-16 > div:nth-child(1) > a:nth-child(2) > img:nth-child(1)')
        navegador.execute_script("arguments[0].scrollIntoView();", caminho)
        moda.click()
        time.sleep(2)


    df.to_csv('C:/Users/xxdav/Downloads/melhores_empresas.csv', index=False)


def pioresEmpresas():
    df = pd.DataFrame({
        'Empresa': [],
        'Reclamacoes Respondidas': [],
        'Voltaria a Fazer Negocio': [],
        'Indice de Solucao': [],
        'Nota do Consumidor': []
    })

    for i in range(2, 5):
        pioresEmp = navegador.find_element(By.CSS_SELECTOR, f'div.rounded-md:nth-child(2) > a:nth-child({i})')
        pioresEmp.click()
        time.sleep(2)
        empNome = navegador.find_element(By.CSS_SELECTOR, '.short-name')
        respondidas = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(2) > span:nth-child(2)')
        fazerNegocio = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(4) > span:nth-child(2)')
        indiceSolucao = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(6) > span:nth-child(2)')
        notaConsumidor = navegador.find_element(By.CSS_SELECTOR, 'div.sc-9xbj9-0:nth-child(8) > span:nth-child(2)')
        df = df._append({'Empresa': empNome.text,
                         'Reclamacoes Respondidas': respondidas.text,
                         'Voltaria a Fazer Negocio': fazerNegocio.text,
                         'Indice de Solucao': indiceSolucao.text,
                         'Nota do Consumidor': notaConsumidor.text},
                        ignore_index=True)

        navegador.back()
        moda = navegador.find_element(By.CSS_SELECTOR, 'button.inline:nth-child(2)')
        caminho = navegador.find_element(By.CSS_SELECTOR,
                                         '.gap-16 > div:nth-child(1) > a:nth-child(2) > img:nth-child(1)')
        navegador.execute_script("arguments[0].scrollIntoView();", caminho)
        moda.click()
        time.sleep(2)
    df.to_csv('C:/Users/xxdav/Downloads/piores_empresas.csv', index=False)

melhoresEmpresas()
pioresEmpresas()