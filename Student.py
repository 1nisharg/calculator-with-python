
class calculator:
   def __init__(self, num1 , num2):
    self.num1 = num1
    self.num2 = num2

   def add(self):
     print(self.num1 + self.num2)

   def subract(self):
      print(self.num1 - self.num2)

   def multiply(self):
        print(self.num1 * self.num2)

   def divide(self):
          print(self.num1 / self.num2)


calc = calculator(5, 3)
result = calc.divide()           

print(result) 