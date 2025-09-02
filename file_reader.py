with open("input.txt")as rozzie:
    content = rozzie.read()
    print(content)
#Converting text to uppercase 
content_upper = content.upper()
print(content_upper)

#splitting the text into words and counting them
words = content.split()
word_count = len(words)
print(f"The number of words: {word_count}")

#wrtinfg the results to output.txt
with open("output.txt", "w") as output_file:
    output_file.write(content_upper)
    output_file.write(f"\nNumber of words: {word_count}\n")

#Asking user for a file name to read
userFile = input("Enter the file name to process" )

try:

    with open("user_File", "r") as userFile:
        user_content = userFile.read()
        print(user_content)
except FileNotFoundError:
    print(f"Error: The file was not found.")
    exit()
except PermissionError:
    print(f"Error: You do not have permission to read the file.")
    exit()