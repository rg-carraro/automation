import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.print_page_options import PrintOptions

options = webdriver.ChromeOptions()
options.add_argument("--headless")
URL = "www.magalu.com.br"
PRODUCT = "TV"
browser = webdriver.Chrome(chrome_options=options)
print_options = PrintOptions()

def test_1(browser, PRODUCT, URL):
    try:
        browser.get(URL)
        browser.find_element(By.CLASS_NAME, PRODUCT)
        assert URL in browser.title
    except:
        print_options.page_ranges = ['1-2']

def test_2(browser, URL):
    try:
        browser.get(URL)
        browser.find_element(By.CLASS_NAME, "select * from produto")
        assert "Resultados para" in browser.title
    except:
        print_options.page_ranges = ['1-2']

def test_3(browser, PRODUCT, URL):
    try:
        browser.get(URL)
        browser.find_element(By.CLASS_NAME, PRODUCT)
        assert URL in browser.title
        browser.findElement(By.className("listItem[1]")).submit();
        browser.findElement(By.id("bagButton")).click()
        browser.findElement(By.id("summary-continue-btn")).click()
        browser.findElement(By.id("BasketContinue-button")).click()
        browser.findElement(By.id("DeliveryPage-continue-button")).click()
        browser.findElement(By.id("pix-line")).click()
        browser.findElement(By.id("continueButton")).click()
        assert "Copiar código Pix" in browser.findElement("CopyPix_button")
    except:
        print_options.page_ranges = ['1-2']