from time import strftime


class Logs:
    def __init__(self, name: str):
        self.name = name

        self.RED = "\033[91m"
        self.GREEN = "\033[92m"
        self.BLUE = "\033[96m"
        self.YELLOW = "\033[93m"
        self.PURPLE = "\033[95m"
        self.BOLD = "\033[1m"
        self.UNDERLINE = "\033[4m"
        self.DISABLE = "\033[0m"

    def send_error(self, text: str) -> None:
        print(f"{self.BOLD + self.RED + self.name + self.DISABLE} » {text} | {self.BOLD + strftime('%H:%M:%S')}")

    def send_warning(self, text: str) -> None:
        print(f"{self.BOLD + self.YELLOW + self.name + self.DISABLE} » {text} | {self.BOLD + strftime('%H:%M:%S')}")

    def send_info(self, text: str) -> None:
        print(f"{self.BOLD + self.GREEN + self.name + self.DISABLE} » {text} | {self.BOLD + strftime('%H:%M:%S')}")

    def send_custom(self, text: str, color) -> None:
        print(f"{self.BOLD + color + self.name + self.DISABLE} » {text} | {self.BOLD + strftime('%H:%M:%S')}")
