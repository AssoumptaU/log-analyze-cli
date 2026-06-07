# This file ONLY handles Feature 1: Reading a file line by line

def read_log_file_lines(file_path):
    
#    This function opens a file safely and reads it line by line.
#   It takes 'file_path' (the name of the file) as an input.
    
    lines_list = []
    
    with open(file_path, "r") as file:
        for line in file:
            # Clean up the spaces/enters and add each line to our list
            lines_list.append(line.strip())
            
    # return the list of lines back 
    return lines_list