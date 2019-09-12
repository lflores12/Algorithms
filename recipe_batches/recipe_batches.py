#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch_count = []
    for name, value in recipe.items():
        if name in ingredients:
            res = ingredients[name] // value
            batch_count.append(res)
        else:
            batch_count.append(0)
    return min(batch_count)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 200, 'butter': 55, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
