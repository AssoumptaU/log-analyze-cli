# We bring in our specialized tools from their separate feature files
from feature1_read_file import read_log_file_lines
from feature2_detect_format import extract_log_details
from feature3_count_log_levels import increment_counter_by_one
from feature4_common_error import track_error_message, find_most_frequent
from feature5_filter_logs import setup_cli_arguments, is_line_matching_filters
from feature6_export_csv import record_failure_timestamp, export_summary_to_csv

# FEATURE 5: PARSE TERMINAL ARGUMENTS
cli_args = setup_cli_arguments()

# Configuration variable
file_to_open = "app.log"

# COUNTERS
total_logs = 0
total_errors = 0
total_warnings = 0
total_info_messages = 0
tracked_errors_pool = {}

# FEATURE 6: INITIALIZE TIMESTAMPS LIST
failure_timestamps_pool = []

print("Starting the Log Analyzer ...")

# FEATURE 1: READ THE LOG FILE 
all_log_lines = read_log_file_lines(file_to_open)


# PROCESSING LOOP
for single_line in all_log_lines:
    
    # Send raw line to Feature 2 to turn it into a structured dictionary
    log_details = extract_log_details(single_line)

    # FEATURE 5: FILTER CHECK
    if not is_line_matching_filters(log_details, cli_args):
        continue 
    
    total_logs = total_logs + 1
    
    # Print the clean, formatted output extracted by Feature 2
    print(f"Detected {log_details['format']} -> "
          f"Timestamp: {log_details['timestamp']}, "
          f"Level: {log_details['level']}, "
          f"Message: {log_details['message']}")
    
    # FEATURE 3: INCREMENT COUNTERS
    clean_level = log_details['level'].strip()
    
    if clean_level == "ERROR":
        total_errors = increment_counter_by_one(total_errors)
        tracked_errors_pool = track_error_message(log_details['message'], tracked_errors_pool)
        
        # FEATURE 6: COLLECT TIMESTAMPS
        failure_timestamps_pool = record_failure_timestamp(log_details['timestamp'], failure_timestamps_pool)
        
    elif clean_level == "WARNING":
        total_warnings = increment_counter_by_one(total_warnings)
        
    elif clean_level == "INFO":
        total_info_messages = increment_counter_by_one(total_info_messages)


# FINAL LOG ANALYSIS SUMMARY
print("\n--- Final Log Analysis Summary ---")
print(f"Total logs:           {total_logs}")
print(f"Errors:               {total_errors}")
print(f"Warnings:             {total_warnings}")
print(f"Info:                 {total_info_messages}")

# FEATURE 4: DISPLAY MOST COMMON ERROR
top_error_message = find_most_frequent(tracked_errors_pool)
print(f"Most frequent error:  \"{top_error_message}\"")

# FEATURE 6: DISPLAY FAILURE TIMESTAMPS
# .join() turns our list ['10:03:22', '10:06:00'] into a single string '10:03:22, 10:06:00'
timestamps_string = ", ".join(failure_timestamps_pool)
print(f"Failure timestamps:   {timestamps_string} ...")

print("Finished reading the file ")


# FEATURE 6: CSV EXPORT CHECK
# If the user passed the -export flag in the terminal, trigger the export machine
if cli_args.export_file:
    export_summary_to_csv(
        cli_args.export_file, 
        total_logs, 
        total_errors, 
        total_warnings, 
        total_info_messages, 
        top_error_message
    )