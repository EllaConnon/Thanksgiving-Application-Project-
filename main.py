#Thanksgiving Recipe Organizer Allowing for 5 Resipes
#Welcome Messages
#Define Arrays
Recipe = []
RecipesOne = []
RecipesTwo = []
RecipesThree = []
RecipesFour = []
RecipesFive = []
#Adding in Resipes
while True:
    numberOfRecipes = int(input("How many Resipies are you adding? (1-5) "))
    for i in range(1, numberOfRecipes+1, 1):
        # Adding in Recipe
        recipeTitle = input("What is the title/name of the recipe? ")
        Recipe.append({
            "Recipe Title": recipeTitle
        })
#Recipe 1
        if i == 1:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesOne.append({
                "Prep Time: ": prepTime
            })
            RecipesOne.append({
                "Cook Time: ": cookTime
            })
            RecipesOne.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                RecipesOne.append({
                    "Ingredient: ": ingredient
                })
                RecipesOne.append({
                    "Amount of ingredient: ": amount
                })
            print("Input Next Recipe")
#Recipe 2
        elif i == 2:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesTwo.append({
                "Prep Time: ": prepTime
            })
            RecipesTwo.append({
                "Cook Time: ": cookTime
            })
            RecipesTwo.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                RecipesTwo.append({
                    "Ingredient: ": ingredient
                })
                RecipesTwo.append({
                    "Amount of ingredient: ": amount
                })
            print("Input Next Recipe")
#Recipe 3
        elif i == 3:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesThree.append({
                "Prep Time: ": prepTime
            })
            RecipesThree.append({
                "Cook Time: ": cookTime
            })
            RecipesThree.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                RecipesThree.append({
                    "Ingredient: ": ingredient
                })
                RecipesThree.append({
                    "Amount of ingredient: ": amount
                })
            print("Input Next Recipe")
#Recipe 4
        elif i == 4:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesFour.append({
                "Prep Time: ": prepTime
            })
            RecipesFour.append({
                "Cook Time: ": cookTime
            })
            RecipesFour.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                RecipesFour.append({
                    "Ingredient: ": ingredient
                })
                RecipesFour.append({
                    "Amount of ingredient: ": amount
                })
            print("Input Next Recipe")
#Recipe 5
        elif i == 5:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesFive.append({
                "Prep Time: ": prepTime
            })
            RecipesFive.append({
                "Cook Time: ": cookTime
            })
            RecipesFive.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                nit = input("What unit is the measurement in? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                RecipesFive.append({
                    "Ingredient: ": ingredient
                })
                RecipesFive.append({
                    "Amount of ingredient: ": amount
                })
            print("Input Next Recipe")
        else:
            print("Error! Pick a number 1 through 5.")
            continue
