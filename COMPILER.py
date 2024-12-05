import os
import re
import sys
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('doubleII', font='starwars'), attrs=['bold'])

# Set a default save directory
DEFAULT_SAVE_DIR = r"C:\Users\ASUS\Desktop\DOUBLEII"

# Ensure the save directory exists
if not os.path.exists(DEFAULT_SAVE_DIR):
    os.makedirs(DEFAULT_SAVE_DIR)

# Tokenizer (Lexer)
def tokenize(line):
    tokens = re.findall(r'[\w\$]+|".*?"|[<>=+-/*(),.]', line)
    return tokens

# Parse a line of code
def parse_line(tokens):
    if tokens[0].isdigit():  # Line number
        line_number = int(tokens.pop(0))
    else:
        line_number = None
    
    command = tokens.pop(0).upper()  # Command like PRINT, INPUT
    args = tokens  # Remaining tokens are arguments
    return line_number, command, args

# Execute a command
def execute(command, args, variables):
    if command == "PRINT":
        # Handle PRINT command
        output = ""
        for arg in args:
            # Check if the argument is a variable or a literal string
            if arg.startswith('"') and arg.endswith('"'):
                output += arg.strip('"') + " "
            elif arg in variables:
                output += str(variables[arg]) + " "
            else:
                output += arg + " "
        print(output.strip())

    elif command == "INPUT":
        # Handle INPUT command
        prompt = " ".join(args).replace('"', '')
        user_input = input(prompt + " ")
        var_name = args[-1]  # Last token is the variable name
        variables[var_name] = user_input

    elif command == "LET":
        # Handle LET command with arithmetic
        var_name = args[0]
        try:
            expression = " ".join(args[2:])  # The part after "LET var_name = "
            # Replace variable names in the expression with their values
            for var in variables:
                expression = expression.replace(var, str(variables[var]))
            
            # Evaluate the arithmetic expression (this handles basic operations)
            value = eval(expression)
            variables[var_name] = value
        except Exception as e:
            print(f"Error: {e}")

    elif command == "END":
        # End the program
        return False
    else:
        print(f"Error: Unknown command '{command}'")
        return True
    return True

# Run the program
def run_program(lines):
    variables = {}
    line_index = 0
    # Sort the lines by line number before executing
    lines.sort(key=lambda x: x[0])  # Sort by the line number
    
    while line_index < len(lines):
        line_number, command, args = lines[line_index]
        if not execute(command, args, variables):
            break
        line_index += 1

# Save the program to a specific directory
def save_program(lines, directory, filename):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Combine the directory and filename
    filepath = os.path.join(directory, filename)
    
    with open(filepath, "w") as f:
        for line in lines:
            f.write(f"{line[0]} {' '.join([line[1]] + line[2])}\n")
    print(f"Program saved to {filepath}")

# Load the program from a specific directory
def load_program(directory, filename):
    filepath = os.path.join(directory, filename)
    
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} does not exist.")
        return []
    
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    parsed_lines = []
    for line in lines:
        tokens = tokenize(line.strip())
        parsed_line = parse_line(tokens)
        if parsed_line[0]:
            parsed_lines.append(parsed_line)
    print(f"Program loaded from {filepath}")
    return parsed_lines

# Main REPL loop
def main():
    print("Welcome to BASIC Interpreter!")
    lines = []
    
    while True:
        user_input = input("BASIC> ").strip()
        
        if user_input.upper() == "RUN":
            if lines:
                run_program(lines)
            else:
                print("Error: No program to run.")
        
        elif user_input.upper() == "LIST":
            if lines:
                # Sort the lines by line number before listing
                lines.sort(key=lambda x: x[0])  # Sort by the line number
                for line in lines:
                    print(f"{line[0]} {' '.join([line[1]] + line[2])}")
            else:
                print("No lines to list.")
        
        elif user_input.upper() == "EXIT":
            break
        
        elif user_input.upper().startswith("SAVE "):
            _, path_filename = user_input.split(maxsplit=1)
            path_filename = path_filename.strip('"')  # Remove quotes around the path/filename
            path_parts = path_filename.rsplit('/', 1)
            
            # If a directory is provided, split into directory and filename
            if len(path_parts) == 2:
                directory = path_parts[0]
                filename = path_parts[1]
            else:
                directory = DEFAULT_SAVE_DIR  # Default to the specified directory
                filename = path_parts[0]
            
            save_program(lines, directory, filename)
        
        elif user_input.upper().startswith("LOAD "):
            _, path_filename = user_input.split(maxsplit=1)
            path_filename = path_filename.strip('"')  # Remove quotes around the path/filename
            path_parts = path_filename.rsplit('/', 1)
            
            # If a directory is provided, split into directory and filename
            if len(path_parts) == 2:
                directory = path_parts[0]
                filename = path_parts[1]
            else:
                directory = DEFAULT_SAVE_DIR  # Default to the specified directory
                filename = path_parts[0]
            
            lines = load_program(directory, filename)
        
        else:
            # Tokenize and parse user input
            tokens = tokenize(user_input)
            if tokens:
                parsed_line = parse_line(tokens)
                if parsed_line[0]:  # Line number present
                    # Replace any existing line with the same number
                    lines = [line for line in lines if line[0] != parsed_line[0]] + [parsed_line]
                    # Sort the lines by line number after adding/replacing
                    lines.sort(key=lambda x: x[0])
                else:
                    print("Error: Invalid syntax.")

if __name__ == "__main__":
    main()
