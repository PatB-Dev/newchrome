from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.google.fr/")

# clique refus google.fr
element = driver.find_element(By.XPATH, "//*[@id='W0wltc']")
element.click()

x = 0
table = ['bonjour', 'revoir', 'salut', 'hello', 'airbus', 'premier vol']

while x < 6:
    variable = table[x]
    driver.get(format("https://www.google.fr/search?q=" + variable))
    search = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
    x = x+1



