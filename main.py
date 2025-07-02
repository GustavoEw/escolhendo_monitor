
from monitors_utility import listar_monitores
from screenshot_save import screeshot_save
from screenshot import screenshot
import mss
import mss.tools
import os
monitores = listar_monitores()
for i, monitor in enumerate(monitores,start=1):
        print (f"{i}.monitor - {monitores}")
while True:
    
    escolha = input("digite o numero do monitor" )
    if escolha.lower()=="sair":
         print("encerrando...")
         break

    try: 
        indice = int (escolha)

    except ValueError:
        print("vc não digitou um numero")
        continue
        
    if indice <1 or indice >len(monitores):
            print("monitor invalido. ")
            continue
    imagem = screenshot(monitores,indice)
    screeshot_save(imagem)