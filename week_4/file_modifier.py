# File Read and Write with error handling

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as infile:
        content = infile.read()
        modified = content.upper()

    with open('modified_output.txt', 'w') as outfile:
        outfile.write(modified)

    print("File has been modified and saved as 'modified_output.txt'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    print("Error: An I/O error occurred while handling the file.")