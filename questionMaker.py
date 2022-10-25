# Creates question functions from user input
import re

# Patterns
varpattern = re.compile("\$+[a-zA-Z0-9]+\$")
_VARpattern =  r"VAR"
remove_sign = r"\$"

# Question from user
usr_input = input("Insert your question with $ wrapping the variabels:")

# Break down input to obtain variable names
variableNames = varpattern.findall(usr_input)

print(variableNames)

# Formatting for the code
newVarNames = []

for object in variableNames:
    newVarName = re.sub(remove_sign,'',object)
    newVarNames.append(newVarName)

print(newVarNames)

questionString = re.sub(varpattern,'"+str(VAR)+"',usr_input)

print(questionString)

i = -1

def replace(match):
    global i
    i += 1
    return newVarNames[i]

questionString2 = re.sub(_VARpattern, replace, questionString)
print(questionString2)


print()
print()

data = ''
count = 0

#Figuring out which number question this is

with open("questionBank.py", 'r') as infile:
    data = infile.readlines()

for line in data:
    if '#' in line:
        count += 1

n = count


# Determining solution formula
ans_formula = input("What is the solution to the problem in variables? *USE EXACT NAMES")


print(f"""
# Question {n}
def Q{n}():
    {newVarNames[0]} = random.randint(0,10)
    {newVarNames[1]} = random.randint(0,10)
    {newVarNames[2]} = random.randint(0,10)
    {newVarNames[3]} = random.randint(0,10)
    {newVarNames[4]} = random.randint(0,10)
    question = str("{questionString2}")
    answer = str({ans_formula})

    return [question,answer]
""")

#Appends answer to question bank
# f = open("questionBank.py", "a")
# f.write(f"""
#
#
# # Question {n}
# def Q{n}():
#     {newVarNames[0]} = random.randint(0,10)
#     {newVarNames[1]} = random.randint(0,10)
#     question = str("{questionString2}")
#     answer = str({ans_formula})
#
#     return [question,answer]
# """)
# f.close()
