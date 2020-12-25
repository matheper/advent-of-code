"""
--- Day 21: Allergen Assessment ---


You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?


--- Part Two ---
Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.

In the above example:

mxmxvkd contains dairy.
sqjhc contains fish.
fvjkl contains soy.
Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?


https://adventofcode.com/2020/day/21
"""

class Menu:
    def __init__(self, menu_items):
        self.items = list()
        self.ingredients = set()
        self.allergens = set()
        self._parse_items(menu_items)

    def _parse_items(self, menu_items):
        items = list()
        for item in menu_items:
            ingredients, allergens = item.split(' (')
            allergens = allergens.replace('contains ', '')[:-1]
            ingredients = {i for i in ingredients.split(' ')}
            allergens = {a for a in allergens.split(', ')}
            self.items.append({
                'ingredients': ingredients,
                'allergens': allergens,
            })
            self.ingredients.update(ingredients)
            self.allergens.update(allergens)

    def non_allergy_safe(self):
        not_safe = set()
        for allergen in list(self.allergens):
            ingredients = []
            for item in self.items:
                if allergen in item['allergens']:
                    ingredients.append(item['ingredients'])
            dangerous = ingredients[0]
            for i in ingredients[1:]:
                dangerous = dangerous.intersection(i)
            not_safe.update(dangerous)
        return not_safe

    def allergy_safe(self):
        safe = self.ingredients - self.non_allergy_safe()
        return safe

    def count_safe_ingredients(self):
        counter = 0
        for allergy_safe in self.allergy_safe():
            for item in self.items:
                if allergy_safe in item['ingredients']:
                    counter += 1
        return counter

    def map_ingredients_allergens(self):
        allergens_map = dict()
        safe_ingredients = self.allergy_safe()
        not_safe_ingredients = self.non_allergy_safe()
        # what not_safe_ingredients is not related to the allergens by item
        inverse_map = dict()
        # what not_safe_ingredients is not related to each allergen
        inverse_allergen = dict()
        for i, item in enumerate(self.items):
            not_safe = item['ingredients'].intersection(not_safe_ingredients)
            for allergen in item['allergens']:
                inverse_map[i] = inverse_map.get(allergen, set())
                inverse_map[i].update(not_safe)

            inverse_map[i] = not_safe_ingredients - inverse_map[i]
            for allergen in item['allergens']:
                inverse_allergen[allergen] = inverse_allergen.get(
                    allergen, set()
                )
                inverse_allergen[allergen].update(inverse_map[i])

        def _map_ingredient_allergen(items):
            for item in items:
                for allergen in item['allergens']:
                    ingredients = (
                        item['ingredients']
                        - safe_ingredients
                        - inverse_allergen[allergen]
                    )
                    if len(ingredients) == 1:
                        ingredient = list(ingredients)[0]
                        allergens_map[allergen] = ingredient
                        inverse_allergen.pop(allergen)
                        for i in items:
                            i['ingredients'] -= {ingredient}
                            i['allergens'] -= {allergen}
                        return

        while inverse_allergen:
            _map_ingredient_allergen(self.items)

        return allergens_map

    def get_canonical_dangerous(self):
        map_ = self.map_ingredients_allergens()
        canonical_list = [map_[k] for k in sorted(map_.keys())]
        return ','.join(canonical_list)


def main():
    with open('inputs/day_21.txt') as input_file:
        menu_items = input_file.read().splitlines()
    menu = Menu(menu_items)
    print(menu.count_safe_ingredients())
    print(menu.get_canonical_dangerous())


if __name__ == '__main__':
    main()