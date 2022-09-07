raw = open("ifd.txt", "r").read()
raw_lists = (raw).lower().replace("\n", " @>").split(">")

# print(raw_lists)

noNumsSpecs = ""

for i in raw_lists:
    for char in i:
        if char.isdigit() | (char in ["/", "&", "-", ".", "'", '"']):
            continue
        else:
            noNumsSpecs += char

# print(noNumsSpecs)

badWords = ["to", "for", "or", "with", "into", "a", "like", "taste", "per", "time", "hours", "minutes", "cooked", "chopped", "roughly", "cups", "tablespoon", "tablespoons", "teaspoons", "teaspoon", "tbsp", "tsp", "pinch", "cup",
            "required", "as", "grated", "boiled", "kg", "kgs", "inch", "vegans", "can", "eliminate", "this", "ingredient", "thinly", "sliced", "atste", "medium", "pieces", "homemade", "finely", "crumbled",
            "small", "diagonally", "ml", "grams", "slit", "and", "picked", "liter", "dressing", "recipe", "minced", "of", "use", "needed", "deep", "fry", "frying", "adjust", "warm+more", "few", "sprig", "halved", "skin", "peel", "tighten", "grind",
            "little", "breads�or", "foot", "cut", "wash", "well", "in", "water", "inches", "chop", "soaked", "tightly", "packed", "cooking", "torn", "overnight", "more", "big", "spoon", "pressure"]

listed_noNumsSpecs = list(noNumsSpecs.split(","))

noNumsSpecsBadwords = ""

for i in listed_noNumsSpecs:
    listOfWords = list(i.split(" "))
    finna = []
    for word in listOfWords:
        if word:
            if (word in badWords) | (word[0] == "(") | (word[-1] == ")"):
                #print("&&&&"+word)
                continue
            else:
                # print(word)
                finna.append(word)

    for f in finna:
        noNumsSpecsBadwords += f + " "
    noNumsSpecsBadwords += ", "
noNumsSpecsBadwordsLIST = noNumsSpecsBadwords.strip().split(",")
###

# ultraList = []
# for i in (noNumsSpecsBadwordsLIST):
#     recipe = []

# print(noNumsSpecsBadwordsLIST)


FinalVegLST = []
for veg in noNumsSpecsBadwordsLIST:
    if veg.strip():
        FinalVegLST.append(veg.strip())

recipe_seg = (", ".join(FinalVegLST)).split("@")[0:-1]
for i in range(len(recipe_seg)):
    recipe_seg[i] = recipe_seg[i].strip().split(', ')
#
# print(recipe_seg)
#
writee = open("Filtered.txt", "w")
for string in recipe_seg:
    writee.writelines(str(string) + "\n")
#

ingredient_dict = dict()
for i in recipe_seg:
   for j in i:
        try:
            ingredient_dict[j.strip()] = ingredient_dict[j.strip()] + 1
        except:
            ingredient_dict[j.strip()] = 1

ingredient_dict = dict(sorted(ingredient_dict.items(), key=lambda item: item[1], reverse=True))
for keys in ingredient_dict.keys():
    print(keys + ":", ingredient_dict[keys])
