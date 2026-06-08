from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Rule, Static, Input, RichLog
from textual.containers import Horizontal

from tui.components.menu import TerminalMenu

class Main_menu(Screen):
    def compose(self) -> ComposeResult:
        yield Static("DOKKAEBI::CLIENT")
        yield Static("Modo: Terminal")
        yield Static("Status: online", id="status")
    
        yield Static("───────────────────────────", classes="separator")
        
        yield TerminalMenu([
            "Connect to Dokkaebi",
            "Local Tests",
            "Settings",
            "Sair",
        ])
        
        yield Static("")
        
        with Horizontal(id="prompt-line"):
            yield Static("dokkaebi>", id="prompt")
            yield Input(id="command-input")

    def on_mount(self) -> None:
        self.query_one("#command-input", Input).focus()
        
    def on_input_submitted(self, event: Input.Submitted) -> None:
        command = event.value.strip()

        match command:
            case "2":
                self.app.push_screen("local_tests")
            case "3":
                self.app.push_screen("settings")
            case _:
                pass

        event.input.value = ""