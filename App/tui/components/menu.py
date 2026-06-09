from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical

from tui.components.menu_header import MenuHeader
from tui.components.menu_options import MenuOptions
from tui.components.menu_description import MenuDescription


class TerminalMenu(Vertical):
    def __init__(
        self,
        title: str,
        items: list[dict[str, str]],
        selected_index: int = 0,
        id: str | None = None,
    ):
        super().__init__(id=id)
        self.title_text = title
        self.items = items
        self.selected_index = selected_index

    def compose(self) -> ComposeResult:
        yield MenuHeader(self.title_text)

        with Horizontal(classes="menu"):
            yield MenuOptions(
                items=self.items,
                selected_index=self.selected_index,
                id="menu-options",
            )

            yield MenuDescription(
                items=self.items,
                selected_index=self.selected_index,
                id="menu-description",
            )

    def set_selected_index(self, index: int) -> None:
        self.selected_index = index

        self.query_one("#menu-options", MenuOptions).set_selected_index(index)
        self.query_one("#menu-description", MenuDescription).set_selected_index(index)