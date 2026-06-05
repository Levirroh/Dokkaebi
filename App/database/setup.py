import psutil
from sqlalchemy import create_engine, text


COMMON_MYSQL_PORTS = [3306, 3307, 3308]
COMMON_USERS = ["root"]
COMMON_PASSWORDS = ["root", "", "admin", "123456"]

#Arquivo para configurar o banco de dados
# Deve ser possível identificar os bancos que o usuário possui e criar um modelo local para testes caso seja Local a conexão
# Deve conseguir se conectar a um banco remoto caso seja essa a opção do usuário

def get_databases():
  databases = []
  
  for p in psutil.process_iter(['name']):
    print("Nome:" + p.info['name'] + " - Certo? " + str("ssms" in p.info['name']))
    if p.info['name'] == "mysqld" or p.info['name'] == "postgres"or p.info['name'] == "ssms":
      databases.append(p)
      
  print(databases)
  return databases


# def setup_sqlite():