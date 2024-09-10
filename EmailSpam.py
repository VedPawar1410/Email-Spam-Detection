import re
import os
import extract_msg
from extract_msg import Message

# Function to extract email from a line using regex
def extract_email(nline):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    match = re.search(email_pattern, nline)
    if match:
        return match.group()
    return None

# List to store email ids
email_list = []

# Directory containing .msg files
folder_path = '# The directory containing .msg files'

# Loop through .msg files in the directory
for filename in os.listdir(folder_path):
    if filename.endswith('.msg') and filename.startswith('Undeliverable'):
        #with open(os.path.join(folder_path, filename), 'r', errors='ignore') as file:
        #with os.scandir(folder_path)as files:
            #files = os.scandir(folder_path)
        for file in folder_path:
            with extract_msg.Message(file) as msg:
                msg_body = msg.body
                #with open(msg, 'r') as s:
                for line in msg_body:
                    if 'Delivery has failed to these recipients or groups' in line:
                        next_line = next(msg_body)
                        email = extract_email(next_line)
                        if email and email not in email_list:
                            email_list.append(email)

print(email_list)