#SELENIUM ile RASTGELE SAYFALARA GİDİP RASTEGLE 100 ENTRY TOPLAMA

#--- Syafalara Tarayıcıdan adresleme ile erişilebiliyor =100 =45  gibi
#Yapılacaklar
#Ekşide şuanda Mustafa Kemal Atatürk başlığında 3188 sayfa girdi mevcut
#Radnom üretici bu sınırlar içerisnde tutularak random sayfalara erişilecek
#10 sayfa 10 girdi

#Radnom sayı url nin sonuna eklenerek yeni link oluşturulacak
#oluşturulan link ile gidilen sayfada girsiler listeye kaydedilecek



from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time


browser=webdriver.Chrome()#sanal taryıcı

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

for entry in entries:

    print(f"{entryCount} . girdi *********************")
    print(element.text)
    entryCount += 1

browser.close()


