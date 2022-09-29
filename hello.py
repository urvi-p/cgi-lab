#!/usr/bin/env python3

# This code is from the recorded and in-person labs

import os
import json

# Print env variables as plain text
# print("Content-Type: text/plain")
# print()
# print(os.environ)

# Get all environment variables and put them in a dictionary
env = {}
for env_key, env_value in os.environ.items():
    env[env_key] = env_value

# Print env variables as json
print("Content-Type: application/json")
print()
print(json.dumps(env))

# Print query parameter data in HTML
# print("Content-Type: text/html")
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}<p>")