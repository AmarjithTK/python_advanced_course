## The Advanced python learning

### Basic lessons

    dir() -- this function can be used to list the all methods associated with a class 

    usage -- dir(Map) - Lists all map methods such as __str__ , __save__ etc

    help () -- lists usage of methods. parameters etc


    suppose I do 
    x = 25
    y = x.__add__(50)

    __add__() function takes two parameters - self,value
    self parameter is the variable x itself

    in reality -->
    y = x.__add__(self , value to be added)



    for eg : folium package . To find the location of the original package files use

    folium.__file__   -  gets the directory of the package




### Summary of the class Vocabulary

    Class - blueprint of object 
    Instance - object created from blueprint
    Method - something that gets an input and gives output
    Constructor - Init function 
    Instance method - Methods available only after creating an object
    Class method - Methods available without having to create object
    Parameters - variables listed in constructor method
    Arguments - variables at the creating of the object instance
    Instance variable - Variables in the 'self' repo
    Class variable - variables for the blueprint
    Attributes - those which are accesible from  '.' method

       


### Some dumb doubts

    why can't we use functions instead of using classes, Function can be modified for any requirement right ?

    Can you do a method on a function - I mean function on top of function but only when we need it

    what is the difference between a class and an object ?

    An instance of class definition is known as object 

    Class methods versus instance methods ?

    class methods require no initialisation at all . But instance methods require object to be created from class blueprint


    how to access class variables from instance methods

    class Geopoint:
        scale = '50.75'
        width = '55'


        def meter(self):
            print(Geopoint.scale)
            print(Geopoint.width)

    








