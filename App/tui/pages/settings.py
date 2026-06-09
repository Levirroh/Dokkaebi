from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static
from textual.containers import Horizontal, Vertical

import tui.classes.settings_config as SettingsConfig
from tui.components.menu_header import MenuHeader


class Settings(Screen):
    BINDINGS = [
        ("up", "move_up", "Subir"),
        ("down", "move_down", "Descer"),
        ("right", "enter", "Entrar"),
        ("enter", "enter", "Entrar"),
        ("escape", "return", "Return"),
    ]

    def __init__(self):
        super().__init__()
        self.settings = SettingsConfig.get_config()

        self.settings_options = list(type(self.settings).model_fields.keys())
        self.settings_options.append("return")

        self.selected_index = 0

    def compose(self) -> ComposeResult:
        with Vertical(id="settings-screen-box"):
            yield MenuHeader(self.__class__.__name__)

            with Horizontal(classes="menu"):
                with Vertical(id="settings-menu"):
                    for index, option in enumerate(self.settings_options):
                        yield Static(
                            option.capitalize(),
                            id=f"settings-option-{index}",
                            classes="menu-option",
                        )

                with Vertical(id="settings-details"):
                    yield Static("", id="settings-details-title")
                    yield Static("", id="settings-details-desc")
                    yield Static("", id="settings-details-options")

    def on_mount(self) -> None:
        self.update_menu()
        self.update_details()

    def update_menu(self) -> None:
        for index, option in enumerate(self.settings_options):
            item = self.query_one(f"#settings-option-{index}", Static)
            label = option.capitalize()

            if index == self.selected_index:
                item.update(f"> {label}")
                item.add_class("selected")
            else:
                item.update(f"  {label}")
                item.remove_class("selected")

    def update_details(self) -> None:
        selected_option = self.settings_options[self.selected_index]

        title = self.query_one("#settings-details-title", Static)
        desc = self.query_one("#settings-details-desc", Static)
        options = self.query_one("#settings-details-options", Static)

        if selected_option == "return":
            title.update("Return")
            desc.update("Go back to the previous menu.")
            options.update("Press ENTER or ESCAPE to return.")
            return

        current_value = getattr(self.settings, selected_option, None)

        title.update(selected_option.capitalize())
        desc.update(f"Current value: {str(current_value).replace(' ', '\n')}")
        options.update("Press ENTER to edit this setting.")

    def action_move_up(self) -> None:
        self.selected_index = (self.selected_index - 1) % len(self.settings_options)
        self.update_menu()
        self.update_details()

    def action_move_down(self) -> None:
        self.selected_index = (self.selected_index + 1) % len(self.settings_options)
        self.update_menu()
        self.update_details()

    def action_return(self) -> None:
        self.app.pop_screen()

    def action_enter(self) -> None:
        selected_option = self.settings_options[self.selected_index]

        match selected_option:
            case "return":
                self.app.pop_screen()

            # case _:
                # Futuramente aqui você pode abrir uma tela/modal de edição.
                # self.notify(f"Editing {selected_option}")