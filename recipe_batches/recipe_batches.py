#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batch = 0
    
    for item in recipe:
        if item not in ingredients: # checking if all required ingrediants are available
            print("Cannot make any batches")
            return 0

    while True:   # each loop subtracts the last amount until quantity of ingrediants no longer greater then recipe
        for food, quantity in ingredients.items():
            if quantity >= recipe.get(food):
                quantity -= recipe.get(food)
                ingredients[food] = quantity
            
            else:
              return batch
        batch += 1  # each loop = 1 batch

    return batch

    


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 10, 'butter': 5, 'flour': 5}
  ingredients = { 'milk': 20, 'butter': 59, 'flour': 50 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
