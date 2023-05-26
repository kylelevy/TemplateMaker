# ******************************************************************************
#
#                             Template Maker V.2.
#                            Created by Kyle Levy
#
# Copyright © 2023 by Kyle Levy
# ******************************************************************************

import numpy as np
from pylatex import Document, Section, Subsection, Math, NoEscape
from questionBank import *


global counter
global AnswerKey
global rows
global doc
global questionList
counter=1
AnswerKey = ''
questionList = []
rows = 3

def page_compile():
    # Creates the document
    doc = Document()

    # Creates a question section and appends all the questions on the questionList
    with doc.create(Section('Questions')):
        for question in questionList:
            AppendQuestion(question, question.solve(), doc)
    
    # Inserts a new page to avoid crowding
    doc.append(NoEscape(
    r'''
    \newpage
    '''))

    # Creates an answers section and appends the answer key
    with doc.create(Section('Answers')):
        doc.append(AnswerKey)

    # Compile LaTeX into PDF
    doc.generate_pdf('Worksheet', clean_tex=False)

    


# Append Question to document
def AppendQuestion(Q, answer, doc):
    global counter
    global AnswerKey
    # Print Question
    doc.append("Q"+str(counter)+")  "+str(Q.question))
    doc.append('\n\n\n\n\n\n\n')

    # Append to Answer Key
    AnswerKey += "Q"+str(counter)+" Answer: "+str(answer)

    if counter%rows == 0:
        AnswerKey += "\n"
    else:
        AnswerKey += "   |   "

    counter = counter+1


# ------------------------------------------------------------------------------

# Pick the questions and how the answers are found in the question bank
# I have chosen to loop these questions so that I get 5 unique problems of
# each type.

# Creating the question list using the questionBank library

for i in range(5):
    Q1 = Add('What is x + y?',random.randint(0,100),random.randint(0,100))
    questionList.append(Q1)

for i in range(5):
    Q2 = Multiply('What x * y?', random.randint(0,12), random.randint(0,12))
    questionList.append(Q2)


#Format fixing for Answer Key
if (counter-1)%3 != 0:
    AnswerKey = AnswerKey[:-7]

# Compile document
page_compile()