# Code smells

A code smell is any characteristic in the source code that possibly indicates a deeper problem. The term become popular
during the 90s at the same time when clean code principles were articulated. Many code smells are just the negative
formulation of clean code principles.

The table below contains the most easily recognizable code smells on the function / method level that indicate clean
code issues. When you create or refactor (rewrite, optimize, etc.) code, pay attention to these, and act accordingly.

| **Issue**                     | **Symptom**                                                                             | **Symptom**                                                                                                               | **Symptom**                                                                |
|-------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| ***Bad naming***              | Non-English identifiers, One letter variable names                                      | Not following the name formatting convention (e.g., camel-case or other word separation instead of underscores in Python) | Deceptive variable / method name (e.g., variable `numbers` contains names) |
| ***Badly formatted code***    | Multiple statements in one line                                                         | Unnecessary blank lines                                                                                                   | Wrong indentation                                                          |
| ***Repeated code***           | Code block or line is repeated when it could be organized into functions                | Not using parameters where it could reduce repeating logic in multiple functions                                          |                                                                            |
| ***Long function or method*** | Long function or method block (> 30 lines)                                              | Long parameter list (>3)                                                                                                  |                                                                            |
| ***Wrong comment usage***     | Uncommented code block (where comment could clear up the functionality of a code block) | Useless comment                                                                                                           | No comment at all                                                          |
| ***Dead code***               | Contains unused code block or line                                                      | Never reachable code lines (e.g., through a bad condition)                                                                |                                                                            |

You should start focusing on the top 3 issues first. The others will gain importance as your projects will get
lengthier.