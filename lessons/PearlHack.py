"""Pearl Hackthon - Books by Women Recommendations Based off of Interest Questions"""
"""Time to book it."""
 
___author__ = "Lucia Wang", "Jillian Whitener", "Colleen Whitener"
 
# book lists - check that the quotation marks format correctly
classics = ["'Anne of Green Gables' by L.M. Montgomery", "'Jane Eyre' by Charlotte Bronte", "'Pride and Prejudice' by Jane Austen", "'To Kill a Mockingbird' by Harper Lee", "'Frankenstein' by Mary Shelley", "'Wuthering Heights' by Emily Bronte", "'Orlando' by Virginia Woolf", "'Anthem' by Ayn Rand”", "'Mrs. Dalloway' by Virgnia Woolf"]
romance = ["'Beach Read' by Emily Henry", "'Throne of Glass' by Sarah J Maas", "'7th Circle' by Tate James", "'Four Psychos' by Kristy Cunning”", "'Gypsy Blood' by Kristy Cunning", "'The Silver Swan' by Amo Jones", "'Pestilence' by Laura Thalassa", "'Trickery' by Jaymin Eve", "'Dark Horse' by Kel Carpenter"]
poetry = ["'Still I Rise' by Maya Angelou", "'The Hill We Climb' by Amanda Gorman", "'Hope is the Thing with Feathers' by Emily Dickinson", "'Valentine' by Carol Ann Duffy", "'The Dark' by Carol Ann Duffy", "'A Song: Lying is an Occupation' by Laetitia Pilkington", "'Because I Could Not Stop for Death' by Emily Dickinson", "'Sad Women' by Daria Domitrovic", "'Mad Girl's' by Sylvia Plath"]
new_adult = ["'The Truth About Forever' by Sarah Dessen", "'In the Unlikely Event' by L.J. Shen", "'The Girl in the Love Song' by Emma Scott", "'Canary' by Tijan", "'Stalk Me' by Jillian Dodd", "'It Ends with Us' by Colleen Hoover", "'After' by Anna Todd", "'Admit Me You Want Me' by Taylor Holloway", "'Our Stop' by Laura Jane Williams"]
fantasy = ["'A Wizard of Earthsea' by Ursula K. Le Guin", "'Dark King' by C.N. Crawford", "'Fae Hunter' by Sarah Wilson", "'The Poppy War' by R.F. Kuang", "'The Fifth Season' by N. K. Jemisin", "'A Court of Thornes and Roses' by Sarah J. Mass", "'Dark Horse' by Kell Carpenter", "'Princess Ballot' by Jaymin Eve"]
 
# function goes through the questionaires


def bookrec():
    print("\n\nWelcome to the book recommendation generator. \n\tThis tool will provide a book recommendation to you based on your answers to a few questions... \n\t\t And all of the books in our database are written by women!")
 
    input("\nWhenever you're ready, press enter.")
 
    genre = input("\nWhat kind of place do you want to live in? \n\nPlease choose from the following: \n\tMansion, Townhouse, House, Condo, Castle \n\n\tType your choice here and press enter: ")
 
    while genre != "Mansion" and genre != "Townhouse" and genre != "House" and genre != "Condo" and genre != "Castle":
        genre = input("\nSorry, try again. \n\tType your choice here: ")
 
    mood = input("\nHow would you describe yourself? \n\nPlease choose from the following: Introvert, Extrovert, Ambivert \n\n\tType your choice here and press enter: ")
   
    while mood != "Introvert" and mood != "Extrovert" and mood != "Ambivert":
        mood = input("\nSorry, try again. \n\tType your choice here: ")
 
    print("\nLove that for you. \n\tNext question. ")
   
    focus = input("\nWhat is your favorite style of clothing? \n\nPlease choose from the following: \n\tFancy, Casual, Quirky \n\n\tType your choice here and press enter: ")
   
    while focus != "Fancy" and focus != "Casual" and focus != "Quirky":
        focus = input("\nSorry, try again. \n\tType your choice here: ")
 
    answers = [genre, mood, focus]
   
    book = findbook(answers)  # calls the actual generator
   
    print("\nBased on your responses, the book you should read is... ")
    print("\n(Count down with us!!)")
    input("\n\t 3.........")
    input("\n\t\t 2......")
    input("\n\t\t\t1...\n")
    print(book)
    print("\n\tEnjoy your book recommendation! Come back soon for another book!")
# function uses the answers to randomly generate a book
 
 
def findbook(ans=[]):
    # genre: mansion = classics,condo = romance, townhouse = poetry, house =  new adult, castle = fantasy ,
    # mood: introvert = sad, extrovert = happy, ambivert = funny
    # focus: fancy = relationship, casual = character, quirky = plot
    # if they don't answer with the right answers we can randomize over the list of joke books
    #  you can essentially copy from this line to 75 and then change the ans[0] and random.choice() to the correct ones based on the key
    if (ans[0] == "Mansion"):  # mansion = classics
        if(ans[1] == "Extrovert"):  # happy
            if(ans[2] == "Casual"):  # character
                return(classics[0])
            elif(ans[2] == "Quirky"):  # plot
                return(classics[1])
            elif(ans[2] == "Fancy"):  # relationship
                return(classics[2])
        elif(ans[1] == "Introvert"):  # sad
            if(ans[2] == "Casual"):  # character
                return(classics[3])
            elif(ans[2] == "Quirky"):  # plot
                return(classics[4])
            elif(ans[2] == "Fancy"):  # relationship
                return(classics[5])
        elif(ans[1] == "Ambivert"):  # funny
            if(ans[2] == "Casual"):  # character
                return(classics[6])
            elif(ans[2] == "Quirky"):  # plot
                return(classics[7])
            elif(ans[2] == "Fancy"):  # relationship
                return(classics[8])
    elif (ans[0] == "Condo"):  # condo = romance
        if(ans[1] == "Extrovert"):
            if(ans[2] == "Casual"):
                return(romance[0])
            elif(ans[2] == "Quirky"):
                return(romance[1])
            elif(ans[2] == "Fancy"):
                return(romance[2])
        elif(ans[1] == "Introvert"):
            if(ans[2] == "Casual"):
                return(romance[3])
            elif(ans[2] == "Quirky"):
                return(romance[4])
            elif(ans[2] == "Fancy"):
                return(romance[5])
        elif(ans[1] == "Ambivert"):
            if(ans[2] == "Casual"):
                return(romance[6])
            elif(ans[2] == "Quirky"):
                return(romance[7])
            elif(ans[2] == "Fancy"):
                return(romance[8])
    elif (ans[0] == "Townhouse"):  # townhouse = poetry
        if(ans[1] == "Extrovert"):
            if(ans[2] == "Casual"):
                return(poetry[0])
            elif(ans[2] == "Quirky"):
                return(poetry[1])
            elif(ans[2] == "Fancy"):
                return(poetry[2])
        elif(ans[1] == "Introvert"):
            if(ans[2] == "Casual"):
                return(poetry[3])
            elif(ans[2] == "Quirky"):
                return(poetry[4])
            elif(ans[2] == "Fancy"):
                return(poetry[5])
        elif(ans[1] == "Ambivert"):
            if(ans[2] == "Casual"):
                return(poetry[6])
            elif(ans[2] == "Quirky"):
                return(poetry[7])
            elif(ans[2] == "Fancy"):
                return(poetry[8])  
    elif (ans[0] == "House"):  # house = new adult
        if(ans[1] == "Extrovert"):
            if(ans[2] == "Casual"):
                return(new_adult[0])
            elif(ans[2] == "Quirky"):
                return(new_adult[1])
            elif(ans[2] == "Fancy"):
                return(new_adult[2])
        elif(ans[1] == "Introvert"):
            if(ans[2] == "Casual"):
                return(new_adult[3])
            elif(ans[2] == "Quirky"):
                return(new_adult[4])
            elif(ans[2] == "Fancy"):
                return(new_adult[5])
        elif(ans[1] == "Ambivert"):
            if(ans[2] == "Casual"):
                return(new_adult[6])
            elif(ans[2] == "Quirky"):
                return(new_adult[7])
            elif(ans[2] == "Fancy"):
                return(new_adult[8])  
    elif (ans[0] == "Castle"):  # castle = fantasy
        if(ans[1] == "Extrovert"):
            if(ans[2] == "Casual"):
                return(fantasy[0])
            elif(ans[2] == "Quirky"):
                return(fantasy[1])
            elif(ans[2] == "Fancy"):
                return(fantasy[2])
        elif(ans[1] == "Introvert"):
            if(ans[2] == "Casual"):
                return(fantasy[3])
            elif(ans[2] == "Quirky"):
                return(fantasy[4])
            elif(ans[2] == "Fancy"):
                return(fantasy[5])
        elif(ans[1] == "Ambivert"):
            if(ans[2] == "Casual"):
                return(fantasy[6])
            elif(ans[2] == "Quirky"):
                return(fantasy[7])
            elif(ans[2] == "Fancy"):
                return(fantasy[8])
 
 
bookrec()
