from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Input, RichLog


class Environment_setup(Screen):
    def compose(self) -> ComposeResult:
        yield Static("DOKKAEBI::SETUP")
        yield Static("Mode: Terminal")
        yield Static("Initial setup required")

        yield RichLog(id="output")
        yield Input(placeholder="setup>")