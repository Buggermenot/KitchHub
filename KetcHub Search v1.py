import random
from TextFormat import *
Veg_lst = list(map(lambda x: x.strip('\n'), open("Veg.txt", "r").readlines()))

def randNumber():
    count = 0
    break_flags = [True, False]
    weight = [10000, 1]
    while True:                         # Generates "Number" of ingredients
        count += 1
        cFlag = random.choices(break_flags, weight)[0]
        # print(cFlag, weight)
        if cFlag:
            weight[1] = 6*weight[1]
        else:
            break
    return count

class Recipe:
    ingredient_list = []
    UID = 0
    name = ''

    # Add more attributes ...


    def __init__(self, lst, uid):
        self.ingredient_list = lst
        self.UID = uid

        for ingredient in ingredient_list:
            self.name += ingredient[0]

    def __repr__(self):
        return self.name

Recipe_lst = dict()                             # All recipes
Recipe_lst_ingredient = dict()                  # All recipes sorted on ingredients
Recipe_lst_ingredient_count = dict()            # All recipes sorted on no. of ingredients
Recipe_UID = 221511

ingredient_count_dict = dict()

for _ in range(2000):
    ingredient_count: int = randNumber()        # Generates random "Number" of ingredients
    # print(ingredient_count)
    ingredient_list = random.choices(Veg_lst, k=ingredient_count)
    R = Recipe(ingredient_list, Recipe_UID)     # Recipe Object stored along with UID.
    Recipe_UID += 1


    Recipe_lst[Recipe_UID] = R                  # Recipe can be called using UID

    for ingredient in ingredient_list:          # Groups Recipes based on Ingredients
        try:
            Recipe_lst_ingredient[ingredient][Recipe_UID] = R
        except:
            Recipe_lst_ingredient[ingredient] = dict()
            Recipe_lst_ingredient[ingredient][Recipe_UID] = R

    try:
        Recipe_lst_ingredient_count[ingredient_count][Recipe_UID] = R
    except:
        Recipe_lst_ingredient_count[ingredient_count] = dict()
        Recipe_lst_ingredient_count[ingredient_count][Recipe_UID] = R

    try:
        ingredient_count_dict[ingredient_count] += 1
    except:
        ingredient_count_dict[ingredient_count] = 1


### All Dictionaries - Contains all Recipe details ##

# print(Underline(Bold("Recipe List")))
# print(Recipe_lst)

# print(Underline(Bold("Ingredient List")))
# for ingredient in sorted(Recipe_lst_ingredient):
#     print(Bold(ingredient + ":"), Recipe_lst_ingredient[ingredient])

# print(Underline(Bold("Ingredient Count List")))
# for count in sorted(Recipe_lst_ingredient_count):
#     print(Bold(str(count) + ":"), Recipe_lst_ingredient_count[count])
#
# print(Underline(Bold("Ingredient Count Distribution)))
# for key in sorted(ingredient_count_dict):
#     print(key, ingredient_count_dict[key])

# testIng = Recipe_lst[221517].ingredient_list              # Test Recipe
# print(testIng)

## - End Dictionaries - ##



## User Input ##
UserIngredientInput = []
print(Underline(Bold("User Inputs")))
while True:
    ingredient_index = int(input("Enter Ingredient Index, Refer to Veg.txt, -1 to finsh: "))
    if ingredient_index == -1:
        break
    Veg = Veg_lst[ingredient_index - 1]     # Calls selected ingredient
    print(Underline("Selected Veg:"), Veg)
    UserIngredientInput.append(Veg)
    print()

print(Underline("Final Selection:"), UserIngredientInput)

Recipes = set(Recipe_lst.keys())
print(Recipes)
for ingredient in UserIngredientInput:
    print(ingredient)
    Recipes = Recipes.intersection(set(Recipe_lst_ingredient[ingredient].keys()))
    print(Recipes)

print(Underline("Final Recipe Set:"), Recipes)
print(Underline("Total Recipes Available:"), len(Recipes))