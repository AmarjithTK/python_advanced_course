### Creating a class object

    class class_name:


        def __init__(self, para1 , para2 , para3):
            self.para1 = para1
            self.para2 = para2

        def catchup(self):    <---- Self parameter allows catchup function to access parameter of other function ( init function )
            round(self.para2)
            return self.para2  

    ** self is like the class object variables which are private 

    global variable contained to use only for the methods inside the 
    


    type() function - this function returns the type of anything !!


    type(datetime)
    < class type = type >
    ----------------- Both are blueprint -----------------
    type(Geopoint)
    < class type = type >


    fathers_day = datetime(1989,10,31)
    type(fathers_day)
    < class type = datetime.datetime>

    -------------- These are instances , actual production -------------

    thalasssery =  Geopoint(latitude = "50" , longitude = "43.54")
    type(thalasssery)
    < class type = Geopoint.Geopoint>


    instance methods vs class methods

    instance methods require a instance of the blueprint class to be created to be able to apply

    eg :
    
     kolkata = Geopoint(latitude = 13.5 , longitude = 24.53)
     kolkata.get_weather()  -------> instance methods



    class methods needs no init to use. 

    eg :

     from geopoint import Geopoint 
     Geopoint.random()  --------> class methods

    class variables and instance variables : 

        class classname :

            flowers = 'rose' |   class variables or blueprint variables
            color = 'blue'   |

            def __init__(self,beauty_number,esr_value):
                self.beauty_number = beauty_number |   
                self.esr_value = esr_value         | instance variables provided on init





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
            
            
            
