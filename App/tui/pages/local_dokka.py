from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Rule, Static, Input, RichLog
from textual.containers import Horizontal

from tui.components.menu import TerminalMenu

class Local_dokka(Screen):
    def compose(self) -> ComposeResult:
        yield Static("DOKKAEBI::ONLINE DOKKA")
        yield Static("Mode: client | Online")
        yield Static("Status: online", id="status")
    
        yield Static("───────────────────────────", classes="separator")
        
        yield Static("")
        
        with Horizontal(id="prompt-line"):
            yield Static("dokkaebi>", id="prompt")
            yield Input(id="command-input")
    
    def on_mount(self) -> None:
        self.query_one("#command-input", Input).focus()