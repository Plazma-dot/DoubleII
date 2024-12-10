from Mini.COMPILERMini import COMPILERMini

# Initialize COMPILERMini
mini = COMPILERMini()

# Step 1: Add some lines of code
mini.set_input('10 PRINT "Hello, World!"')
mini.set_input('20 LET X = 10 + 5')
mini.set_input('30 PRINT "The value of X is "; X')
mini.set_input('40 END')

# Step 2: List the program
mini.set_input('LIST')

# Step 3: Run the program
mini.set_input('RUN')

# Step 4: Process inputs and display outputs
mini.main()  # Process all commands in the input queue

# Print captured output
print(mini.get_output())
