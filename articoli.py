'''
Fare uno script che analizzando il contenuto di una pagina web di notizie (ansa.it) 
scarichi le prime 5 notizie (anteprime testuali) 
presenti nella home e le salvi su un file (txt). 

Prevedere la possibilità di passare un argomento al comando. 
Se questo parametro è presente, salvare sul file txt solo le notizie
(tra le 5 analizzate) che contengano quella stringa
'''
from pickletools import string1
import urllib.request    
import re
from wsgiref.util import request_uri

# scarica su fil l'html del sito
urllib.request.urlretrieve("https://www.ansa.it/", "ansa.txt")


# cerca tutti i titoli
with open('ansa.txt', encoding='utf-8', errors='ignore') as f:
    content = f.read()

result=re.findall('<h3 class="news-title area-primopiano"(.*)</a></h3>',content)

#svuoto il file
open('ansa.txt','w').close()

def firstFiveNews(result,s):
    f = open("ansa.txt",'a',encoding='utf-8')
    for i in range(0,5):
        tmp=re.findall('.html">(.*)',result[i])[0]
        if(s in tmp):
            if('<br>' in tmp):
                f.write(re.findall('.html">(.*)<br>',result[i])[0])
                f.write('. ')
                f.write(re.findall('<br>(.*)',result[i])[0])
                f.write('\n')
            else:
                f.write(tmp)
                f.write('\n')
    f.close()

if __name__ == "__main__":
    firstFiveNews(result,input("Digitare la stringa da cercare nei primi 5 ariticoli o premere enter: "))
