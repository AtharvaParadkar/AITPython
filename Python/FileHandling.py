# Read file word by word:
def read_file_word_by_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        for word in words:
            print(word)
filename = 'sample.txt'  # Replace with your file name
read_file_word_by_word(filename)


#Read character by character from a file:
def read_file_character_by_character(filename):
    with open(filename, 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            print(char)
filename = 'sample.txt'  # Replace with your file name
read_file_character_by_character(filename)


#Get number of characters, words, spaces, and lines in a file:
def count_file_stats(filename):
    with open(filename, 'r') as file:
        content = file.read()
        char_count = len(content)
        word_count = len(content.split())
        space_count = content.count(' ')
        line_count = content.count('\n')
        print(f"Number of characters: {char_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of spaces: {space_count}")
        print(f"Number of lines: {line_count}")
filename = 'sample.txt'  # Replace with your file name
count_file_stats(filename)


#Count the number of occurrences of a key-value pair in a text file:
def count_key_value_occurrences(filename, key, value):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if key in line and value in line:
                count += 1
    print(f"Number of occurrences: {count}")
filename = 'sample.txt'  # Replace with your file name
key = 'key'  # Replace with your key
value = 'value'  # Replace with your value
count_key_value_occurrences(filename, key, value)


#Find 'n' character words in a text file:
def find_n_character_words(filename, n):
    with open(filename, 'r') as file:
        words = file.read().split()
        n_character_words = [word for word in words if len(word) == n]
        print(f"Words with {n} characters: {n_character_words}")
filename = 'sample.txt'  # Replace with your file name
n = 5  # Replace with the desired number of characters
find_n_character_words(filename, n)


#Count the number of lines in a text file in Python:
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for _ in file)
        print(f"Number of lines: {line_count}")
filename = 'sample.txt'  # Replace with your file name
count_lines(filename)


#Read a list of dictionaries from a file:
import json
def read_list_of_dictionaries(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    print(data)
filename = 'sample.json'  # Replace with your file name
read_list_of_dictionaries(filename)


#Append content of one text file to another:
def append_file_content(source_file, destination_file):
    with open(source_file, 'r') as source:
        content = source.read()
    with open(destination_file, 'a') as destination:
        destination.write(content)
source_file = 'sample.txt'  # Replace with your source file name
destination_file = 'destination.txt'  # Replace with your destination file name
append_file_content(source_file, destination_file)


#Reverse the content of a file and store it in another file:
def reverse_file_content(source_file, destination_file):
    with open(source_file, 'r') as source:
        content = source.read()
    reversed_content = content[::-1]
    with open(destination_file, 'w') as destination:
        destination.write(reversed_content)
source_file = 'sample.txt'  # Replace with your source file name
destination_file = 'destination.txt'  # Replace with your destination file name
reverse_file_content(source_file, destination_file)


#Merge two files into a third file:
def merge_files(file1, file2, merged_file):
    with open(file1, 'r') as f1:
        content1 = f1.read()
    with open(file2, 'r') as f2:
        content2 = f2.read()
    merged_content = content1 + content2
    with open(merged_file, 'w') as merged:
        merged.write(merged_content)
file1 = 'sample.txt'  # Replace with your first file name
file2 = 'sample2.txt'  # Replace with your second file name
merged_file = 'destination.txt'  # Replace with your merged file name
merge_files(file1, file2, merged_file)
