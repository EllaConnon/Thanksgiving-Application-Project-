#Thanksgiving Recipe Organizer Allowing for 5 Resipes
#Welcome Messages
#Define Varibles
time = 0
#Define Arrays
Recipe = []
RecipesOne = []
RecipesTwo = []
RecipesThree = []
RecipesFour = []
RecipesFive = []
#Define Functions
def recipeDetails(array):
    time = int(input("How many hours will "))
#Adding in Resipes
while True:
    numberOfRecipes = int(input("How many Resipies are you adding? (1-5) "))
    for i in range(1, numberOfRecipes+1, 1):
        # Adding in Recipe
        recipeTitle = input("What is the title/name of the recipe? ")
        Recipe.append({
            "Recipe Title": recipeTitle
        })
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
        if i == 2:
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