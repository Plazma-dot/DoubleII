# DoubleII - A BASIC Interpreter for Python

DoubleII is an open-source BASIC interpreter inspired by the Apple II. It allows you to write, execute, save, and load BASIC programs, supporting variables, arithmetic operations, and basic input/output functionality.

# About
This project is based on the Apple II and BASIC, interpreted through Python. It's an ongoing open-source effort for BASIC programming enthusiasts.

## Features

- **Commands Supported**:
  - `LET` for variable assignments (supports arithmetic expressions)
  - `PRINT` to display output
  - `INPUT` for taking user input
  - `GOTO` to jump to a line
  - `GOSUB`/`RETURN` for function calls
  - `RUN` to execute the program
  - `LIST` to display the program
  - `SAVE`/`LOAD` to save/load programs
  - `EXIT` to exit the interpreter
- **Variable Support**: Use variables in `LET` and `PRINT` commands
- **Arithmetic**: Supports basic operations (addition, subtraction, multiplication, division)
- **Persistent Storage**: Save/load programs to/from files

## Requirements

- Python 3.x
- `pyfiglet` for program headers
- `termcolor` for colored output

## Install dependencies with:

```bash
pip install pyfiglet termcolor
```

## COMPILERMini
**Differences** from the full version:

- `set_input`: Imitates terminal input
- `get_output`: Analogous to print() in the full version

## MicroPython
**The MicroPython version is still in testing. Feel free to edit and contribute!**

## License
**This project is licensed under the MIT License.**
