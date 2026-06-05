import asyncio
import os
import socket
import psutil
from datetime import datetime

import api.helpers.terminal_helper as terminal_helper
import api.helpers.screen_helper as screen_helper


DEFAULT_WIDTH = 80

DOKKAEBI_LOGO = [
"██████╗  ██████╗ ██╗  ██╗██╗  ██╗ █████╗ ███████╗██████╗ ██╗",
"██╔══██╗██╔═══██╗██║ ██╔╝██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██║",
"██║  ██║██║   ██║█████╔╝ █████╔╝ ███████║█████╗  ██████╔╝██║",
"██║  ██║██║   ██║██╔═██╗ ██╔═██╗ ██╔══██║██╔══╝  ██╔══██╗██║",
"██████╔╝╚██████╔╝██║  ██╗██║  ██╗██║  ██║███████╗██████╔╝██║",
"╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝",
]



def get_terminal_width(max_width: int = DEFAULT_WIDTH) -> int:
    try:
        terminal_width = os.get_terminal_size().columns
        return min(terminal_width, max_width)
    except OSError:
        return max_width


def get_current_time() -> str:
    return datetime.now().strftime("%H:%M:%S")


def get_local_ip() -> str:
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "N/A"


def get_active_network_name() -> str:
   
    try:
        stats = psutil.net_if_stats()

        for interface_name, interface_stats in stats.items():
            if interface_stats.isup:
                return interface_name

        return "N/A"

    except Exception:
        return "N/A"


def top_border(width: int):
    print("╔" + ("═" * (width - 2)) + "╗")


def middle_border(width: int):
    print("╠" + ("═" * (width - 2)) + "╣")


def bottom_border(width: int):
    print("╚" + ("═" * (width - 2)) + "╝")


def empty_line(width: int):
    print("║" + (" " * (width - 2)) + "║")


def format_line(left_text: str = "", right_text: str = "", width: int = DEFAULT_WIDTH) -> str:
   
    inner_width = width - 2

    left_text = str(left_text)
    right_text = str(right_text)

    available_space = inner_width - len(left_text) - len(right_text)

    if available_space < 1:
        content = left_text[:inner_width]
        return "║" + content.ljust(inner_width) + "║"

    content = left_text + (" " * available_space) + right_text

    return "║" + content + "║"


def content_line(text: str = "", width: int = DEFAULT_WIDTH):
    inner_width = width - 4
    text = str(text)

    if len(text) > inner_width:
        text = text[:inner_width - 3] + "..."

    print(f"║ {text.ljust(inner_width)} ║")


def wrapped_content(text: str, width: int = DEFAULT_WIDTH):
    inner_width = width - 4
    text = str(text)

    if not text:
        content_line("", width)
        return

    words = text.split()
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= inner_width:
            if current_line:
                current_line += " "
            current_line += word
        else:
            content_line(current_line, width)
            current_line = word

    if current_line:
        content_line(current_line, width)


def render_header(width: int):
    current_time = get_current_time()
    local_ip = get_local_ip()
    network_name = get_active_network_name()

    right_info = [
        f"Horário: {current_time}",
        f"IP: {local_ip}",
        f"Rede: {network_name}",
    ]

    for index, logo_line in enumerate(DOKKAEBI_LOGO):
        right_text = right_info[index] if index < len(right_info) else ""
        print(format_line(logo_line, right_text, width))

def render_screen(
    title: str = "",
    lines: list[str] | None = None,
    width: int | None = None,
    clear: bool = True,
    show_input_area: bool = True
):
    if clear:
        screen_helper.clear_screen()

    if width is None:
        width = get_terminal_width()

    lines = lines or []

    top_border(width)
    render_header(width)
    middle_border(width)

    if title:
        content_line(title, width)
        middle_border(width)

    if lines:
        for line in lines:
            wrapped_content(line, width)
    else:
        empty_line(width)

    if show_input_area:
        middle_border(width)
    else:
        bottom_border(width)


def ask_inside_frame(prompt: str = "> ", width: int | None = None) -> str:
    
    if width is None:
        width = get_terminal_width()

    inner_width = width - 4
    prompt_text = f" {prompt}"

    print("║ " + prompt_text, end="")

    option = input().strip()

    bottom_border(width)

    return option


def pause(message: str = "Pressione Enter para continuar..."):
    width = get_terminal_width()

    middle_border(width)
    print("║ " + f" {message}", end="")
    input()
    bottom_border(width)


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


def message(
    title: str,
    text: str,
    width: int | None = None,
    clear: bool = True,
    wait: bool = True
):
   
    if width is None:
        width = get_terminal_width()

    render_screen(
        title=title,
        lines=[text],
        width=width,
        clear=clear,
        show_input_area=False
    )

    if wait:
        pause()


def success(text: str):
    message("Sucesso", text)


def error(text: str):
    message("Erro", text)


def info(text: str):
    message("Informação", text)


def form(
    title: str,
    fields: list[str],
    width: int | None = None,
    clear: bool = True
) -> dict[str, str]:
   
    if width is None:
        width = get_terminal_width()

    render_screen(
        title=title,
        lines=["Preencha os campos abaixo:"],
        width=width,
        clear=clear,
        show_input_area=False
    )

    values = {}

    for field in fields:
        middle_border(width)
        print("║ " + f"{field}: ", end="")
        values[field] = input().strip()

    bottom_border(width)

    return values

def main():
    terminal_helper.cor_terminal("0b")

    has_database_connection = screen_helper.handle_database_connection()

    if not has_database_connection:
        screen_helper.shutdown_terminal()
        exit(0)

    asyncio.run(menu())


if __name__ == "__main__":
    main()