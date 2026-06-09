from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Vertical


class MenuDescription(Vertical):
    def __init__(
        self,
        items: list[dict[str, str]],
        selected_index: int = 0,
        id: str | None = None,
    ):
        super().__init__(id=id)
        self.items = items
        self.selected_index = selected_index

    def compose(self) -> ComposeResult:
        yield Static("", id="settings-details-title")
        yield Static("", id="settings-details-desc")
        yield Static("", id="settings-details-requires")
        yield Static("", id="settings-details-warnings")

    def on_mount(self) -> None:
        self.update_description()

    def set_selected_index(self, index: int) -> None:
        self.selected_index = index
        self.update_description()

    def update_description(self) -> None:
        selected_item = self.items[self.selected_index]

        self.query_one("#settings-details-title", Static).update(
            selected_item["title"]
        )

        self.query_one("#settings-details-desc", Static).update(
            selected_item["description"]
        )

        requires = selected_item.get("requires", [])

        self.query_one("#settings-details-requires", Static).update(
            ("Requires: " + ", ".join(requires).capitalize().replace("_"," ") if requires else "")
        )
        
        warnings = selected_item.get("warnings", [])

        self.query_one("#settings-details-warnings", Static).update(
            ("WARNING: " + "\n".join(warnings).capitalize().replace("_"," ") if warnings else "")
        )