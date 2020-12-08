#!/usr/bin/python3

import os
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from urllib.request import urlretrieve
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from io import BytesIO
import base64
from imageio import imread
import numpy as np
from tensorflow.keras.optimizers import SGD, Adam
import pickle

from PIL import Image
# iMPORT YOUR LIBRARIES AND CLASSES HERE

app = Flask(__name__)
CORS(app)

# INITIALIZE THE MODEL OVER HEREhsive-hall-288310.appspot.com/o/deep_learning%2Fno_fight%2Fimg183.jpg?alt=media&token=121b4773-8658-4e8b-906f-d3bdd0abeca9
violence_net = load_model('models/violence_detector_model_resnet50_new5')
violence_net.compile(optimizer= Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
le = pickle.loads(open("le.pickle", "rb").read())

@app.route('/')
def violence_detection():
	img_url = request.args.get('url')
	#print("The url is " + img_url)
	if img_url is None:
		b64_url = request.args.get('base64')
		if b64_url is None:
			return []
		# img = imread(base64.b64decode(str(b64_url.split('base64,')[1].replace(' ','+'))))
		# image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		# print(type(image))
		# image = Image.fromarray(image)
		with open("image.jpg", "wb") as fh:
			fh.write(base64.b64decode(b64_url))
		image = load_img('image.jpg', target_size=(224, 224, 3))
		image = img_to_array(image)
		image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
	else:
		urlretrieve(img_url, "image2.jpg")
		image = load_img('image2.jpg', target_size=(224, 224, 3))
		image = img_to_array(image)
		image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

	
	# run your model over "image" and 	 the results into json format
	pred = violence_net.predict(image)[0]
	prediction = np.argmax(pred)
	category = le.classes_[prediction]
	print(category)
	
	return jsonify({"category": category, "accuracy":str(pred[prediction])})


@app.route('/favicon.ico')
def return_nothing():
    return "test2"


if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '3000'))
    except ValueError:
        PORT = 3000
    app.run(HOST, PORT, debug=False)
'''

JSON FORMAT:

{
	"label":"violence"/"non-violence"
	"score":0.95
}



'''