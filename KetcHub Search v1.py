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
    ingredient_count = 0
    # Add more attributes ...


    def __init__(self, lst, uid):
        self.ingredient_list = lst
        self.UID = uid
        self.ingredient_count = count

        for ingredient in ingredient_list:
            self.name += ingredient[0]

    def __repr__(self):
        return self.name

Recipe_lst = dict()                                             # All recipes
Recipe_lst_ingredient = dict()                                  # All recipes sorted on ingredients
Recipe_lst_ingredient_count = dict()                            # All recipes sorted on no. of ingredients
Recipe_UID = 221511

ingredient_count_dict = dict()

for _ in range(20000):
    ingredient_count = randNumber()                             # Generates random "Number" of ingredients
    # print(ingredient_count)
    ingredient_list = random.sample(Veg_lst, k=ingredient_count)
    R = Recipe(ingredient_list, Recipe_UID, ingredient_count)   # Recipe Object stored along with UID.
    Recipe_UID += 1


    Recipe_lst[Recipe_UID] = R                                  # Recipe can be called using UID

    for ingredient in ingredient_list:                          # Groups Recipes based on Ingredients
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
# print(Underline(Bold("Ingredient Count Distribution")))
# for key in sorted(ingredient_count_dict):
#     print(key, ingredient_count_dict[key])
#
# testIng = Recipe_lst[221517].ingredient_list                  # Test Recipe
# print(testIng)

## - End Dictionaries - ##


## User Input ##
UserIngredientInput = []
print(Underline(Bold("User Inputs")))
while True:
    ingredient_index = int(input("Enter Ingredient Index, Refer to Veg.txt, -1 to finsh: "))
    if ingredient_index == -1:
        break
    try:
        Veg = Veg_lst[ingredient_index - 1]                     # Calls selected ingredient
    except:
        break
    print(Underline("Selected Veg:"), Veg)
    UserIngredientInput.append(Veg)
    print()
UserIngredientInput = list(set(UserIngredientInput))
print(Underline("Final Selection:"), UserIngredientInput)       # Final list of ingredients

## Test 1: Recipes that use any user ingredients atleast once
# Recipes = set(Recipe_lst.keys())
# print(Recipes)
# for ingredient in UserIngredientInput:
#     print(ingredient)
#     Recipes = Recipes.intersection(set(Recipe_lst_ingredient[ingredient].keys()))
#     print(Recipes)


## Test 2:
# Recipe_set = set()
# for ingredient in UserIngredientInput:
#     Recipe_set = Recipe_set.intersection(set(Recipe_lst_ingredient[ingredient].keys()))
#
# ingredient_count_set = set()
# for count in range (1, len(UserIngredientInput) + 1):
#     try:
#         ingredient_count_set = ingredient_count_set.union(set(Recipe_lst_ingredient_count[count].keys()))
#     except:
#         pass
# Recipes = Recipe_set.intersection(ingredient_count_set)

# --------------------------- #
## Test 3:              ->> WORKS AS REQUIRED!!
Recipes = set()

## Recipe Return Algo ##
for ingredient in UserIngredientInput:                          # Union of Recipes with any of User inputs
    Recipes = Recipes.union(set(Recipe_lst_ingredient[ingredient].keys()))

for ingredient in Recipe_lst_ingredient:                        # Remove undesired ingredients
    if ingredient not in UserIngredientInput:
        Recipes.difference_update(set(Recipe_lst_ingredient[ingredient].keys()))
# -End of Recipe Return Algo- #

## Auxiliary Stuff
Recipe_dict = dict()
for recipe in Recipes:
    try:
        Recipe_dict[Recipe_lst[recipe].ingredient_count].append(recipe)
    except:
        Recipe_dict[Recipe_lst[recipe].ingredient_count] = [recipe]

# All print returns
print(Underline("Final Recipe Set:"))
for count in sorted(Recipe_dict.keys(), reverse=True):
    print(Bold(str(count) + ":"), Recipe_dict[count])

print(Underline("Total Recipes Available:"), len(Recipes))


# [DEBUGGING] Call and check any recipe [DEBUGGING] #
while True:
    chk_recipe = int(input(Bold("Enter Recipe ID to check: ")))
    try:
        print("Recipe Name:", Recipe_lst[chk_recipe])
        print("Ingredients:", Recipe_lst[chk_recipe].ingredient_list)
    except:
        print("Recipe Does not exist")
# # # -END CODE- # # #