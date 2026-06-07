# This file ONLY handles Feature 4: Finding the most common error message

def track_error_message(message_text, error_dictionary):
    """
    This function takes an error message and our dictionary of tracked errors.
    It cleans the message text, updates the count, and returns the updated dictionary.
    """
    # Clean up any hidden newlines (\n) or trailing spaces from the text
    clean_message = message_text.strip()
    
    # Check if this specific error message is already a key in our dictionary
    if clean_message in error_dictionary:
        # If it exists, add 1 to its current value
        error_dictionary[clean_message] = error_dictionary[clean_message] + 1
    else:
        # If it is brand new, create the key and start it at 1
        error_dictionary[clean_message] = 1
        
    return error_dictionary


def find_most_frequent(error_dictionary):
    """
    This function looks at our completed dictionary and uses max() 
    to find which error message key has the highest count value.
    """
    # If the dictionary is completely empty (no errors found at all)
    if not error_dictionary:
        return "No errors found"
        
    # max() goes through the dictionary keys and uses the .get method 
    # to find which key has the highest number value attached to it.
    most_common_key = max(error_dictionary, key=error_dictionary.get)
    
    return most_common_key