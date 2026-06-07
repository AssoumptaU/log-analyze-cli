# We need to tell Python the name of the file we want to open
file_to_open = "app.log"

print("Starting the Log Analyzer ...")

# 'with open' tells Python to unlock and open the file. 
# 'r' means we only want to 'read' the file (not change it).
with open(file_to_open, "r") as file:
    
    # This loop tells Python: "Go through the file, one single line at a time"
    for line in file:
        
        # .strip() removes the invisible 'Enter' key spaces at the end of each line
        clean_line = line.strip()
        
        # Print the line to our terminal screen
        print(clean_line)

print("Finished reading the file!")