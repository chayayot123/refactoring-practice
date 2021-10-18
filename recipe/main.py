from recipe import Recipe

def make_recipe(name, chocolate=0, coffee=0, milk=0, sugar=0, price=0.0):
    recipe = Recipe(name)
    recipe.chocolate = chocolate
    recipe.coffee = coffee
    recipe.milk = milk
    recipe.sugar = sugar
    recipe.price = price

if __name__ == '__main__':
    recipe1 = make_recipe("Coffee with sugar", 4, 2, 1, 40.0)
    print(recipe1)

    recipe2 = make_recipe("Latte", 3, 2, 1, 40.0)
    print(recipe2)

    recipe3 = make_recipe("Hot Chocolate", 0, 3, 2, 4, 30.0)
    print(recipe3)