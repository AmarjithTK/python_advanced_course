variable = 'pi'

class piupdate:
    def __init__(self,*variable):
        variable = 'hello'
        return variable
pi = piupdate(variable)  

print(variable,pi)