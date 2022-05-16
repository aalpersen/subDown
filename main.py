import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime


def main( ):
    driver_path = r'C:\selenium\geckodriver.exe'
    binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    subtitle_address = "https://turkcealtyazi.org/mov/2805096/chicago-pd.html"

    options = webdriver.FirefoxOptions()
    options.binary_location = binary_path
    driver = webdriver.Firefox(executable_path = driver_path, options=options)

    altyazi_links = []
    #start page retreival
    driver.get(subtitle_address)
    altyazidiv = driver.find_element(By.ID, "altyazilar")
    altyazilar = altyazidiv.find_elements(By.XPATH, "//a[@href]")
    print(altyazilar)
    for eleman in altyazilar:
        templink = eleman.get_attribute("href")
        if "/sub/" in templink:
            altyazi_links.append(templink)
    print(altyazi_links)

    for link in altyazi_links:
        acilacak = "window.open(\""+link+"\",\"_blank\");"
        driver.execute_script(acilacak)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(15)
        buton_div = driver.find_element(By.CLASS_NAME, "nblock")
        # butond = buton_div.find_element(By.ID, "")
        buton = buton_div.find_element(By.CLASS_NAME, "altIndirButton")
        buton.click()

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    driver.quit()


if __name__ == "__main__":
    main()

