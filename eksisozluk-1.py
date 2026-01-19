from selenium import webdriver
from selenium.webdriver.common.by import By

import time

#SELENIUM ile  EKŞİ SÖZLÜĞÜ SANAL BROWSERDA AÇIP ENTRY ÇEKMEYİ DENEME

#webdriver dan site açabilemk için browser oluşturulacak

browser=webdriver.Chrome()

#gidilecek sayfa
url="https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url) #url ye gitmek için veirlen komut

time.sleep(5) #sayfa yüklemesi için beklenilen süre

#by Css Selector ile sayfadki tüm entryleri alma
#bu foknsiyon aldığı paraöetredeki eleman ya da elemanları getirir

elements=browser.find_elements(By.CSS_SELECTOR,".content")
#content olan tüm içeirkleri elements listesine ata

for element in elements:
    print("***************************************")
    print(element.text)#entryleri yazdırma


browser.close()