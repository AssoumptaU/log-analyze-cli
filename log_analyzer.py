import json

file_to_open = "app.log"

print("--- Starting the Log Analyzer ---")

with open(file_to_open, "r") as file:
    for line in file:
        clean_line = line.strip()
        
        # --- FEATURE 2: DETECT FORMAT ---
        try:
            # Parse the line into a dictionary
            structured_json_data = json.loads(clean_line)
            
            # Extract all THREE required fields 
            log_timestamp = structured_json_data['timestamp']
            log_level = structured_json_data['level']
            log_message = structured_json_data['message']
            
            # Print all three extracted fields clearly
            print(f"Detected JSON Format -> Timestamp: {log_timestamp}, Level: {log_level}, Message: {log_message}")
            
        except json.JSONDecodeError:
            # If it's not JSON, it's a plain text line
            print(f"Detected Plain Text Format -> {clean_line}")

print("--- Finished reading the file ---")