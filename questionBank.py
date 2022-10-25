# Retrieve input
import random
import math

#Question 1 as a function
def Q1():
    x = random.randint(0,10)
    y = random.randint(0,10)
    question = str("What is the product of "+str(x)+" and "+str(y)+"?")
    answer = str(x*y)

    return [question,answer]

#Question 2
def Q2():
    x = random.randint(0,10)
    y = random.randint(0,10)
    question = str("What is the sum of "+str(x)+" and "+str(y)+"?")
    answer = str(x+y)

    return [question,answer]
