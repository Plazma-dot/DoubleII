import os
import re
import sys
from typing import List, Tuple, Union
from termcolor import cprint
from pyfiglet import figlet_format

# Clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()
cprint(figlet_format('double II', font='starwars'), attrs=['bold'])

# Default save directory
DEFAULT_SAVE_DIR = os.getcwd()

# Ensure the save directory exists
os.makedirs(DEFAULT_SAVE_DIR, exist_ok=True)

# Memory slots for storing program lines
MEM_SLOT: List[Tuple[int, str, List[str]]] = []

# Tokenizer (Lexer)
def tokenize(line: str) -> List[str]:
    return re.findall(r'[\w\$]+|".*?"|[<>=+\-/*(),.]', line)

# Parse a line of code
def parse_line(tokens: List[str]) -> Tuple[Union[int, None], str, List[str]]:
    line_number = int(tokens.pop(0)) if tokens[0].isdigit() else None
    command = tokens.pop(0).upper()
    args = tokens
    return line_number, command, args

def execute(command: str, args: List[str], variables: dict, line_index: int, 
            lines: List[Tuple[int, str, List[str]]], call_stack: List[int]) -> Tuple[bool, int]:
    command = command.upper()

    if command == "PRINT":
        output = " ".join(
            arg.strip('"') if arg.startswith('"') and arg.endswith('"') else str(variables.get(arg, arg))
            for arg in args
        )
        print(output)

    elif command == "INPUT":
        prompt = " ".join(args[:-1]).replace('"', '')
        var_name = args[-1]
        variables[var_name] = input(f"{prompt} ")

    elif command == "LET":
        var_name = args[0]
        expression = " ".join(args[2:])
        try:
            for var, value in variables.items():
                expression = expression.replace(var, str(value))
            variables[var_name] = eval(expression)
        except Exception as e:
            print(f"Error evaluating LET expression: {e}")

    elif command == "HOME":
        clear_console()
        return False, line_index

    elif command == "GOTO":
        target_line = int(args[0])
        target_index = next((i for i, line in enumerate(lines) if line[0] == target_line), None)
        return (True, target_index) if target_index is not None else (print(f"Line {target_line} not found."), line_index)

    elif command == "GOSUB":
        target_line = int(args[0])
        target_index = next((i for i, line in enumerate(lines) if line[0] == target_line), None)
        if target_index is not None:
            call_stack.append(line_index + 1)
            return True, target_index
        print(f"Line {target_line} not found.")
        return False, line_index

    elif command == "RETURN":
        if call_stack:
            return True, call_stack.pop()
        print("RETURN called without matching GOSUB.")

    elif command == "END":
        return False, line_index

    elif command == "IF":
        try:
            condition, then_command = " ".join(args).split(" THEN ", 1)
            condition_result = eval(condition, {}, variables)
            if condition_result:
                new_tokens = tokenize(then_command)
                _, then_command, then_args = parse_line(new_tokens)
                return execute(then_command, then_args, variables, line_index, lines, call_stack)
        except Exception as e:
            print(f"Error evaluating IF condition: {e}")

    else:
        print(f"Unknown command: {command}")
    
    return True, line_index

# Run the program
def run_program(lines: List[Tuple[int, str, List[str]]]):
    variables = {}
    call_stack = []
    line_index = 0

    while line_index < len(lines):
        line_number, command, args = lines[line_index]
        continue_execution, new_index = execute(command, args, variables, line_index, lines, call_stack)
        if not continue_execution:
            break
        line_index = new_index if new_index != line_index else line_index + 1

# Save the program
def save_program(lines: List[Tuple[int, str, List[str]]], directory: str, filename: str):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        for line in lines:
            f.write(f"{line[0]} {' '.join([line[1]] + line[2])}\n")
    print(f"Program saved to {filepath}")

# Load the program
def load_program(directory: str, filename: str) -> List[Tuple[int, str, List[str]]]:
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} does not exist.")
        return []

    with open(filepath, "r") as f:
        lines = [parse_line(tokenize(line.strip())) for line in f]
    print(f"Program loaded from {filepath}")
    return lines

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
                for line in sorted(lines, key=lambda x: x[0]):
                    print(f"{line[0]} {' '.join([line[1]] + line[2])}")
            else:
                print("No lines to list.")

        elif user_input.upper() == "HOME":
            clear_console()

        elif user_input.upper() == "EXIT":
            break

        elif user_input.upper().startswith("SAVE "):
            path_filename = user_input[5:].strip('"')
            directory, filename = os.path.split(path_filename) or (DEFAULT_SAVE_DIR, path_filename)
            save_program(lines, directory or DEFAULT_SAVE_DIR, filename)

        elif user_input.upper().startswith("LOAD "):
            path_filename = user_input[5:].strip('"')
            directory, filename = os.path.split(path_filename) or (DEFAULT_SAVE_DIR, path_filename)
            lines = load_program(directory or DEFAULT_SAVE_DIR, filename)

        else:
            tokens = tokenize(user_input)
            if tokens:
                parsed_line = parse_line(tokens)
                if parsed_line[0] is not None:
                    lines = [line for line in lines if line[0] != parsed_line[0]] + [parsed_line]
                    lines.sort(key=lambda x: x[0])
                else:
                    print("Error: Invalid syntax.")

if __name__ == "__main__":
    main()
