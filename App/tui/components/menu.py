from textual.widgets import Static

class TerminalMenu(Static):
    def __init__(self, options: list[str]):
        self.options = options
        super().__init__()

    def on_mount(self) -> None:
        lines = []

        for index, option in enumerate(self.options, start=1):
            lines.append(f"[{index}] - {option}")

        self.update("\n".join(lines))