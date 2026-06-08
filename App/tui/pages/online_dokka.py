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
    
    def compose(self) -> ComposeResult:
        with Vertical(id="header-box"):
            yield Static(f"DOKKAEBI::{self.__class__.__name__.replace('_', ' ').upper()} | Mode: Terminal | Status: {self.settings.connection.connection_type.value}", id="title")

            with Horizontal(classes="menu"):
                with Vertical(id="settings-menu"):
                    for index, option in enumerate(self.options):
                        yield Static(
                            option,
                            id=f"settings-option-{index}",
                            classes="menu-option"
                        )

                yield Static("detalhes", id="settings-details")
    
    def update_menu(self) -> None:
        for index, option in enumerate(self.options):
            item = self.query_one(f"#settings-option-{index}", Static)

            if index == self.selected_index:
                item.update(f"> {option}")
                item.add_class("selected")
            else:
                item.update(f"  {option}")
                item.remove_class("selected")
                
    def on_mount(self) -> None:
        self.update_menu()
        
    def action_move_up(self) -> None:
        self.selected_index = (self.selected_index - 1) % len(self.options)
        self.update_menu()

    def action_move_down(self) -> None:
        self.selected_index = (self.selected_index + 1) % len(self.options)
        self.update_menu()

    def action_select(self) -> None:
        selected = self.options[self.selected_index]

        match selected:
            case "Return":
                self.app.pop_screen()