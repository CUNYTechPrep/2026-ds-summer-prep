# Week 04 - Last week of Summer Prep


### Agenda
0. Turn on 'transcripts' / try to get CC with names. 
0. Remind me to start recording. 
0. Check HW
0. Lecture
0. Secret Word
0. Break
0. [Jeopardy!](https://jeopardylabs.com/play/summer-prep-jeopardy-4)
0. Discussion 
0. NO HW :) 

### Lecture Topics
0. Classes / Objects
0. Break and continue.
0. Smart use of return.
0. Try and Except.
0. Checking types. 
0. Yall seem to like print string formatting. 
0. Reading / Writing Files
0. Bad vs Good Coding Techinques
0. Using inputs in jupyter notebooks
0. Matplotlib sucks
0. Running a 'real' non-notebook python .py file.
    * running a file, inputting args, asking for input, importing helper functions


#### Running 'real' .py files.
For example, we have a few `.py` files in the real_python_files folder.  

To run any python file, open your terminal and type in 
`python3 <name_of_python_file.py>`

For example:
`python3 01_run_print_five.py`

Passing in arguments:
`python3 02_input_args.py Zack 40`

Better way to pass in args:
`python3 03_better_input_args.py --name Zack --age 40`

### WTF is `if __name__ == "__main__":`

```python
.
.
.

if __name__ == "__main__":
    run_my_function()
```

TLDR - it means if you RUN THIS FILE DIRECTLY FROM THE TERMINAL, it will the code below.  However, if you IMPORT the file into another file, it will not run. 

It controls the execution of code in a script depending on whether the script is being run directly or imported as a module (aka library or file). 

 
### Getting inputs/arguments from user
* When using the input() command, it's essential to:
* Provide clear and informative prompts.
* Validate the input to ensure it meets expected criteria.
* Handle invalid input gracefully, guiding the user to correct their input.
* Convert the input to the appropriate data type and handle errors accordingly.
* Avoid using input() in a way that assumes perfect input from the user.


# There is no HW or exercise. The rest of class will be for a discussion
1. What's the best way to succeed at CTP?
1. Whats the most important deliverable for CTP?
1. Do we have tests and finals?
1. Ask questions in slack. 