#! /usr/bin/env python3

import os, requests, json, sys

# fb_dir = sys.argv[1] if len(sys.argv) > 1 else "/data/feedback"
# server_url = sys.argv[2] if len(sys.argv) > 2 else "http://35.229.79.83/feedback"
fb_dir = "/data/feedback"
server_url = "http://35.229.79.83/feedback"


# Check files from directory
def check_files():
    """Checks the default directory, if none given as a parameter, if it exists."""

    print(">>> Checking directory: '{}'".format(fb_dir))
    if os.path.isdir(fb_dir):
        print(">>> Directory exists...")
        files = os.listdir(fb_dir)
        return files
    else:
        print(">>> Directory does not exist")


# Open all text files
def open_file(infile):
    """Open the file from the directory then convert into a dictionary."""

    try:
        print(">>> Opening {}.".format(infile))
        with open(os.path.join(fb_dir, infile), "r") as file:
            # Convert text to dictionary
            template = {
                "title": infile[0].strip(), 
                "name": infile[1].strip(), 
                "date": infile[2].strip(), 
                "feedback": "".join(infile[3:]).strip()
                }
    except FileNotFoundError:
        print(">>> File not found")
    
    return template


# Send dictionary to server
def send_to_server(feedback):
    """Send the feedback to the server."""

    # Check Response Code
    response = requests.get(server_url)
    assert response.status_code == 200

    # header_content = {'Content-type': 'application/json'} 
    print(">>> New Feedback : ", feedback)
    assert isinstance(feedback, dict)
    print(">>> server : ", server_url)
    response = requests.post(url=server_url, json=feedback) #, headers=header_content, verify=False)
    print(">>> Response Code: ", response.status_code)
    # Check if the POST request was successful
    if response.status_code == 201:
        print(">>> Feedback uploaded successfully!")    
    else:
        print(f">>> Error uploading feedback: {response.status_code}")


def main() -> None:
    print(">>> Url: '{}'".format(server_url))
    file_list = check_files()
    if file_list is None:
        print("Cannot find file list.")
        exit(1)
    for infile in file_list:
        feedback = open_file(infile)
        send_to_server(feedback)
    print(">>> [DONE] Feedbacks sent to server.")



if __name__ == "__main__":
    main()