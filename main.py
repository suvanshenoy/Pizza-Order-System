# date : 20th jan 2022
# file_name : main.py

from pizzaOrder import order_pizza, add_credits,color_and_style



def iterate_pizza_keys(pizza_dict: dict[str, float], pizza_dict_name: str):
    str_pizza_keys = ""
    print(
        color_and_style("bold cyan underline", f"\tAvailable {pizza_dict_name} :\n")
    )
    for pizza_key, pizza_key_value in pizza_dict.items():
        str_pizza_keys += color_and_style(
            "bold cyan", f"\t{pizza_key} [${(pizza_key_value)}]\n"
        )
    return str_pizza_keys


pizza_size, pizza_topping = {"small": 5.0, "medium": 8.50, "large": 10.25}, {
    "ham": 0.80,
    "mushrooms": 0.50,
    "pepperoni": 1.0,
    "peppers": 0.80,
    "onions": 0.40,
    "extra cheese": 1.50,
}

ac = add_credits.AddCredits()
op = order_pizza.Orderpizza(pizza_size, pizza_topping, ac.add(100))

selected_pizza_size, selected_pizza_topping = input(
    "{}\n\t=>".format(iterate_pizza_keys(pizza_size, "pizza size".upper()))
), input("{}\n\t=>".format(iterate_pizza_keys(pizza_topping, "pizza topping".upper())))


print(
    op.select_pizza_size(selected_pizza_size),
    op.select_pizza_topping(selected_pizza_topping),
    op.calculate_pizza_total(),
)

print(
    color_and_style("white bold underline", "\nRecent orders:\n".upper()),
    color_and_style("white bold", f"\n\tpizza size : {selected_pizza_size}"),
    color_and_style("white bold", f"\n\tpizza topping : {selected_pizza_topping}"),
)
