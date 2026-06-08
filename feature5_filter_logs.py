from datetime import datetime

def setup_cli_arguments():
#This function sets up the allowed terminal flags (--level, --from, --to).
#It parses whatever the user typed in the terminal.
    import argparse
    
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Filters")
    
    # We define our optional filters
    parser.add_argument("--level", type=str, help="Filter logs by level (ERROR, WARNING, INFO)")
    parser.add_argument("--from-time", dest="from_time", type=str, help="Start time format: YYYY-MM-DD HH:MM")
    parser.add_argument("--to-time", dest="to_time", type=str, help="End time format: YYYY-MM-DD HH:MM")
    parser.add_argument("-export", dest="export_file", type=str, help="Export summary to a CSV file")
    
    # Python gathers them all up into a clean object
    return parser.parse_args()


def is_line_matching_filters(log_details, arguments):
    
#This function checks a single log line against our user filters.
#Returns True if the line passes the filters, False if it should be skipped.
    
    # 1. LEVEL FILTER CHECK
    if arguments.level:
        # If the user requested a specific level, and this line doesn't match, skip it!
        if log_details['level'].strip() != arguments.level.strip():
            return False

    # 2. TIME RANGE FILTER CHECK
    # We convert the log's string timestamp into an actual datetime object for comparison
    try:
        # Our logs look like '2026-01-15 10:03:22', so we parse with seconds (%S)
        log_time_obj = datetime.strptime(log_details['timestamp'].strip(), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        # If the timestamp format is weird, we skip time filtering for safety
        return True

    # Check the '--from-time' boundary
    if arguments.from_time:
        from_obj = datetime.strptime(arguments.from_time.strip(), "%Y-%m-%d %H:%M")
        if log_time_obj < from_obj:
            return False

    # Check the '--to-time' boundary
    if arguments.to_time:
        to_obj = datetime.strptime(arguments.to_time.strip(), "%Y-%m-%d %H:%M")
        if log_time_obj > to_obj:
            return False

    # If it didn't fail any of the active checks, it's a match!
    return True