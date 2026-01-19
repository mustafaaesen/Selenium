# 2. örnekte alınan girdileri bir adım ileriye taşıyaray dosya açma ve ona kaydetme


from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

browser=webdriver.Chrome()


url="https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="#gidilecek link

#p deki sayı değeri randomdan alınmaya çalışılacak
pageCount=1

entries= []
entryCount=1

while pageCount<=10:
    randomPage=random.randint(1,3188) #gidilecek rastgele sayfa

    newUrl = url + str(randomPage) #random page değeri str olarak linkinin sonuna eklenir ve gönderilir
    browser.get(newUrl)#başlatma metodu
    elements= browser.find_elements(By.CSS_SELECTOR,".content")
    #her sayfadaki girdileri bulma
    time.sleep(2) #her sayfada 5 saniye bekleme

    for element in elements: #girdilerdeki metinleri listeye atama

        entries.append(element.text)
    
    pageCount += 1

with open("entry.txt","w",encoding="utf-8") as file:

    for entry in entries:

        file.write(str(entryCount) + ".\n" + entry + ".\n")
        file.write("************************************\n")
        entryCount += 1

browser.close()