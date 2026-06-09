from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static

from tui.components.menu_header import MenuHeader
from tui.components.menu_options import MenuOptions
from tui.components.menu_description import MenuDescription


class TerminalMenu(Vertical):
    def __init__(
        self,
        title: str,
        items: list[dict[str, str]],
        selected_index: int = 0,
        branch: dict = None,
        history = [],
        id: str | None = None,
    ):
        super().__init__(id=id)
        self.branch = branch
        self.title_text = title
        self.items = items
        self.history = history
        self.selected_index = selected_index

    def compose(self) -> ComposeResult:
        yield MenuHeader(self.title_text)

        with Vertical():
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
            
            path = self.history + [self.branch]

            if len(path) >= 2 and path[-1]["id"] == path[-2]["id"]:
                path = path[:-1]

            yield Static("/".join([branch["id"] for branch in path]))
            
            
    def set_selected_index(self, index: int) -> None:
        self.selected_index = index

        self.query_one("#menu-options", MenuOptions).set_selected_index(index)
        self.query_one("#menu-description", MenuDescription).set_selected_index(index)