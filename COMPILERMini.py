import os
import re
from termcolor import cprint
from pyfiglet import figlet_format

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

    def tokenize(self, line):
        return re.findall(r'[\w\$]+|".*?"|[<>=+-/*(),.]', line)

    def parse_line(self, tokens):
        if tokens[0].isdigit():
            line_number = int(tokens.pop(0))
        else:
            line_number = None

        command = tokens.pop(0).upper()
        args = tokens
        return line_number, command, args

    def execute(self, command, args, line_index):
        command = command.upper()
        if command == "PRINT":
            output = "".join(
                arg.strip('"') + " " if arg.startswith('"') else str(self.variables.get(arg, arg)) + " "
                for arg in args
            )
            self._print(output.strip())

        elif command == "INPUT":
            if self.input_queue:
                user_input = self.input_queue.pop(0)
            else:
                user_input = input(" ".join(args).replace('"', '') + " ")
            var_name = args[-1]
            self.variables[var_name] = user_input

        elif command == "LET":
            var_name = args[0]
            expression = " ".join(args[2:])
            for var in self.variables:
                expression = expression.replace(var, str(self.variables[var]))
            try:
                self.variables[var_name] = eval(expression)
            except Exception as e:
                self._print(f"Error: {e}")

        elif command == "GOTO":
            target_line = int(args[0])
            for idx, line in enumerate(self.lines):
                if line[0] == target_line:
                    return idx
            self._print(f"Error: Line {target_line} not found.")

        elif command == "END":
            return None
        return line_index + 1

    def run_program(self):
        self.variables.clear()
        self.call_stack.clear()
        line_index = 0

        while line_index is not None and line_index < len(self.lines):
            line_number, command, args = self.lines[line_index]
            line_index = self.execute(command, args, line_index)

    def process_input(self, user_input):
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
                if parsed_line[0]:
                    self.lines = [line for line in self.lines if line[0] != parsed_line[0]] + [parsed_line]
                else:
                    self._print("Error: Invalid syntax.")

    def main(self):
        while self.input_queue:
            self.process_input(self.input_queue.pop(0))

# Example usage
if __name__ == "__main__":
    mini = COMPILERMini()
    mini.set_input('10 PRINT "hello world"')
    mini.set_input('20 END')
    mini.set_input('RUN')
    mini.main()
    print(mini.get_output())
