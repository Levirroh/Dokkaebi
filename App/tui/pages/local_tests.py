from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Rule, Static, Input, RichLog
from textual.containers import Horizontal, Vertical

import tui.classes.settings_config as SettingsConfig
from tui.components.menu import TerminalMenu

class Local_tests(Screen):
    BINDINGS = [
        ("up", "move_up", "Subir"),
        ("down", "move_down", "Descer"),
        ("enter", "select", "Selecionar"),
    ]
    
    def __init__(self):
        super().__init__()
        self.settings = SettingsConfig.get_config()
        self.selected_index = 0

        self.menu_items = [
            {
                "label": "Link Dokka",
                "title": "Connect a new device",
                "description": (
                    "Tries connection with a device in the same network"
                ),
                "options": "It only works in ONLINE mode",
                "action": "",
            },
            {
                "label": "Try endpoints",
                "title": "Endpoints",
                "description": "Opens a menu for endpoint testing.",
                "options": "",
                "action": "",
            },
            {
                "label": "Return",
                "title": "Return",
                "description": "Go back to the previous menu",
                "options": "Press ENTER to return",
                "action": "return",
            }
        ]
    
    def compose(self) -> ComposeResult:
        yield TerminalMenu(
            title=self.__class__.__name__,
            items=self.menu_items,
            selected_index=self.selected_index,
            id="terminal-menu",
        )
        
    def update_menu(self) -> None:
        menu = self.query_one("#terminal-menu", TerminalMenu)
        menu.set_selected_index(self.selected_index)

    def action_move_up(self) -> None:
        self.selected_index = (self.selected_index - 1) % len(self.menu_items)
        self.update_menu()

    def action_move_down(self) -> None:
        self.selected_index = (self.selected_index + 1) % len(self.menu_items)
        self.update_menu()

    def action_select(self) -> None:
        selected_item = self.menu_items[self.selected_index]

        match selected_item["action"]:
            case "online_dokka":
                pass

            case "local_tests":
                pass

            case "settings":
                pass

            case "return":
                self.app.pop_screen()