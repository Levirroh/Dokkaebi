import socket

IP_DOKKA = "100.111.192.88" 
PORTA = 5005
AF_INET = socket.AF_INET # PIv4
SOCK_STREAM = socket.SOCK_STREAM # TCP

servidor = socket.socket(AF_INET, SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((IP_DOKKA, PORTA))

servidor.listen(5)

print(f"[*] Dokkaebi ouvindo em {IP_DOKKA}:{PORTA}...")
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
          print(f"[*] Comando recebido do Agente: {comando}")

          # 3. Responde ao Agente (aparentemente tem que ser em bytes a resposta)
          resposta = f"Dokkaebi: Comando '{comando}' recebido com sucesso!".encode('utf-8')
          conn.send(resposta)

  finally:
      print("Comando realizado!")
      conn.close()  # Vital para liberar o Agente e aceitar o próximo
      
      
# Só chega aqui se o loop quebrar
servidor.close()
print("[!] Servidor Dokkaebi desligado.")