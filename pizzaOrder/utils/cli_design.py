from pytermgui import tim


class CliDesign:
    def __init__(self):
        pass


class Colorizer:
    def __init__(self):
        pass

    def color_and_style(self, color: str = "white bold", text: str = ""):
        return tim.parse(f"[{color}]{text}")

