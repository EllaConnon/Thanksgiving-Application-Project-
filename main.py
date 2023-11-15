#Thanksgiving Recipe Organizer Allowing for 5 Resipes
#Welcome Messages
#Define Array
Recipe = []

#Adding in Resipes
while True:
    numberOfRecipes = int(input("How many Resipies are you adding? (1-5) "))
    for i in range(numberOfRecipes):
        # Adding in Recipe
        recipeTitle = input("What is the title/name of the recipe? ")
        Recipe.append({
            "Recipe Title": recipeTitle
        })
    if numberOfRecipes == 1:
        RecipesOne = []
    elif numberOfRecipes == 2:
        RecipesTwo = []
    elif numberOfRecipes == 3:
        RecipesThree = []
    elif numberOfRecipes == 4:
        RecipesFour = []
    elif numberOfRecipes == 5:
        RecipesFive = []
    else:
        print("Error! Pick a number 1 through 5.")
        continue