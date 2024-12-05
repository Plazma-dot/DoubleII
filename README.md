#BASIC Interpreter: doubleII
This is a simple BASIC interpreter that allows you to write, execute, save, and load BASIC programs with support for variables, arithmetic operations, and basic input/output functionality.

#Features:
  #Commands Supported:
    LET for variable assignments with support for arithmetic expressions.
    PRINT to display output.
    INPUT for taking user input and storing it in variables.
    RUN to execute the program.
    LIST to list the current program.
    SAVE to save the program to a file.
    LOAD to load a program from a file.
    EXIT to exit the interpreter.
    
  #Variable Support: Use variables in LET statements and PRINT commands.
  #Arithmetic Operations: Support for basic arithmetic operations like addition, subtraction, multiplication, and division.
  #Persistent Storage: Save and load programs to/from files.
  
#Requirements:
  Python 3.x
  pyfiglet (for program header)
  termcolor (for colored terminal output)
  
#You can install the required libraries using pip:
  pip install pyfiglet termcolor
      
#Running the Interpreter:
  Clone the Repository: If you haven't already, clone the repository or download the script file.
  git clone https://github.com/yourusername/doubleII.git
  cd doubleII
  #Run the Interpreter: 
    To run the interpreter, simply execute the Python script:
    python basic_interpreter.py
    This will start the interpreter in the terminal.

#Commands Overview:
  LET Command
  Assigns a value to a variable. You can use arithmetic operations in the assignment.
  
  10 LET X = 5 + 3
  20 LET Y = X * 2
  PRINT Command
  Prints output to the screen. You can print both strings and variables.
  
  30 PRINT X
  40 PRINT "Hello, World!"
  INPUT Command
  Prompts the user for input and stores the value in a variable.
  
  50 INPUT "Enter your name: ", Name
  60 PRINT "Hello, " + Name
  RUN Command
  Executes the program.
  
  RUN
  LIST Command
  Lists all the lines of code in the current program.
  
  LIST
  SAVE Command
  Saves the current program to a file. Specify the directory and filename.
  
  SAVE "C:/path/to/program.txt"
  LOAD Command
  Loads a program from a file.
  
  LOAD "C:/path/to/program.txt"
  EXIT Command
  Exits the interpreter.
  
  EXIT
  Example Program:
  10 LET X = 5 + 3
  20 LET Y = X * 2
  30 PRINT X
  40 PRINT Y
  50 INPUT "What is your name? ", Name
  60 PRINT "Hello, " + Name
  70 END

    Expected Output:
    8
    16
    What is your name? Alice
    Hello, Alice
    Saving and Loading Programs:
    To save your program, use the SAVE command followed by the path and filename. For example:

  SAVE "C:/Users/YourUsername/Desktop/my_program.txt"
  To load a program, use the LOAD command followed by the path to the file:
  LOAD "C:/Users/YourUsername/Desktop/my_program.txt"
  Notes:
  The interpreter is very basic and does not support advanced features like arrays, loops, or conditional statements.
  Arithmetic operations are evaluated using Python's built-in eval() function, so be cautious when working with user inputs or external data.
  Contributing:
  Feel free to contribute to this project! You can submit pull requests, open issues, or suggest improvements.
