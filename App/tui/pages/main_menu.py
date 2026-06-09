from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Rule, Static, Input, RichLog
from textual.containers import Horizontal, Vertical

import tui.classes.settings_config as SettingsConfig
from tui.components.menu import TerminalMenu

class Main_menu(Screen):
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
                "label": "Connect to Dokkaebi",
                "title": "ONLINE Dokkaebi",
                "description": (
                    "Enters online mode if configured. \n" +
                    "Provides a menu with all online capabilities"
                ),
                "options": "It only works in ONLINE mode",
                "action": "online_dokka",
            },
            {
                "label": "Local Tests",
                "title": "Local testing",
                "description": "Provides a menu with all offline actions.",
                "options": "",
                "action": "local_tests",
            },
            {
                "label": "Settings",
                "title": "Settings",
                "description": "Provides a menu with all configs for Dokkaebi.",
                "options": "",
                "action": "settings",
            },
            {
                "label": "Exit",
                "title": "Exit",
                "description": "Press ENTER to exit",
                "options": "This action will leave the application",
                "action": "exit",
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
                self.app.push_screen("online_dokka")
                pass

            case "local_tests":
                self.app.push_screen("local_tests")
                pass

            case "settings":
                self.app.push_screen("settings")
                pass

            case "return":
                self.app.pop_screen()

            case "exit":
                self.app.exit()