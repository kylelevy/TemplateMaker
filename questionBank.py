# Retrieve input
import random
import math

# Define a Question class
class Question:
    def __init__(self, question, var1, var2):
        self.question = question
        self.var1 = var1
        self.var2 = var2

        self.question = question.replace('x', str(self.var1))
        self.question = self.question.replace('y', str(self.var2))

class Add(Question):
    def solve(self):
        return self.var1 + self.var2
        
class Multiply(Question):
     def solve(self):
          return self.var1 * self.var2