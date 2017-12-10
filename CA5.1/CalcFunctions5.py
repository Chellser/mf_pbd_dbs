import math 
    
class Calculator(object): 
 
    def add(a, b):
        return map(lambda x,y: x+y, a, b)
    print add ([10, 20, 30], [1,2,3])
        
    def subtract(a, b):
        return map(lambda x,y: x-y, a, b)
    print subtract ([10, 20, 30], [1,2,3])
        
    def multiply (a, b):
        return map(lambda x,y: x*y, a, b)
    print multiply ([10, 20, 30], [1,2,3])
        
    def divide (a, b):
        return map(lambda x,y: 'nan' if y == 0 else x/float(y), a, b)
    print divide ([10, 20, 30], [1,2,3])
        
    def cube(a):
        return map(lambda x: x*x*x, a)
    print cube ([10, 20, 30])
        
    def exponent(a, b): 
        return map (lambda x, y: x ** y, a, b)
    print exponent ([10, 20, 30], [1,2,3])        
                
    def factorial(a):
        return map(lambda x: math.factorial(x) ,a)
    print factorial ([2, 4, 8])
    
    def sqrt(a):
        return map(lambda x: math.sqrt(x), a)
    print sqrt ([10, 20, 30])
   
    def power(a, b):
        return map (lambda x, y: math.pow(x, y), a, b)
    print power ([2, 4, 6], [3, 5, 7])

    def log10(a):
        return map(lambda x: math.log10(x), a)  
    print log10 ([5, 7, 9])

    
    def number_input(self):
        valid_input = False
        while not valid_input:  
            try: 
            # ask the user to enter up to two numbers
                numbers = [int(x) for x in input('Enter a list of numbers to calculate (use a space to seperate) : ').split(',')] 
                valid_input = True 
                return numbers
            except:
                print 'Please enter a valid number.'
                

    def calc_function(a,b): #A function has a definitive number of parameters. Need two functions to cover two-number inputs.
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
                "Enter 6 for cube. \n"
                "Enter 7 for factorial. \n"
                "Enter 8 for square root. \n"
                "Enter 9 for power. \n"
                "Enter 10 for log10. \n"
                "Enter 0 to quit. \n"
                ))
                if op == 1: 
                    return list(map(lambda x,y: x+y, a, b))
                elif op == 2: 
                    return list(map(lambda x,y: x-y, a, b))
                elif op == 3: 
                    return list(map(lambda x,y: x*y, a, b))
                elif op == 4:
                    return list(map(lambda x,y: 'nan' if y == 0 else x/float(y), a, b))
                elif op == 5: 
                    return list(map(lambda x, y: x ** y, a, b))                
                elif op == 6: 
                    return list(map(lambda x: x*x*x, a))         
                elif op == 7: 
                    return list(map(lambda x: math.factorial(x) ,a))
                elif op == 8: 
                    return list(map(lambda x: math.sqrt(x), a) )
                elif op == 9: 
                    return list(map(lambda x, y: math.pow(x, y), a, b))                   
                elif op == 10: 
                    return list(map(lambda x: math.log10(x), a))                     
                elif op == 0:
                    return 'Thank you, goodbye'
                    valid_input = True
                else:
                    print 'This program requires you to enter a number from 1 - 10 or 0 to quit' 
                    print 
            except: 
                print 'Please enter a valid number.'
    

