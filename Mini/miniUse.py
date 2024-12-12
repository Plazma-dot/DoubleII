from COMPILERMini import COMPILERMini

# Create an instance of the compiler
mini = COMPILERMini()

# Add program lines
mini.set_input('10 LET X = 5')
mini.set_input('20 IF X > 3 THEN 40')
mini.set_input('30 PRINT "This will not print."')
mini.set_input('40 PRINT "X is greater than 3."')
mini.set_input('50 END')

# List the program
mini.call('LIST')

# Run the program
mini.call('RUN')
