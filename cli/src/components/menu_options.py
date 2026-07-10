from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Vertical


class MenuOptions(Vertical):
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
        for index, item in enumerate(self.items):
            yield Static(
                item["label"],
                id=f"settings-option-{index}",
                classes="menu-option",
            )

    def on_mount(self) -> None:
        self.update_options()

    def set_selected_index(self, index: int) -> None:
        self.selected_index = index
        self.update_options()

    def update_options(self) -> None:
        for index, item_data in enumerate(self.items):
            option_widget = self.query_one(f"#settings-option-{index}", Static)
            label = item_data["label"]

            if index == self.selected_index:
                option_widget.update(f"> {label}")
                option_widget.add_class("selected")
            else:
                option_widget.update(f"  {label}")
                option_widget.remove_class("selected")
                