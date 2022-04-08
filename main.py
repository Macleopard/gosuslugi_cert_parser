import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
url = "https://www.gosuslugi.ru/covid-cert/status/14d22f26-9cf2-4437-addd-51f155c63f72?lang=ru"

def main():
    service = Service(ChromeDriverManager().install())
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(service=service, option=op) если нужно, чтобы не было видно браузера, может лагать
    # без появления
    driver.get(url)
    time.sleep(2)
    cert_id = driver.find_element(By.ID, 'cert-id').text
    status = driver.find_element(By.ID, 'status').text
    full_name = driver.find_element(By.ID, 'full-name').text
    passport = driver.find_element(By.XPATH, '//*[@id="other-attrs"]/div[2]/div[2]').text
    date = driver.find_element(By.XPATH, '//*[@id="other-attrs"]/div[1]/div[2]').text
    print(cert_id)
    print(status)
    print(full_name)
    print(date)
    print(passport)
    driver.close()


if __name__ == "__main__":
    main()
