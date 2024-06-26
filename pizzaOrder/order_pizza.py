
from .utils import color_and_style

class Orderpizza:
    def __init__(
        self,
        pizza_size: dict[str, float],
        pizza_topping: dict[str, float],
        current_credit: float,
    ):
        self.pizza_size = pizza_size
        self.pizza_topping = pizza_topping
        self.current_credit = current_credit
        self.total = 0

    def select_pizza_size(self, pizza_size_name: str):
        try:
            pizza_size_cost = self.pizza_size[pizza_size_name]
            self.total += pizza_size_cost
            self.current_credit -= pizza_size_cost
            return color_and_style(
                "cyan bold dim",
                f"\n\tYou have selected {pizza_size_name} (${pizza_size_cost}) [current : ${self.current_credit}]",
            )
        except KeyError as ke:
            return color_and_style("red bold", "\n\tError : Invalid pizza name\n")

    def select_pizza_topping(self, pizza_topping_name: str):
        try:
            pizza_topping_cost = self.pizza_topping[pizza_topping_name]
            self.total += pizza_topping_cost
            self.current_credit -= pizza_topping_cost
            return color_and_style(
                "cyan bold dim",
                f"\n\tYou have selected {pizza_topping_name} (${pizza_topping_cost}) [current : ${self.current_credit}]",
            )
        except KeyError as ke:
            return color_and_style("red bold", "\n\tError : Invalid pizza topping name\n")

    def calculate_pizza_total(self):
        return color_and_style("cyan bold", f"\n\tOverall price : {self.total}")
