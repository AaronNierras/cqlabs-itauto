#! /usr/bin/env python3

import os
import requests
import json


feedback_files = os.listdir('/data/feedback')

for file in feedback_files:
    with open(f'/data/feedback/{file}', 'r') as f:
        lines = f.readlines()
        feedback = {
            "title": lines[0].strip(),
            "name": lines[1].strip(),
            "date": lines[2].strip(),
            "feedback": ''.join(lines[3:]).strip()
        }
        header_content = {'Content-type': 'application/json'} 
        assert isinstance(feedback, dict)
        feedback = json.dumps(feedback)
        print(">>> feedback: \n", feedback, "\n")
        response = requests.post(url="http://35.229.79.83/feedback", json=feedback, headers=header_content, verify=False)
        # Check if the POST request was successful
        if response.status_code == 201:
            print(">>> Feedback uploaded successfully!")
        else:
            print(f">>> Error uploading feedback: {response.status_code}")