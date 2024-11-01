import os

# Specify the directory path here
directory_path = '/'

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)
