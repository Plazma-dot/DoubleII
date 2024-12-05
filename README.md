# BASIC Interpreter: `doubleII`

This is a simple **BASIC interpreter** that allows you to write, execute, save, and load BASIC programs with support for variables, arithmetic operations, and basic input/output functionality.

## Features:
- **Commands Supported**:
  - `LET` for variable assignments with support for arithmetic expressions.
  - `PRINT` to display output.
  - `INPUT` for taking user input and storing it in variables.
  - `RUN` to execute the program.
  - `LIST` to list the current program.
  - `SAVE` to save the program to a file.
  - `LOAD` to load a program from a file.
  - `EXIT` to exit the interpreter.
- **Variable Support**: Use variables in `LET` statements and `PRINT` commands.
- **Arithmetic Operations**: Support for basic arithmetic operations like addition, subtraction, multiplication, and division.
- **Persistent Storage**: Save and load programs to/from files.

## Requirements:
- Python 3.x
- `pyfiglet` (for program header)
- `termcolor` (for colored terminal output)

You can install the required libraries using `pip`:

```bash
pip install pyfiglet termcolor
