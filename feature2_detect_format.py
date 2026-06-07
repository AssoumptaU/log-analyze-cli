import json

def extract_log_details(single_line):

#This function takes a single line of text, detects its format,
#and returns a dictionary containing: timestamp, level, and message.
    
    try:
        # Try to parse the line as JSON
        structured_json_data = json.loads(single_line)
        
        return {
            "timestamp": structured_json_data["timestamp"],
            "level": structured_json_data["level"],
            "message": structured_json_data["message"],
            "format": "JSON"
        }
        
    except json.JSONDecodeError:
        # Fallback for Plain Text if JSON fails
        # Split by spaces, max 3 splits to keep the message together
        split_line = single_line.split(" ", 3)
        
        log_date = split_line[0]
        log_time = split_line[1]
        log_level = split_line[2]
        log_message = split_line[3]
        
        return {
            "timestamp": f"{log_date} {log_time}",
            "level": log_level,
            "message": log_message,
            "format": "Plain Text"
        }