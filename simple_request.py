# USAGE
# python simple_request.py

# import the necessary packages
import requests
from datetime import datetime

print("simple_request Start",datetime.now())

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://localhost:5000/predict"
IMAGE_PATH = "dog.jpg"

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

print("simple_request Image prepared",datetime.now())

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()

print("simple_request Request send",datetime.now())

# ensure the request was sucessful
if r["success"]:
	# loop over the predictions and display them
	for (i, result) in enumerate(r["predictions"]):
		print("{}. {}: {:.4f}".format(i + 1, result["label"],
			result["probability"]))
# otherwise, the request failed
else:
	print("Request failed")
    
print("simple_request Completed",datetime.now())
