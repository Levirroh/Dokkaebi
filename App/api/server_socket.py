import socket
from dotenv import load_dotenv
import os
# carregar .env
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
# O programa espera nesse lugar até a conexão com o Agente ser estabelecida. O método accept() retorna um novo socket (conn) e o endereço do cliente (addr).
while not exit:
  conn, addr = servidor.accept()
  print(f"[+] Conexão estabelecida com: {addr}")
  
  try:
      # 1. Recebe os dados (que são em 1024 bytes)
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
            # Mova a resposta para cá!
            resposta = f"Dokkaebi: Executando {acao}".encode('utf-8')
            conn.send(resposta)
          else:
            print(f"[!] Tentativa de acesso negada para: {addr}")

        # 3. Responde ao Agente (aparentemente tem que ser em bytes a resposta)
        resposta = f"Dokkaebi: Comando '{comando}' recebido com sucesso!".encode('utf-8')
        conn.send(resposta)

  finally:
      print("Comando realizado!")
      conn.close()  # Vital para liberar o Agente e aceitar o próximo
      
      
# Só chega aqui se o loop quebrar
servidor.close()
print("[!] Servidor Dokkaebi desligado.")