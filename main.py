#Thanksgiving Recipe Organizer Allowing for 5 Recipes
#Welcome Messages
print(" ")
print("Welcome to the Thanksgiving 5 Recipe holder! If you need help using this application please read the README page's instructions. Enjoy!!")
print(" ")
#Define Arrays
#overall recipes
Recipe = []
#details
RecipesOne = []
RecipesTwo = []
RecipesThree = []
RecipesFour = []
RecipesFive = []
#ingredients array
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

steps = True
m = 1
#Adding in Recipes
while True:
    numberOfRecipes = int(input("How many Resipies are you adding? (1-5) "))
    for i in range(1, numberOfRecipes+1, 1):
        # Adding in Recipe
        recipeTitle = input("What is the title/name of the recipe? ")
        Recipe.append(recipeTitle)
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
               print("Just enter the step, no numbers in front of the step.")
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
           RecipesTwo.append(ingredientsTwo)
           while steps:
               print("Just enter the step, no numbers in front of the step.")
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
               ingredientsThree.append(ingredient)
               ingredientsThree.append(amount)
               ingredientsThree.append(unit)
           RecipesThree.append(ingredientsThree)
           while steps:
               print("Just enter the step, no numbers in front of the step.")
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
               print("Just enter the step, no numbers in front of the step.")
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
               print("Just enter the step, no numbers in front of the step.")
               step = input("What is the step? ")
               stepFive.append(step)
               steps = input("Are there more steps? ")
               steps = steps == "yes" or steps == "Yes"
           RecipesFive.append(stepFive)
           Recipe.append(RecipesFive)
           print(" ")
#else error statment
        else:
           print("Error! Pick a number 1 through 5.")
           continue
    break
while True:
    num = len(Recipe)
    print(" ")
    print("Your Recipes:")
    for e in range(0,num,2):
        print(str(m)+".) "+str(Recipe[e]))
        m = m+1
    which = int(input("Which recipe would you like to view? "))
    numb = len(RecipesOne)
    numb = numb - 2
    print(" ")
    
    if which == 1:
        print(Recipe[0])
        for q in range(numb):
            print(RecipesOne[q])
        print(' ')
        numb = len(ingredientsOne)
        numbb = numb/3
        e=0
        m=1
        for w in range(0,numbb+1, 3):
            print(ingredientsOne[e]+" "+ingredientsOne[e+2]+" "+ingredientsOne[e+1])
            e = e + 3
        for q in range(len(stepsOne)):
            print(str(m) +".) "+ str(stepsOne[q]))
            m = m+1

    elif which == 2:
        print(Recipe[2])
        for q in range(numb):
            print(RecipesTwo[q])
        print(' ')
        numb = len(ingredientsTwo)
        numbb = numb/3
        e=0
        m=1
        for w in range(0,numbb+1, 3):
            print(ingredientsTwo[e]+" "+ingredientsTwo[e+2]+" "+ingredientsTwo[e+1])
            e = e + 3
        for q in range(len(stepTwo)):
            print(str(m) +".) "+ str(stepTwo[q]))
            m = m+1

    elif which == 3:
        print(Recipe[4])
        for q in range(numb):
            print(RecipesThree[q])
        print(' ')
        numb = len(ingredientsThree)
        numbb = numb/3
        e=0
        m=1
        for w in range(0,numbb+1, 3):
            print(ingredientsThree[e]+" "+ingredientsThree[e+2]+" "+ingredientsThree[e+1])
            e = e + 3
        for q in range(len(stepThree)):
            print(str(m) +".) "+ str(stepThree[q]))
            m = m+1

    elif which == 4:
        print(Recipe[6])
        for q in range(numb):
            print(RecipesFour[q])
        print(' ')
        numb = len(ingredientsFour)
        numbb = numb/3
        e=0
        m=1
        for w in range(0,numbb+1, 3):
            print(ingredientsFour[e]+" "+ingredientsFour[e+2]+" "+ingredientsFour[e+1])
            e = e + 3
        for q in range(len(stepFour)):
            print(str(m) +".) "+ str(stepFour[q]))
            m = m+1

    elif which == 5:
        print(Recipe[8])
        for q in range(numb):
            print(RecipesFive[q])
        print(' ')
        numb = ingredientsFive.len()
        numbb = numb/3
        e=0
        m=1
        for w in range(0,numbb+1, 3):
            print(ingredientsFive[e]+" "+ingredientsFive[e+2]+" "+ingredientsFive[e+1])
            e = e + 3
        for q in range(len(stepFive)):
            print(str(m) +".) "+ str(stepFive[q]))
            m = m+1
    
    ask = input("Would you like to view another recipe? ")
    if ask == "yes" or ask == "Yes":
        continue
    else:
        break