import os
import re

class COMPILERMini:
    def __init__(self):
        self.lines = []  # Program lines
        self.variables = {}  # Variables storage
        self.call_stack = []  # Call stack for GOSUB/RETURN
        self.output = []  # Captured output
        self.input_queue = []  # Simulated input queue

    def set_input(self, user_input):
        """Simulates user input to the program."""
        self.input_queue.append(user_input)

    def get_output(self):
        """Returns all captured output."""
        return "\n".join(self.output)

    def _print(self, message):
        """Captures output instead of printing directly."""
        self.output.append(message)

    def call(self, user_input):
        """Processes a single user command and updates the output."""
        self.input_queue.append(user_input)
        self.main()
        print("\n".join(self.output))
        self.output.clear()

    def tokenize(self, line):
        """Tokenizes a line of code into individual components."""
        return re.findall(r'[\w\$]+|".*?"|[<>=+\-/*(),.]', line)

    def parse_line(self, tokens):
        """Parses a tokenized line into line number, command, and arguments."""
        line_number = int(tokens.pop(0)) if tokens[0].isdigit() else None
        command = tokens.pop(0).upper()
        args = tokens
        return line_number, command, args

    def execute(self, command, args, line_index):
        """Executes a single command."""
        command = command.upper()
        try:
            if command == "PRINT":
                output = " ".join(
                    arg.strip('"') if arg.startswith('"') and arg.endswith('"') else str(self.variables.get(arg, arg))
                    for arg in args
                )
                self._print(output.strip())

            elif command == "INPUT":
                prompt = " ".join(args[:-1]).replace('"', '')
                var_name = args[-1]
                user_input = self.input_queue.pop(0) if self.input_queue else input(f"{prompt} ")
                self.variables[var_name] = user_input

            elif command == "LET":
                var_name = args[0]
                expression = " ".join(args[2:])
                for var, value in self.variables.items():
                    expression = expression.replace(var, str(value))
                self.variables[var_name] = eval(expression)

            elif command == "IF":
                condition = " ".join(args[:-2])
                target_line = int(args[-1])
                for var, value in self.variables.items():
                    condition = condition.replace(var, str(value))
                if eval(condition):
                    for idx, line in enumerate(self.lines):
                        if line[0] == target_line:
                            return idx

            elif command == "GOTO":
                target_line = int(args[0])
                for idx, line in enumerate(self.lines):
                    if line[0] == target_line:
                        return idx
                self._print(f"Error: Line {target_line} not found.")

            elif command == "END":
                return None

        except Exception as e:
            self._print(f"Error executing {command}: {e}")

        return line_index + 1

    def run_program(self):
        """Runs the stored program from the beginning."""
        self.variables.clear()
        self.call_stack.clear()
        line_index = 0

        while line_index is not None and line_index < len(self.lines):
            line_number, command, args = self.lines[line_index]
            line_index = self.execute(command, args, line_index)

    def process_input(self, user_input):
        """Processes a single user command."""
        user_input = user_input.strip()
        if user_input.upper() == "RUN":
            self.run_program()
        elif user_input.upper() == "LIST":
            for line in sorted(self.lines, key=lambda x: x[0]):
                self._print(f"{line[0]} {' '.join([line[1]] + line[2])}")
        else:
            tokens = self.tokenize(user_input)
            if tokens:
                parsed_line = self.parse_line(tokens)
                if parsed_line[0] is not None:
                    self.lines = [line for line in self.lines if line[0] != parsed_line[0]] + [parsed_line]
                else:
                    self._print("Error: Invalid syntax.")

    def main(self):
        """Processes all commands in the input queue."""
        while self.input_queue:
            self.process_input(self.input_queue.pop(0))
