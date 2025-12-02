🍌 Banana Ripeness Classification System

This project shows how a small model can guess the ripeness level of a banana from a picture. It uses TensorFlow with a MobileNet V2 base and runs through a FastAPI service. The web page is built with HTML and JavaScript. You can run the full setup with Docker.

📷 How I Collected the Data

I took pictures of bananas I bought from the store for fifteen days. Then I resized the images for MobileNet V2 and used data augmentation to create more samples so the model would not overfit.

I split the data into train and validation groups and sorted them into five classes

* ripe

* unripe

* overripe

* rotten

* not banana

🧠 How the Model Was Built

I used transfer learning by freezing the base model so its weights would stay the same.
Then I added three simple layers on top and trained them with my data.
After that I fine tuned the model for better results and tested a few versions to pick the best one.

🌐 App Features

Image upload and camera capture

Real time prediction through FastAPI

Simple front end with HTML and JavaScript

Easy setup with Docker and Docker Compose

⚙️ How It Works

The FastAPI service loads the trained model and takes an image from the user.
It prepares the image and sends back the predicted class.
The web page shows the result right away.
I plan to place this on my site so anyone can try it with Docker.

🛠️ Tech Used

TensorFlow
ImageNet V2
FastAPI
JavaScript
Python
Docker
Docker Compose

🔗 Links

GitHub and live demo will be added soon.