from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

import tui.classes.settings_config as SettingsConfig


class MenuHeader(Static):
    def __init__(self, title: str, id: str | None = None):
        super().__init__(id=id)
        self.title_text = title
        self.settings = SettingsConfig.get_config()

    def compose(self) -> ComposeResult:
        yield Static(
            (
                f"DOKKAEBI::{self.title_text.replace('_', ' ').upper()} "
                f"| Mode: Terminal "
                f"| Status: {self.settings.connection.connection_type.value}"
            ),
            id="title",
        )