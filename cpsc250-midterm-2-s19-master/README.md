# Midterm Exam 1

You may only consult with:
* Your instructor to clarify intent of questions if needed
* https://gitlab.pcs.cnu.edu   - your personal CS150 and CS250 repo's only
* Your single sheet (double sided) of handwritten notes

You will also have access to the following Python doc pages.
* https://docs.python.org/3/

No other help is allowed.

Fork this project to your personal `first.last.yy-cpsc250-f18` group (not your default personal group).

Clone to the local computer (and remember the folder you used).

Add the project to PyCharm.

Ignore WebCat errors. My unit test is different than the one loaded to WebCat.

Comment out any code that you cannot get to work.
(Leave it in place in case I look for partial credit.)

## Don't forget to look at code in the given folder!

## Make sure you complete the Scholar portion of quiz and submit first (20 points)

___If you get stuck move on to next question or ask your instructor for clarification; don't just sit there "spinning your wheels" without making progress.___

__DO NOT modify any tests or code in given folder!__

****

# File I/O - do 2 (and only 2) of the 3 programs File I/O Programs

## CSV Input

Shell code is given in `src1/program1.py` ; associated tests are in the `test1/test_program1.py`.

Import the data as defined in the `data/csv_data.txt` file and `program1.py`
* Read the data 
* Return as separate lists as directed in method doc string

## Text File Search

Shell code with details is given in the `src2/program2.py` script; associated test is `test2/test_program2.py`.

Given fully specified file path, read the data from file and return a number of occurrences of the given word.

## File Copy

Shell code with details is given in the `src3/program3.py` script; associated test is `test3/test_program3.py`.

Given the source and target, both fully specified file path, 
copy the file without using any module.

# Class definition and inheritance (2 of 3 required) 
****

## Method Overloads

See the instructions given in `src4/program4.py` script; associated tests are `test4/test_program4.py`.

* Implement the required operator overload for "+"  as described in the doc string of `program4.py`

## Class Inheritance I

See the instructions given in `src5/program5.py` script; associated tests are `test5/test_program5.py`.

This requires you to write one class that inherits from `given/person.py` file.
* You are required to override the method that converts to `str`
  * modify as directed in the `program5.py` file
* You should build upon the given code in the `Person` and `Hero` classes.

## Class Inheritance II

See the instructions given in `src6/program6.py` script; associated tests are `test6/test_program6.py`.

This requires you to write one class that inherits from both `given/person.py` 
and `given\hero.py` classes.

* You are required to override the method that converts to `str`
* You should build upon the given code in the `Person` class 
* You should be sure to call the constructors for both the `Person` and `Hero` classes.




