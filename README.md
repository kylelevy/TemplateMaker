# Template Maker
_V.2._

I redid the original template maker with some significant changes. First, I have restructured the code to work on an object-oriented basis to simplify storing questions, answers and solutions. Furthermore, I switched the document dependency from fpdf to pyLaTeX, primarily due to preference and simplicity. This would allow easy integration with LaTeX handle on formulas, graphs, tables, and equations. I hope this is useful to someone making worksheets or practice problems for their students.

## How to Customize Questions and Solutions
Questions are just objects. To create your own, go into the `questionBank.py`, create a new subclass, and set the question to yours as a string, and the answer will be given in the `solve()` function as a return equation. Then, go to the `main.py` and add the questions to the questionLink at the bottom under the horizontal line.

## Dependencies
* pylatex
* random

Copyright © 2023 by Kyle Levy
