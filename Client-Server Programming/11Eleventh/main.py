from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PASSWORD import *

def downloadAllClientServerHomeworks(chrome):
    chrome.get("https://mystat.itstep.org/ru/main/homework/page/index")
    allHomeworks = chrome.find_elements_by_class_name("homework-item")
    for item in allHomeworks:
        if item.find_element_by_class_name("all-name-spec").text == "Клієнт-серверне програмування":
            downloadLink = item.find_element_by_class_name("load-file").get_attribute("href")
            chrome.get(downloadLink)



chrome = webdriver.Chrome()  # Initialize Chrome WebDriver
wait = WebDriverWait(chrome, 10)
chrome.get("https://mystat.itstep.org/ru/auth/login/index")

elementLoginField = wait.until(EC.presence_of_element_located((By.ID, "username")))
elementLoginField.send_keys(f"{LOGIN}")
elementPasswordField = wait.until(EC.presence_of_element_located((By.ID, "password")))
elementPasswordField.send_keys(f"{PASSWORD}")
elementButtonLogin = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.login-action")))
elementButtonLogin.click()

time.sleep(5)
chrome.get("https://mystat.itstep.org/ru/main/homework/page/index")
WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "homework-item")))
allHomeworks = chrome.find_elements(By.CLASS_NAME, "homework-item")
print("Найдено домашних заданий:", len(allHomeworks))
for item in allHomeworks:
    all_name_spec = item.find_element(By.CLASS_NAME, "all-name-spec").text
    if all_name_spec == "Клієнт-серверне програмування":
        try:
            print("I TRY")
            download_link = item.find_element(By.CLASS_NAME, "load-file").get_attribute("href")
            chrome.get(download_link)
        except:
            print("Ссылка для скачивания не найдена.")

input()
chrome.quit()