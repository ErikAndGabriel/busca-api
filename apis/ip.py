import os 
import requests
import json
from colorama import Back, init
import ipaddress

init()

def clear():
    os.system('clear')

class ApiIp:
    def __init__(self, ip):
        self.ip = ip 

    def validar(self):
        try:
            ipaddress.ip_address(self.ip)
            return True
        except ValueError:
            return False
class Buscar(ApiIp):
    def __init__(self, ip):
        self.ip = ip

    def buscar(self):
        url = f"https://ipinfo.io/{self.ip}/json"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            print("========= DADOS API =========")
            print(f"\nip: {dados['ip']}")
            print(f"cidade: {dados['city']}")
            print(f"lacalizaçao: {dados['loc']}")
            print(f"organizaçao: {dados['org']}")
            print(f"postal: {dados['postal']}")
            print(f"regiao: {dados['region']}")
            print(f"readme: {dados['readme']}")
            print("\n=============================")
            return dados
        else:
            print(f"resposta: {resposta.status_code}")
            return None


class Arquivo(Buscar):
    def __init__(self, ip, arquivo):
        super().__init__(ip)
        self.arquivo = arquivo 
    
    def salvar(self):
        dados = self.buscar()
        if dados:
            with open(f"{self.arquivo}", "w") as arq:
                json.dump(dados, arq, indent=4)
            print(f"arquivo salvo em {self.arquivo}")
def menu():
    while True:
        try:
            print("======= MENU =======")
            print("|                  |")
            print("|1. procurarIP     |")
            print("|2. sair           |")
            print("|                  |")
            print("====================")
            escolha = int(input("\nip/escolha > "))
            if escolha == 1:
                ip = input("ip a se procurar: ")
                usuario = Buscar(ip)
                usuario.buscar()
                salvar = input("deseja salvar?(s/n): ")
                if salvar == "s".lower():
                    nome_arquivo = input("nome do arquivo: ")
                    usuario = Arquivo(ip, nome_arquivo)
                    usuario.salvar()
                    input("precione [ENTER]")
                    clear()
                    continue
                else:
                    input("precione [ENTER]")
                    clear()
                    continue
            elif escolha == 2:
                print("========= EXIT ========")
                print("""obrgado por usar o ip api
feito com amor, obiigetivo de aprender ips e 
apis""")
                exit()
            else:
                print("escolha invalida!")
                input("precione [ENTER]")
                clear()
                continue

        except ValueError:
            print("somente numeros!")
            input("precione [ENTER]")
            clear()
            continue
clear()
menu() 
