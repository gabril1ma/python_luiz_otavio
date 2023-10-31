from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

ROOT_FOLDER = Path(__file__).parent

CHROMEDRIVER_EXEC = ROOT_FOLDER / "drivers" / "chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=CHROMEDRIVER_EXEC)
chrome_browser = webdriver.Chrome(
    
    service=chrome_service,
    options=chrome_options,
)

chrome_browser.get("https://www.reclameaqui.com.br/empresa/oi-internet/lista-reclamacoes/?pagina=2")

time.sleep(10)


