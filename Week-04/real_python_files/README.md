# Running Python Files from Your Terminal
All this information is also in the main readme file one directory up. 


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

