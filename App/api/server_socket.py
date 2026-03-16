import socket
from dotenv import load_dotenv
import os
load_dotenv()

AF_INET = socket.AF_INET # PIv4
SOCK_STREAM = socket.SOCK_STREAM # TCP

servidor = socket.socket(AF_INET, SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((os.getenv("IP_DOKKA"), int(os.getenv("PORTA"))))

servidor.listen(5)

def isValidKey(chave):
		return chave == os.getenv("CHAVE_MESTRA")


print(f"[*] Dokkaebi ouvindo em {os.getenv('IP_DOKKA')}:{os.getenv('PORTA')}...")
servidor.listen(5)
exit = False
while not exit:
  conn, addr = servidor.accept()
  print(f"[+] Conexão estabelecida com: {addr}")
  
  try:
      dados = conn.recv(1024)
      if not dados:
          print("[-] Conexão fechada pelo Agente.")
      else:
        comando = dados.decode('utf-8').strip()
        
        if (":" in comando):
          partes = comando.split(":")
          chave = partes[0]
          acao = partes[1]
          
          print(f"[*] Comando recebido do Agente: {comando}")
          
          if isValidKey(chave):
            print(f"[*] Chave válida! Executando: {acao}")
            resposta = f"Dokkaebi: Executando {acao}".encode('utf-8')
            conn.send(resposta)
          else:
            print(f"[!] Tentativa de acesso negada para: {addr}")

        resposta = f"Dokkaebi: Comando '{comando}' recebido com sucesso!".encode('utf-8')
        conn.send(resposta)

  finally:
      print("Comando realizado!")
      conn.close() 
      
      
servidor.close()
print("[!] Servidor Dokkaebi desligado.")