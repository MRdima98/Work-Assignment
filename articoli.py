'''
Fare uno script che analizzando il contenuto di una pagina web di notizie (ansa.it) 
scarichi le prime 5 notizie (anteprime testuali) 
presenti nella home e le salvi su un file (txt). 

Prevedere la possibilità di passare un argomento al comando. 
Se questo parametro è presente, salvare sul file txt solo le notizie
(tra le 5 analizzate) che contengano quella stringa
'''
from distutils.filelist import findall
from pickletools import string1
import urllib.request    
import re
from wsgiref.util import request_uri

# scarica su fil l'html del sito
urllib.request.urlretrieve("https://www.ansa.it/", "ansa.txt")
#urllib.request.urlretrieve("https://www.ansa.it/", "bug.txt")

# cerca tutti i titoli
with open('ansa.txt', encoding='utf-8', errors='ignore') as f:
    content = f.read()

result=re.findall('<h3 class="news-title area-primopiano"(.*)</a></h3>',content)

#svuoto il file
open('ansa.txt','w').close()

def firstFiveNews(result,s):
    f = open("ansa.txt",'a',encoding='utf-8')
    for i in range(0,5):
        cleanS=cleanString(result[i],i)
        if(s in cleanS):
            f.write(cleanS)
    f.close()

def cleanString(s,i):
    '''
    Funzione che filtra il link e formatta correttamente il ritorno a capo
    '''
    s=re.findall('.html">(.*)',s)[0]
    if('<br>' in s):
        s1=re.findall('(.*)<br>',s)[0]
        s2=re.findall('<br>(.*)',s)[0]
        s=s1+'\n'+s2
    if('<br />' in s):
        s1=re.findall('(.*)<br />',s)[0]
        s2=re.findall('<br />(,*)',s)[0]
        s=s1+'\n'+s2 
    return 'Notizia '+str(i+1)+':\n'+s+'\n\n'

if __name__ == "__main__":
    firstFiveNews(result,input("Digitare la stringa da cercare nei primi 5 ariticoli o premere enter: "))
