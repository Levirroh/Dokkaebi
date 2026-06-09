from textual.app import App, ComposeResult

from tui.pages.settings import Settings
from tui.pages.main_menu import Main_menu
from tui.pages.setup import Environment_setup


class Dokkaebi_client(App):
    CSS_PATH = "../styles/style.tcss"

    SCREENS = {
        "main_menu": Main_menu,
        "setup": Environment_setup,
        "settings": Settings,
    }

    def on_mount(self) -> None:
        is_configured = True

        if is_configured:
            self.push_screen("main_menu")
        else:
            self.push_screen("setup")