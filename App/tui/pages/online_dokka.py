from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Rule, Static, Input, RichLog
from textual.containers import Horizontal, Vertical

import tui.classes.settings_config as SettingsConfig
from tui.components.menu import TerminalMenu

class Online_dokka(Screen):
    BINDINGS = [
        ("up", "move_up", "Subir"),
        ("down", "move_down", "Descer"),
        ("enter", "select", "Selecionar"),
    ]
    
    def __init__(self):
        super().__init__()
        self.settings = SettingsConfig.get_config()
        self.selected_index = 0
        self.options = [
            "Actions",
            "Dashboard",
            "Return"
        ]
        self.desc = [
            {
                "title": "Actions on online devices",
                "description": (
                    "In actions menu is possible to call\n"
                    "functions and endpoints in other devices"
                ),
                "options": "It only works in ONLINE mode."
            },
            {
                "title": "Dashboard",
                "description": "Shows a list of all online devices and their stats.",
                "options": "It only works in ONLINE mode."
            },
            {
                "title": "Return",
                "description": "Go back to the previous menu.",
                "options": "Press ENTER to return."
            }
        ]
        self.menu_items = [
                {
                    "label": "Actions",
                    "title": "Actions on online devices",
                    "description": (
                        "In actions menu is possible to call\n"
                        "functions and endpoints in other devices"
                    ),
                    "options": "It only works in ONLINE mode",
                    "action": "",
                },
                {
                    "label": "Dashboard",
                    "title": "Dashboard",
                    "description": "Shows a list of all online devices and their stats.",
                    "options": "It only works in ONLINE mode",
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
                self.app.push_screen("local_tests")
                pass

            case "settings":
                pass

            case "return":
                self.app.pop_screen()