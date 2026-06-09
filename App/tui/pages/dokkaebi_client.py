from textual.app import App, ComposeResult

from tui.pages.online_dokka import Online_dokka
from tui.pages.settings import Settings
from tui.pages.local_tests import Local_tests
from tui.pages.main_menu import Main_menu
from tui.pages.setup import Environment_setup


class Dokkaebi_client(App):
    CSS_PATH = "../styles/style.tcss"

    SCREENS = {
        "main_menu": Main_menu,
        "online_dokka": Online_dokka,
        "setup": Environment_setup,
        "local_tests": Local_tests,
        "settings": Settings,
    }

    def on_mount(self) -> None:
        is_configured = True

        if is_configured:
            self.push_screen("main_menu")
        else:
            self.push_screen("setup")