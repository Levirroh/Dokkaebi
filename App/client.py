import asyncio
import os

# https://www.asciiart.eu/text-to-ascii-art#google_vignette

import database.session as session
import database.setup as setup
import api.endpoints.auth_ep as auth
import api.helpers.terminal_helper as terminal_helper
import api.endpoints.brain_ep as brain
import api.endpoints.master_ep as master
import api.endpoints.system_ep as system
import main as main


async def menu():
    while True:
        print("\n=== Dokkaebi Terminal Client ===")
        print("1 - Agents")
        print("2 - Auth")
        print("3 - Brain")
        print("4 - Master")
        print("5 - System")
        print("0 - Sair")

        option = input("> ")

        if option == "1":
            await agent_menu()
        elif option == "2":
            await auth_menu()
        elif option == "3":
            await brain_menu()
        elif option == "4":
            await master_menu()
        elif option == "5":
            await system_menu()
        elif option == "0":
            break
        else:
            print("Opção inválida.")


async def agent_menu():
    while True:
        print("\n=== Agents Menu ===")
        print("0 - Voltar")

        option = input("> ")

        if option == "0":
            break
        else:
            print("Opção inválida.")


async def auth_menu():
    while True:
        print("\n=== Auth Menu ===")
        print("1 - Login")
        print("0 - Voltar")

        option = input("> ")

        if option == "1":
          username = input("Username: ")
          password = input("Password: ")

          try:
              req = auth.Login(
                  username=username,
                  password=password
              )

              res = await auth.login(req, session)

              print(res)

          except Exception as e:
              print("Erro:", e)

          finally:
              session.close()

          input("Pressione Enter para continuar...")
        elif option == "0":
            break
        else:
            print("Opção inválida.")


async def brain_menu():
    while True:
        print("\n=== Brain Menu ===")
        print("1 - Logs")
        print("2 - Notifications")
        print("0 - Voltar")

        option = input("> ")

        if option == "1":
            res = await brain.logs()
            print(res)
            input("Pressione Enter para continuar...")

        elif option == "2":
            res = await brain.notifications()
            print(res)
            input("Pressione Enter para continuar...")

        elif option == "0":
            break
        else:
            print("Opção inválida.")


async def master_menu():
    while True:
        print("\n=== Master Menu ===")
        print("1 - Dashboard")
        print("0 - Voltar")

        option = input("> ")

        if option == "1":
            res = await master.dashboard()
            print(res)
            input("Pressione Enter para continuar...")

        elif option == "0":
            break
        else:
            print("Opção inválida.")


async def system_menu():
    while True:
        print("\n=== System Menu ===")
        print("0 - Voltar")

        option = input("> ")

        if option == "0":
            break
        else:
            print("Opção inválida.")


def select_database_connection():
    while True:
        print("\nEscolha a conexão do banco:")
        print("1 - Conexão Local automática")
        print("2 - Conexão Local usando SQLite")
        print("3 - Conexão Remota")
        print("0 - Sair")

        option = input("> ")

        if option == "1":
          setup.get_databases()
          print("Falha ao conectar no banco local.")
        if option == "2":
          setup.get_databases()
          print("Falha ao conectar no banco local.")
        elif option == "2":
          print("Falha ao conectar no banco remoto.")
        elif option == "0":
          return False

        else:
            print("Opção inválida.")


if __name__ == "__main__":
  terminal_helper.limpar_terminal()
  terminal_helper.cor_terminal('0b')
  
  connected = session.test_connection()
  
  print("""
██████╗  ██████╗ ██╗  ██╗██╗  ██╗ █████╗ ███████╗██████╗ ██╗
██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██║
██║  ██║██║   ██║█████╔╝ █████╔╝ ███████║█████╗  ██████╔╝██║
██║  ██║██║   ██║██╔═██╗ ██╔═██╗ ██╔══██║██╔══╝  ██╔══██╗██║
██████╔╝╚██████╔╝██║  ██╗██║  ██╗██║  ██║███████╗██████╔╝██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝
        """)
  print("Bem-vindo ao terminal para testes Dokkaebi.")
  
  if(not connected):
    print("Não foi encontrado uma conexão com o banco de dados")
    print("Deseja criar uma nova conexão?")
    
    while True:
      print("1 - Sim")
      print("0 - Sair")

      option = input("> ")

      if option == "1":
        select_database_connection()
      elif option == "0":
        terminal_helper.limpar_terminal()
        print("Adeus.")
        terminal_helper.cor_terminal("04")
        exit(0)
      else:
        print("Opção inválida.")
  
  asyncio.run(menu())
