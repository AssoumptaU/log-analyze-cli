import csv

def record_failure_timestamp(timestamp_text, timestamp_list):
    """
    This function takes a timestamp string, extracts just the time portion,
    and appends it to our tracker list.
    """
    # Our logs look like '2026-01-15 10:03:22'. 
    # We use split(" ") to separate the date from the time, and take the time part [1]
    time_only = timestamp_text.strip().split(" ")[1]
    timestamp_list.append(time_only)
    return timestamp_list


def export_summary_to_csv(filename, total, errors, warnings, info, top_error):
    """
    This function creates a brand new CSV file and writes our metrics
    using the exact row structure required by the instructor.
    """
    # Open the file in write mode ('w') with clean line endings
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the column headers exactly as expected
        writer.writerow(["metric", "value"])
        
        # Write individual rows for each metric
        writer.writerow(["total_logs", total])
        writer.writerow(["errors", errors])
        writer.writerow(["warnings", warnings])
        writer.writerow(["info", info])
        writer.writerow(["most_common_error", top_error])
        
    print(f" Successfully exported summary data to {filename}")