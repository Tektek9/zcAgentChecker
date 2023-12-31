from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
from bs4 import BeautifulSoup
import requests  
import sys
from datetime import datetime

email = "emailmu"
passwd = "passwordmu"
url = "zoneadmin urlmu"

print("\n===============================")
print("=  Bulk ZCloud Agent Checker  =")
print("===============================")
print("1. Cek All Agent zCloud")
print("2. Simple check")
print("3. Monitoring All Agent zCloud")
print("4. Keluar")
jawaban =  int(input("Silahkan pilih menu diatas: "))
print("\n")

tanggal = datetime.now()

def serverwithAgent():    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome_driver = '/chromedriver_win32'
    driver = webdriver.Chrome(chrome_driver, options=options)
    driver.get(url1)
    time.sleep(1)

    ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/input')
    ngetik.send_keys(email)

    ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/input')    
    ngetik.send_keys(passwd)
    
    ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/button')
    ngetik.click()
    time.sleep(1)
    print("\n")

    halaman = driver.page_source
    soup = BeautifulSoup(halaman, "html.parser")
    tdbody = soup.select_one('table > tbody')
    if tdbody:
        target = tdbody.find_all("tr")

        for row in target:
            td1 = row.select_one('td:nth-of-type(1)')
            td2 = row.select_one('td:nth-of-type(2)')
            
            if td1 and td2 :
                val1 = td1.get_text()
                val2 = td2.get_text()
                print("Nama Server = ", val1)
                print("Last Seen   = ", val2, "\n")

def  ngeceksuimpel():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome_driver = '/chromedriver_win32'
    driver = webdriver.Chrome(chrome_driver, options=options)
    driver.get(url1)
    time.sleep(1)

    ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/input')
    ngetik.send_keys(email)

    ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/input')    
    ngetik.send_keys(passwd)
    
    ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/button')
    ngetik.click()
    time.sleep(1)
    print("\n")

    ngetik = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/div/div[3]/div[2]/div[2]/div[2]')
    tulisan = ngetik.text
    if tulisan.find("No problems found") != -1:
        print("Zcloud aman boskuh :*\n")
    else:
        print("Zcloud rodok goyang, satset ",url)

def monitoring():
    a = 0
    while True:
        if a != 25:
            serverwithAgent()
            a += 1
            # print(f"monitor ke {a}")
            time.sleep(5)
            print(tanggal)
        elif a == 25:
            takon = str(input("Apakah anda ingin lanjut melakukan monitoring Y/N ?? "))
            if takon == "Y" or takon == "y":
                monitoring()
            else:
                print("Maaf inputan tidak jelas, program auto close ya :V")
                sys.exit()
    
t = threading.Thread(target=monitoring)

if jawaban == 1: 
    try:
        sc = requests.get(url)
        if sc.status_code == 200 :
            url1 = url
            serverwithAgent()
        takon = str(input("Apakah anda ingin keluar dari aplikasi ini Y/N??"))
        if takon == "Y":
            print("Terimakasih salam kuli boskuh :*")
            sys.exit()
        else:
            print("")
    except requests.exceptions.ConnectionError:
        print("Request error\n")
elif jawaban == 2:
    try:
        sc = requests.get(url)
        if sc.status_code == 200 :
            url1 = url
            ngeceksuimpel()
        takon = str(input("Apakah anda ingin keluar dari aplikasi ini Y/N??"))
        if takon == "Y":
            print("Terimakasih salam kuli boskuh :*")
            sys.exit()
        else:
            print("")
    except requests.exceptions.ConnectionError:
        print("Request Error\n")
elif jawaban == 3:
    try:
        sc = requests.get(url)
        if sc.status_code == 200 :
            url1 = url
            t.start()
    except requests.exceptions.ConnectionError:
        print("Request Error\n")
elif jawaban == 4:
    print("Terimakasih salam kuli boskuh :*")
    sys.exit()
else:
    print("Silahkan masukan dengan benar ya boskuh XD")
