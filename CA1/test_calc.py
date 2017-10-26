

from Calc_test import Calculator
import unittest

class TestCalc(unittest.TestCase): 

    def test_calc_multiply(self):
        result = Calculator().multiply (5,5)
        self.assertEqual(25, result) 
        result = Calculator().multiply (5,0)
        self.assertEqual(0, result)    
        result = Calculator().multiply (5,1)
        self.assertEqual(5, result)
        result = Calculator().multiply (5,0.2)
        self.assertEqual(1, result)         

    def test_calc_add(self):
        result = Calculator().add (5,5)
        self.assertEqual(10, result)
        result = Calculator().add (2,3)
        self.assertEqual(5, result)
        try:
            Calculator().add('2', '5')
            self.fail('should have thrown error')
        except ValueError:
            pass
        
    def test_calc_subtract(self):
        result = Calculator().subtract (5,5)
        self.assertEqual(0, result) 
        result = Calculator().subtract (5,3)
        self.assertEqual(2, result) 
        result = Calculator().subtract (3,5)
        self.assertEqual(-2, result)      

    def test_calc_divide(self):
        result = Calculator().divide (5,5)
        self.assertEqual(1, result) 
        result = Calculator().divide (5,1)
        self.assertEqual(5, result)
        result = Calculator().divide (5,0.2)
        self.assertEqual(25, result)          
        result = Calculator().divide (5,4)
        self.assertEqual(1.25, result)
        result = Calculator().divide (5,0)
        self.assertEqual('nan', result)        

    def test_calc_exponent(self):
        result = Calculator().exponent (5,2)
        self.assertEqual(25, result) 
        result = Calculator().exponent (5,3)
        self.assertEqual(125, result) 
        result = Calculator().exponent (10, -2)
        self.assertEqual('error', result)     
        result = Calculator().exponent (3,0)
        self.assertEqual(1, result)       
        
    def test_calc_cube(self):
        result = Calculator().cube (3)
        self.assertEqual(27, result) 
        result = Calculator().cube (25)
        self.assertEqual(15625, result) 
        result = Calculator().cube (-2)
        self.assertEqual('error', result)     
        result = Calculator().exponent (0)
        self.assertEqual('error', result)  
        
    def test_factorial(self):
        result = Calculator().factorial(5)
        self.assertEqual(120, result)
        result = Calculator().factorial(6)
        self.assertEqual(720, result) 

    def test_sin_x(self):
        result = Calculator().sin_x(23)
        self.assertEqual(0.390731127744, result)
        result = Calculator().sin_x(-3)
        self.assertEqual(-0.0523359562429, result) 
        result = Calculator().sin_x(0)
        self.assertEqual(0, result)
        
    def test_cos_x(self):
        result = Calculator().cos_x(23)
        self.assertEqual(0.920504836759, result)
        result = Calculator().cos_x(0)
        self.assertEqual(1.0, result)         
        result = Calculator().cos_x(-3)
        self.assertEqual(0.998629534755, result)
        
    def test_tan_x(self):
        result = Calculator().tan_x(23)
        self.assertEqual(0.424468483103, result)
        result = Calculator().tan_x(-2)
        self.assertEqual(-0.0349207694917, result)   
        result = Calculator().tan_x(0)
        self.assertEqual(0, result)        
        
if __name__ == '__main__':
        unittest.main()
        

        
        
        
        
        
        
        