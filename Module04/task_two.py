import string

def count_words(filename):
    try:
        # Open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove punctuation from the content
        # Create a translation table to remove all punctuation
        translator = str.maketrans('', '', string.punctuation)
        content_no_punct = content.translate(translator)
        
        # Split the content into words and count them
        words = content_no_punct.split()
        
        return len(words)
    
    except FileNotFoundError:
        # Return None if the file doesn't exist
        return None
    
filename = r"C:\Users\pcber\Documents\GitHub\Assignments_46W38\Module04\The_Zen_of_Python.txt"

# Call the function and get the word count
word_count = count_words(filename)

# Print the result using a formatted f-string
if word_count is not None:
    print(f"File: '{filename}' contains {word_count} words.")
else:
    print(f"Error: File '{filename}' not found.")