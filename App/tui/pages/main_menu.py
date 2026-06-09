from textual.app import ComposeResult
from textual.screen import Screen

from tui.navigation.action_handler import ActionHandler
from tui.navigation.menu_tree.menu_tree import MAIN_TREE, RETURN_NODE
import tui.classes.settings_config as SettingsConfig
from tui.components.menu import TerminalMenu


class Main_menu(Screen):
    BINDINGS = [
        ("up", "move_up", "Up"),
        ("down", "move_down", "Down"),
        ("enter", "select", "Select"),
        ("escape", "return", "Return"),
    ]

    def __init__(self):
        super().__init__()
        self.settings = SettingsConfig.get_config()

        self.selected_index = 0

        self.history = []
        self.action_handler = ActionHandler(self)        
        
        self.TREE = MAIN_TREE
        self.BRANCH = self.TREE
        self.tree_children = self.BRANCH["children"]

    def compose(self) -> ComposeResult:
        yield TerminalMenu(
            title=self.BRANCH["title"],
            items=self.tree_children,
            selected_index=self.selected_index,
            id="terminal-menu",
        )

    def update_menu_selection(self) -> None:
        menu = self.query_one("#terminal-menu", TerminalMenu)
        menu.set_selected_index(self.selected_index)

    def reload_menu(self) -> None:
        menu = self.query_one("#terminal-menu", TerminalMenu)

        if self.BRANCH["id"] != "main":
            self.tree_children = self.BRANCH["children"] + [RETURN_NODE]
        else:
            self.tree_children = self.BRANCH["children"]

        menu.title = self.BRANCH["title"]
        menu.items = self.tree_children

        menu.set_selected_index(self.selected_index)
        menu.refresh(recompose=True)

    def action_move_up(self) -> None:
        self.selected_index = (self.selected_index - 1) % len(self.tree_children)
        self.update_menu_selection()

    def action_move_down(self) -> None:
        self.selected_index = (self.selected_index + 1) % len(self.tree_children)
        self.update_menu_selection()
        
    def action_return(self) -> None:
        if self.BRANCH["id"] != "main":
            if self.history:
                self.BRANCH = self.history.pop()
                self.selected_index = 0
                self.reload_menu()        
            else:
                self.app.pop_screen()
        else:
            self.app.exit()

    def action_select(self) -> None:
        selected_item = self.tree_children[self.selected_index]
        selected_type = selected_item["type"]

        if selected_type == "folder":
            self.history.append(self.BRANCH)
            self.BRANCH = selected_item
            self.tree_children = self.BRANCH["children"]
            self.selected_index = 0
            self.reload_menu()

        elif selected_type == "screen":
            self.app.push_screen(selected_item["screen"])

        elif selected_type == "action":
            self.action_handler.handle(selected_item)       
                    