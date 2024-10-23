from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

#passe a variavel opts para o webdriver

navegador = webdriver.Chrome(options = opts)

url = r"https://www.kabum.com.br/"
url2 = r"https://www.dell.com/pt-br"
url3 = r"https://www.magazineluiza.com.br/"

navegador.get(url)