class ActionHandler:
    def __init__(self, screen):
        self.screen = screen

    def handle(self, node):
        action = node["action"]

        if action == "return":
            self.return_menu()

        elif action == "exit":
            self.screen.app.exit()

    def return_menu(self):
        if self.screen.history:
            self.screen.BRANCH = self.screen.history.pop()
            self.screen.selected_index = 0
            self.screen.reload_menu()