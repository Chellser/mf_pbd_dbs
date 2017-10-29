    
class Calculator(object): 
    
    def number_types (self, x, y): 
        number_types = (int, float, complex)
        if not isinstance(x, number_types) or not isinstance(y, number_types): 
            raise ValueError
        return ' '
        
    def number_types_2 (self, x): 
        number_types_2 = (int, float, complex)
        if not isinstance(x, number_types_2): 
            raise ValueError
        return ' '    
    
    def add(self, x, y):
        self.number_types(x,y)
        return x + y

    def cube(self, x):
        self.number_types_2(x)    
        if x == 0:
            return 'error'
        if x < 0:
            return 'error'
    
        return x * x * x
        
    def divide(self, x, y):
        self.number_types(x,y)
        if y == 0:
            return 'nan'
        return x / float(y)
        
    def exponent(self, x, y):
        self.number_types(x,y)
        if y == 0:
            return 1
        if y < 0:
            return 'error'
    
        return x ** y
                
    def factorial(self, x):
        self.number_types_2(x)   
        return reduce(lambda x,y:x*y, [1]+range(1,x+1))
        
    def factorial_simple(self, x):
        self.number_types_2(x)  
        if x == 0:
           return 1
        else:
            return x * self.factorial_simple(x - 1)

    def multiply(self, x, y):
        self.number_types(x,y)    
        return x * y
                        
    def subtract(self, x, y):
        self.number_types(x,y)    
        return x - y            
            
# Sin, Cos and Tan all calculated using the Taylor Polynomial Series which requires that we convert x into rad by multiplying it by pi. 
     
    def sin_x(self, x):
        self.number_types_2(x)    
        pi = 3.14159265358979323846264
        rad = x * pi / 180
        return rad - (rad**3 / self.factorial_simple(3)) + (rad**5 / self.factorial_simple(5)) - (rad**7 / self.factorial_simple(7))

    def cos_x(self, x):
        self.number_types_2(x)  
        pi = 3.14159265358979323846264
        rad = x * pi / 180
        return 1 - (rad**2 / self.factorial_simple(2)) + (rad**4 / self.factorial_simple(4)) - (rad**6 / self.factorial_simple(6)) 
        
    def tan_x(self, x):
        self.number_types_2(x)     
        pi = 3.14159265358979323846264
        rad = x * pi / 180
        return rad + ((rad**3) * 1/3) + ((rad**5) * 2/15) + ((rad**7) * 17/315)
        

    def number_input(self):
        valid_input = False
        while not valid_input:  
            try: 
            # ask the user to enter up to two numbers
                numb_input = raw_input('Enter up to two numbers to calculate (use a space to seperate) : ')
                numbers = list(map(float,numb_input.split(' '))) #take up to two numbers turn them into intergers, split them at the space, and add to a list
                valid_input = True 
                return numbers
            except:
                print 'Please enter a valid number.'
                

    def xy_function(self,x,y): #A function has a definitive number of parameters. Need two functions to cover two-number inputs.
        valid_input = False
        while not valid_input: 
            try:
            # ask user what calculation function they want to use            
                op = int(raw_input(
                "Which mathematical function would you like to use?: \n"
                "Enter 1 for addition. \n"
                "Enter 2 for subtraction. \n"
                "Enter 3 for multiplication. \n"
                "Enter 4 for division. \n"  
                "Enter 5 for exponent. \n"
                "Enter 0 to quit. \n"
                ))
                if op == 1: 
                    return self.add(x,y)
                elif op == 2: 
                    return self.subtract(x,y)
                elif op == 3: 
                    return self.multiply(x,y)
                elif op == 4:
                    return self.divide(x,y)
                elif op == 5: 
                    return self.exponent(x,y)
                elif op == 0:
                    return 'Thank you, goodbye'
                    valid_input = True
                else:
                    print 'This program requires you to enter a number from 1 - 5 or 0 to quit' 
                    print 
            except: 
                print 'Please enter a valid number.'
    
    def x_function(self, x):
        valid_input = False
        while not valid_input: 
            try:
            # ask user what calculation function they want to use
                op = int(raw_input(
                "Which mathematical function would you like to use?: \n"
                "Enter 1 for sin. \n"
                "Enter 2 for cos. \n"
                "Enter 3 for tan. \n"
                "Enter 4 for cube. \n"
                "Enter 5 for factorial. \n"
                "Enter 0 to quit. \n"
                ))
                if op == 1:
                    return self.sin_x(x)
                elif op == 2:
                    return self.cos_x(x)
                elif op == 3:
                    return self.tan_x(x)
                elif op == 4:
                    return self.cube(x)
                elif op == 5:
                    return self.factorial_simple(x)   
                elif op == 0:
                    return 'Thank you, goodbye'
                    valid_input = True
                else:
                    print 'This program requires you to enter a number from 1 - 5 or 0 to quit'   
                    print 
            except:
                print 'Please enter a valid number.'
