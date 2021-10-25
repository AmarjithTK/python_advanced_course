# Sequence types ================

# lists , tuples , range , etc

# lists = [ 'hi there ', 'its fun' , 'not too much' , 'mongi anamika ' , ' ammonnma']
# tuples = ('335', 'dark knight' , '35.35' , '3434', 'wondersland')

# range = range(10,51)



# List vs Tuples ===================

#  - List and tuple both can be homogenous or hetrogenous
#  - List is dynamic and tuple is static in nature
#  - Insertion and deletion can be done on lists but **not on tuples
#  - Methods can be applied on lists **only




:: String manipulation


    string_text = "I don't know " 


    print(string_text)


    #  ' I don't know' [false] python execution failed miserably
    #  'I don\'t know ' [true] python successful
    #  "I don't know"   [true] python successful

    #   \ is known as escape sequence
    #   It escapes the sequential character - Don't treat the next character as part of syntax

    wordiii = """  hello love'd "world  """ 

    # Triple quotes are used when  ** double quotes and ** single quotes are included in text

    # Syntax is -  """ ------- Enter the '" " 'nonsense" here -------- """


    # Use either Triple quotes or Escape sequences accordingly





String Methods ============



:: List all - dir(str) or dir("any string") 


    'islower, isnumeric, isspace , istitile , isupper, capitalisze , isdecimal etc'


    name = "mongi anamika"


    name.capitalize() -  capitalized first letter


    name.split("*")  -  splits into array with '*' as seperator


    name.title() - Capitalize first letter of all words


    name.__add__('junior citizen') - concatenate python backend


    name.__contains("5") -  return true if 5 is found   



:: Template literal  js alternative in python

user = 'mongi123'

Normal way
    
    message = 'User ' + user +'is logged in'


::Template literal way (string interpolation)

    message = f"User {user} is logged in" 
     - dont forget the 'f' in the start


Python slicing ==========



Getting a slice from string with constraints


 /// python indexing is upper exclude [0,7)  - 7 not included


    slice(start,end,gap) default gap =1


    string =  'amarnathak'

    string[slice(1,7,2)] - output mra 




Magic method for slice

    string[start:end:gap] 




