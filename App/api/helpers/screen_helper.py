import asyncio
import os

from client import ask_inside_frame, get_terminal_width, render_screen
import database.session as session
import database.setup as setup

import api.endpoints.auth_ep as auth
import api.endpoints.brain_ep as brain
import api.endpoints.master_ep as master
import api.endpoints.system_ep as system

import api.helpers.terminal_helper as terminal_helper
import api.helpers.screen_helper as screen


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    

def menu(
    title: str,
    options: dict[str, str],
    width: int | None = None,
    clear: bool = True
) -> str:
    if width is None:
        width = get_terminal_width()

    lines = []

    for key, value in options.items():
        lines.append(f"{key} - {value}")

    render_screen(
        title=title,
        lines=lines,
        width=width,
        clear=clear,
        show_input_area=True
    )

    return ask_inside_frame(width=width)
  
  

async def agent_menu():
    options = {
        "0": "Voltar"
    }

    while True:
        option = screen.menu("Agents Menu", options)

        if option == "0":
            break

        screen.error("Opção inválida.")


async def auth_menu():
    options = {
        "1": "Login",
        "0": "Voltar"
    }

    while True:
        option = screen.menu("Auth Menu", options)

        if option == "1":
            await login_flow()

        elif option == "0":
            break

        else:
            screen.error("Opção inválida.")


async def login_flow():
    data = screen.form("Login", ["Username", "Password"])

    username = data["Username"]
    password = data["Password"]

    try:
        req = auth.Login(
            username=username,
            password=password
        )

        res = await auth.login(req, session)

        screen.message(
            title="Resultado do Login",
            text=str(res)
        )

    except Exception as e:
        screen.error(str(e))

    finally:
        close_database_session()


async def brain_menu():
    options = {
        "1": "Logs",
        "2": "Notifications",
        "0": "Voltar"
    }

    while True:
        option = screen.menu("Brain Menu", options)

        if option == "1":
            await show_endpoint_result("Brain Logs", brain.logs)

        elif option == "2":
            await show_endpoint_result("Brain Notifications", brain.notifications)

        elif option == "0":
            break

        else:
            screen.error("Opção inválida.")


async def master_menu():
    options = {
        "1": "Dashboard",
        "0": "Voltar"
    }

    while True:
        option = screen.menu("Master Menu", options)

        if option == "1":
            await show_endpoint_result("Master Dashboard", master.dashboard)

        elif option == "0":
            break

        else:
            screen.error("Opção inválida.")


async def system_menu():
    options = {
        "0": "Voltar"
    }

    while True:
        option = screen.menu("System Menu", options)

        if option == "0":
            break

        screen.error("Opção inválida.")


async def show_endpoint_result(title: str, endpoint_function):
    try:
        res = await endpoint_function()

        screen.message(
            title=title,
            text=str(res)
        )

    except Exception as e:
        screen.error(str(e))


def select_database_connection() -> bool:
    options = {
        "1": "Conexão Local automática",
        "2": "Conexão Local usando SQLite",
        "3": "Conexão Remota",
        "0": "Sair"
    }

    while True:
        option = screen.menu("Configuração do Banco de Dados", options)

        if option == "1":
            return configure_local_database()

        elif option == "2":
            return configure_sqlite_database()

        elif option == "3":
            return configure_remote_database()

        elif option == "0":
            return False

        else:
            screen.error("Opção inválida.")


def configure_local_database() -> bool:
    try:
        setup.get_databases()

        screen.success("Verificação de bancos locais finalizada.")
        return True

    except Exception as e:
        screen.error(f"Falha ao conectar no banco local: {e}")
        return False


def configure_sqlite_database() -> bool:
    try:
        if hasattr(setup, "setup_sqlite"):
            setup.setup_sqlite()

        elif hasattr(setup, "create_sqlite_database"):
            setup.create_sqlite_database()

        else:
            screen.info("Nenhuma função de configuração SQLite foi encontrada em database.setup.")
            return False

        screen.success("Banco SQLite configurado com sucesso.")
        return True

    except Exception as e:
        screen.error(f"Falha ao configurar SQLite: {e}")
        return False


def configure_remote_database() -> bool:
    try:
        if hasattr(setup, "setup_remote_database"):
            setup.setup_remote_database()

        else:
            screen.info("Nenhuma função de configuração remota foi encontrada em database.setup.")
            return False

        screen.success("Banco remoto configurado com sucesso.")
        return True

    except Exception as e:
        screen.error(f"Falha ao conectar no banco remoto: {e}")
        return False


def close_database_session():
    try:
        if hasattr(session, "close"):
            session.close()
    except Exception:
        pass


def handle_database_connection() -> bool:
    connected = session.test_connection()

    if connected:
        return True

    while True:
        option = screen.menu(
            title="Banco de Dados não encontrado",
            options={
                "1": "Criar nova conexão",
                "0": "Sair"
            }
        )

        if option == "1":
            return select_database_connection()

        elif option == "0":
            return False

        else:
            screen.error("Opção inválida.")


def shutdown_terminal():
    screen.clear_screen()
    print("Adeus.")
    terminal_helper.cor_terminal("04")


if __name__ == "__main__":
    terminal_helper.cor_terminal("0b")

    has_database_connection = handle_database_connection()

    if not has_database_connection:
        shutdown_terminal()
        exit(0)

    asyncio.run(menu())
    
    
    