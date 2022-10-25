# ******************************************************************************
#
#                                Template Maker
#                            Created by Kyle Levy
#
#
# ******************************************************************************

from fpdf import FPDF
from questionBank import *

pdf = FPDF('P', 'mm', 'Letter')

pdf.add_page()

pdf.set_font('times', '', 11)

pdf.set_auto_page_break(auto=True, margin = 40)

pdf.set_font('times', 'U', 18)
pdf.multi_cell(200, 20, 'Document Title',0,'C',ln=True)
global counter
global AnswerKey
global rows
counter=1
AnswerKey = ''

#Customization Section
rows = 3

# Append Question to PDF
def AppendQuestion(function, times):
    global counter
    global rows
    global AnswerKey
    for x in range(times):
        # Print Question
        temp = function()
        pdf.set_font('times','', 11)
        pdf.multi_cell(200,10,"Q"+str(counter)+")  "+str(temp[0]),ln=True)

        if counter < 3:
            pdf.cell(200,80,'',0,2)
        else:
            pdf.cell(200,55,'',0,2)

        # Append to Answer Key
        AnswerKey += "Q"+str(counter)+" Answer: "+str(temp[1])

        if counter%rows == 0:
            AnswerKey += "\n"
        else:
            AnswerKey += "   |   "

        counter = counter+1


# ------------------------------------------------------------------------------

# Pick the questions you want and how many you would like
# from the question bank

AppendQuestion(Q1,5)
AppendQuestion(Q2,5)



#Format fixing for Answer Key
if (counter-1)%3 != 0:
    AnswerKey = AnswerKey[:-7]

# Answer Key
pdf.add_page()
pdf.set_font('times', '', 24)
pdf.cell(40,20,'Answer Key', ln=True)
pdf.set_font('times','',14)
pdf.multi_cell(200,15, AnswerKey,0,'C')

print(AnswerKey)

#Exprot
pdf.output('Worksheet.pdf')
