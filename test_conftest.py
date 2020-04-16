from selenium import webdriver

# Указываем полный путь к geckodriver.exe на вашем ПК.
driver = webdriver.Firefox('C:\\geckodriver\\geckodriver.exe')
driver.get("http://www.google.com")

