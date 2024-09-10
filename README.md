Undeliverable Email Extractor

This Python script extracts email addresses from .msg files, particularly those that are undeliverable email messages. The script looks for .msg files in a specified directory and attempts to extract the email addresses of recipients who couldn't be delivered to.

Features
Extract Emails from .msg Files: The script is capable of reading Microsoft Outlook .msg files.
Identify Undeliverable Messages: It specifically targets messages starting with 'Undeliverable' in their filenames and parses them.
Extract Failed Recipient Addresses: The script searches for the phrase "Delivery has failed to these recipients or groups" and extracts the email addresses from the line immediately after this phrase.
Requirements
Before running the script, you need to install the following libraries:

extract-msg: To handle .msg file extraction.
re (Regex): To help with the email extraction process.
os: To handle file operations.


You can install extract-msg using pip:
pip install extract-msg

How to Use
Clone the repository:
git clone https://github.com/yourusername/undeliverable-email-extractor.git
cd undeliverable-email-extractor

Place your .msg files: Ensure all the .msg files that need to be processed are placed in a directory.
Update the script: Open the Python script and modify the folder_path variable to point to the directory containing your .msg files.
Example:
folder_path = '/path/to/your/msg/files'

Run the script: Once the script is set up, run it using Python:
python extract_undeliverable_emails.py
Output: The script will output a list of unique email addresses of recipients for whom delivery has failed.

Example Output
['email1@example.com', 'email2@example.com', 'email3@example.com']

Here is a high-level explanation of the code:

Email Extraction: The extract_email function uses a regular expression to search for email addresses within each line of the email body.

Processing .msg Files: The script iterates over each .msg file in the specified directory, looking for files starting with the keyword "Undeliverable".

Searching for Failed Delivery: It looks for a specific message ("Delivery has failed to these recipients or groups") within the body of each message, then extracts the email address from the next line.

Storing Unique Emails: Emails are appended to a list, ensuring there are no duplicates.

Notes
The script assumes the .msg files are undeliverable messages that follow a standard format, which may vary between email systems.
Ensure the directory path is correctly set before running the script.
