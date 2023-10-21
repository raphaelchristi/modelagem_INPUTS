import datetime

# Define the global log file path
log_file = "recognizeINPUT.log"

def trace_msg(msg_to_log):
    # Get the current timestamp
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("[%d/%m/%Y %H:%M:%S]")

    # Construct the log message
    log_message = f"{timestamp}: {msg_to_log}\n"

    # Append the log message to the log file
    with open(log_file, 'a') as file:
        file.write(log_message)

# Example usage:
# trace_msg(msg)