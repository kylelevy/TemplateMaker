# Template Maker
_V.2._

I redid the original template maker with some big changes. I have restructured the code to work on an object oriented basis to make storing questions, answers and solutions way easier. Furthermore, I switched the document dependancy from fpdf to pyLaTeX. Mostly due to preference and simplicity. This would also allow for easy integration with LaTeX handle on formulas, graphs, tables, and equations. Hope this can be useful to someone who is making worksheets or practice problems for their students.

## How to Customize Questions and Solutions
Questions are just objects. In order to create your own, go into the `questionBank.py` and create a new subclass and set the question to yours as a string, and the answer will be given in the `solve()` function as a return equation. Then, go to the `main.py` and add the questions to the questionLink at the bottom under the horizontal line.

## Dependencies
* pylatex
* random

Copyright © 2023 by Kyle Levy