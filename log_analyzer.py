# We bring in our specialized tools from their separate feature files
from feature1_read_file import read_log_file_lines
from feature2_detect_format import extract_log_details
from feature3_count_log_levels import increment_counter_by_one
from feature4_common_error import track_error_message, find_most_frequent

# Configuration variable: changing this changes the file for the whole project
file_to_open = "app.log"

# FEATURE 3: INITIALIZE COUNTERS
# We start our counter variables at zero before reading any files
total_errors = 0
total_warnings = 0
total_info_messages = 0

# FEATURE 4: INITIALIZE ERROR DICTIONARY
# We start with a completely empty dictionary to track unique error messages
tracked_errors_pool = {}

print("Starting the Log Analyzer ...")

# FEATURE 1: READ THE LOG FILE 
# We hand the file name to Feature 1, and it returns a list of raw string lines
all_log_lines = read_log_file_lines(file_to_open)


# FEATURE 2: DETECT AND EXTRACT FORMAT 
# We loop through our raw lines list and feed each line into the Feature 2 tool
for single_line in all_log_lines:
    
    # Send the raw string line to Feature 2 to turn it into a structured dictionary
    log_details = extract_log_details(single_line)
    
    # Print the clean, formatted output extracted by Feature 2
    print(f"Detected {log_details['format']} -> "
          f"Timestamp: {log_details['timestamp']}, "
          f"Level: {log_details['level']}, "
          f"Message: {log_details['message']}")
    
    # FEATURE 3: INCREMENT COUNTERS (One variable at a time!)
    # We strip the level string to ensure exact matching without hidden spaces
    clean_level = log_details['level'].strip()
    
    if clean_level == "ERROR":
        total_errors = increment_counter_by_one(total_errors)
        
        # FEATURE 4: TRACK ERROR MESSAGES
        # If it's an ERROR, we also want to track its message to count frequencies
        tracked_errors_pool = track_error_message(log_details['message'], tracked_errors_pool)
        
    elif clean_level == "WARNING":
        total_warnings = increment_counter_by_one(total_warnings)
        
    elif clean_level == "INFO":
        total_info_messages = increment_counter_by_one(total_info_messages)


# FEATURE 3: DISPLAY TOTALS
# Now that the loop is completely done, we print the final counter results
print("\n--- Final Log Level Totals ---")
print(f"Errors:   {total_errors}")
print(f"Warnings: {total_warnings}")
print(f"Info:     {total_info_messages}")

# FEATURE 4: DISPLAY MOST COMMON ERROR
# We ask Feature 4 to analyze our dictionary pool and find the highest value key
top_error_message = find_most_frequent(tracked_errors_pool)
print(f"Most frequent error: {top_error_message}")

print("Finished reading the file ")