#Thanksgiving Recipe Organizer Allowing for 5 Resipes
#Welcome Messages
#Define Arrays
#overall resipies
Recipe = []
#details
RecipesOne = []
RecipesTwo = []
RecipesThree = []
RecipesFour = []
RecipesFive = []
#ingredits array
ingredientsOne = ["Ingredients: "]
ingredientsTwo = ["Ingredients: "]
ingredientsThree = ["Ingredients: "]
ingredientsFour = ["Ingredients: "]
ingredientsFive = ["Ingredients: "]
#steps arrays
stepsOne = ["Steps: "]
stepTwo = ["Steps: "]
stepThree = ["Steps: "]
stepFour = ["Steps: "]
stepFive = ["Steps: "]
#are there more stps
steps = True
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
                "Prep Time(minutes): ": prepTime
            })
            RecipesOne.append({
                "Cook Time(minutes): ": cookTime
            })
            RecipesOne.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                unit = input("What unit is the measurement in? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                ingredientsOne.append(ingredient)
                ingredientsOne.append(amount)
                ingredientsOne.append(unit)
            RecipesOne.append(ingredientsOne)
            while steps:
                print("Step format: #.) step here")
                step = input("What is the step? ")
                stepsOne.append(step)
                steps = input("Are there more steps? ")
                steps = steps == "yes" or steps == "Yes"
            RecipesOne.append(stepsOne)
            Recipe.append(RecipesOne)
            print(" ")
#Recipe 2
        elif i == 2:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesTwo.append({
                "Prep Time(minutes): ": prepTime
            })
            RecipesTwo.append({
                "Cook Time(minutes): ": cookTime
            })
            RecipesTwo.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                unit = input("What unit is the measurement in? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                ingredientsTwo.append(ingredient)
                ingredientsTwo.append(amount)
                ingredientsTwo.append(unit)
            RecipesTwo.append(ingredientsOne)
            while steps:
                print("Step format: #.) step here")
                step = input("What is the step? ")
                stepTwo.append(step)
                steps = input("Are there more steps? ")
                steps = steps == "yes" or steps == "Yes"
            RecipesTwo.append(stepTwo)
            Recipe.append(RecipesTwo)
            print(" ")
#Recipe 3
        elif i == 3:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesThree.append({
                "Prep Time(minutes): ": prepTime
            })
            RecipesThree.append({
                "Cook Time(minutes): ": cookTime
            })
            RecipesThree.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                unit = input("What unit is the measurement in? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                ingredientsOne.append(ingredient)
                ingredientsOne.append(amount)
                ingredientsOne.append(unit)
            RecipesThree.append(ingredientsOne)
            while steps:
                print("Step format: #.) step here")
                step = input("What is the step? ")
                stepThree.append(step)
                steps = input("Are there more steps? ")
                steps = steps == "yes" or steps == "Yes"
            RecipesThree.append(stepThree)
            Recipe.append(RecipesThree)
            print(" ")
#Recipe 4
        elif i == 4:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesFour.append({
                "Prep Time(minutes): ": prepTime
            })
            RecipesFour.append({
                "Cook Time(minutes): ": cookTime
            })
            RecipesFour.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                unit = input("What unit is the measurement in? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                ingredientsFour.append(ingredient)
                ingredientsFour.append(amount)
                ingredientsFour.append(unit)
            RecipesFour.append(ingredientsFour)
            while steps:
                print("Step format: #.) step here")
                step = input("What is the step? ")
                stepFour.append(step)
                steps = input("Are there more steps? ")
                steps = steps == "yes" or steps == "Yes"
            RecipesFour.append(stepFour)
            Recipe.append(RecipesFour)
            print(" ")
#Recipe 5
        elif i == 5:
            prepTime = int(input("How many minutes does it take to prep for this recipe? "))
            cookTime = int(input("How many minutes does it take to cook this recipe? "))
            servings = float(input("How many servings does the recipe yield? "))
            RecipesFive.append({
                "Prep Time in minutes: ": prepTime
            })
            RecipesFive.append({
                "Cook Time in minutes: ": cookTime
            })
            RecipesFive.append({
                "Yields: ": servings
            })
            numberOfIngredients = int(input("How many ingredients are in the recipe? "))
            for w in range(numberOfIngredients):
                ingredient = input("What is the ingredient? ")
                unit = input("What unit is the measurement in? ")
                amount = float(input("How much of " + str(ingredient) + "? "))
                ingredientsFive.append(ingredient)
                ingredientsFive.append(amount)
                ingredientsFive.append(unit)
            RecipesFive.append(ingredientsFive)
            while steps:
                print("Step format: #.) step here")
                step = input("What is the step? ")
                stepFive.append(step)
                steps = input("Are there more steps? ")
                steps = steps == "yes" or steps == "Yes"
            RecipesFive.append(stepFive)
            Recipe.append(RecipesFive)
            print(" ")
        else:
            print("Error! Pick a number 1 through 5.")
            continue