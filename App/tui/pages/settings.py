from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Rule, Static, Input, RichLog
from textual.containers import Horizontal, Vertical

import tui.classes.settings_config as SettingsConfig
from tui.components.menu import TerminalMenu

class Settings(Screen):
    CSS_PATH="../styles/settings.tcss"
    BINDINGS = [
        ("up", "move_up", "Subir"),
        ("down", "move_down", "Descer"),
        ("right", "move_left", "Entrar"),
        ("enter", "enter", "Entrar"),
        ("escape", "return", "Return"),
    ]
    
    def __init__(self):
        super().__init__()
        self.settings = SettingsConfig.get_config()
        self.settings_options = list(type(self.settings).model_fields.keys())
        self.settings_options.append("return")
        self.selected_index = 0
    
    def _on_mount(self, event):
        self.update_menu()
    
    def compose(self) -> ComposeResult:
        with Vertical(id="settings-box"):
            yield Static(f"DOKKAEBI::{self.__class__.__name__.replace("_", " ").upper()} | Mode: Terminal | Status: {self.settings.connection.connection_type.value}", id="title")

            with Horizontal(classes="menu", id="settings-content"):
                with Vertical(id="settings-menu"):
                    for index, option in enumerate(self.settings_options):
                        yield Static(
                            option.capitalize(),
                            id=f"settings-option-{index}",
                            classes="menu-option"
                        )

                yield Static("detalhes", id="settings-details")
    
    def update_menu(self) -> None:
        for index, option in enumerate(self.settings_options):
            item = self.query_one(f"#settings-option-{index}", Static)

            if index == self.selected_index:
                item.update(f"> {option.capitalize()}")
                item.add_class("selected")
            else:
                item.update(f"  {option.capitalize()}")
                item.remove_class("selected")
        
                    
    def action_move_up(self) -> None:
        self.selected_index -= 1

        if self.selected_index < 0:
            self.selected_index = len(self.settings_options) - 1

        self.update_menu()
        # self.update_details()


    def action_move_down(self) -> None:
        self.selected_index += 1

        if self.selected_index >= len(self.settings_options):
            self.selected_index = 0

        self.update_menu()
        # self.update_details()
        
    def action_return(self) -> None:
        self.app.pop_screen()
    
    def action_enter(self) -> None:
        print("asdkasd")