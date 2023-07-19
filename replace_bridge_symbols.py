# Define the replacement symbols
symbols = {"!C": "<font color=green>&clubs;</font>", "!D": "<font color=orange>&diams;</font>", "!H": "<font color=red>&hearts;</font>", "!S": "<font color=blue>&spades;</font>"}

# Open the file in read and write mode
with open("system.md", "r+") as file:
  # Read the input string from the file
  input_string = file.read()

  # Loop through the symbols and replace them in the input string
  for key, value in symbols.items():
    input_string = input_string.replace(key, value)

  # Move the file pointer to the beginning of the file
  file.seek(0)

  # Write the output string to the file
  file.write(input_string)
