from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

chrome_browser.get("https://www.kabum.com.br")

search_input = WebDriverWait(chrome_browser, 10).until(
    EC.presence_of_element_located((By.NAME, "query")
    )
)

search_input.send_keys("placa de video")
search_input.send_keys(Keys.ENTER)

time.sleep(10)


