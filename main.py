#Thanksgiving Recipe Organizer Allowing for 5 Resipes
#Welcome Messages
#Define Array
Recipe = []

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
            RecipesOne = []
        elif i == 2:
            RecipesTwo = []
        elif i == 3:
            RecipesThree = []
        elif i == 4:
            RecipesFour = []
        elif i == 5:
            RecipesFive = []
        else:
            print("Error! Pick a number 1 through 5.")
            continue