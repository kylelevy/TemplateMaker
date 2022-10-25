# TemplateMaker
A software designed to automatically generate random value word problems based on user input. (It exports as a pdf work sheet with an answer key)

This code depends on fpdf. This code will create a pdf with random value word problems. It will append an answer key to the end of the document. The questions can be customized by modifying the Question Bank file. This can be done using the Question Maker script.

The quetion bank contains the question functions with the question and answer as an array. 

The question maker is a script which creates the question functions using the user input and regular expressions to extract the variable names and replace them with random values when they are implimented into the document. Once extracted, the user can prove the solution formula in terms of the variables they gave so that the answer key can be populated.
