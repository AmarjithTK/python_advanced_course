## Sequence types ================

	 lists , tuples , range , etc

	 lists = [ 'hi there ', 'its fun' , 'not too much' , 'mongi anamika ' , ' ammonnma']
	 tuples = ('335', 'dark knight' , '35.35' , '3434', 'wondersland')

	 range = range(10,51)



## List vs Tuples ===================

	  - List and tuple both can be homogenous or hetrogenous
	  - List is dynamic and tuple is static in nature
	  - Insertion and deletion can be done on lists but **not on tuples
	  - Methods can be applied on lists **only
  
  
  
## Python Slicing 

 
   	  - Getting a slice from string with constraints


	  	python indexing is upper exclude [0,7)  - 7 not included


		slice(start,end,gap) default gap =1


		string =  'amarnathak'

		string[slice(1,7,2)] - output mra 




	 - Magic method for slice
	 

    	string[start:end:gap] - read it twice
    	
    	name = 'arjun.html'
    	
    	name[1:3:1]  -  'rj'  is output // upper boundary is open bracket [1,3)
    	
    	name[2:] - jun.html
    	name[1:] - rjun.html
    	name[-4:-1] - htm
    	name[-3:] - tml 
    	name[-6:] - n.html ***** used once
    	
    - Indexing array
    
    	name[6] - h
    	name[-3] - t
    	
 	- List vs Tuples
 		
 		
 		list = ['homo1', 'homo2', 'home3']   - Homogenous resizable
 		
 		tuple =  ('hetro',25, 'hetrogenout',44,'curly bracket')  - Hetrogenous and 	non resized
 		
 		tupleupdated =  ('hetrogenous',22,'hetro',55,'curly bra')



		 
    	
    
    
    
