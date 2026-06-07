#We IMPORT the specific function from our Feature 1 file
from feature1_read_file import read_log_file_lines
# Import the Feature 2 tool
from feature2_detect_format import extract_log_details

file_to_open = "app.log"

print("--- Starting the Log Analyzer ---")

# 2. We USE the Feature 1 tool to get all our lines
all_log_lines = read_log_file_lines(file_to_open)

# 3. For now, let's just print them to prove it worked!
for single_line in all_log_lines:
    print(f"Feature 1 Read: {single_line}")

print("--- Finished reading the file ---")