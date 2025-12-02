from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
import tensorflow as tf
from PIL import Image
import numpy as np
import io
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input

categories = ['unripe', 'ripe', 'overripe', 'rotten']

categories.sort()
print(categories)

try:
    model = tf.keras.models.load_model('../banana/images.keras')
    print("Model loaded successfully!")
except Exception as e:
    print(f'model not loaded {e}')
    model = None


def classify_image(image_file):

    img = Image.open(io.BytesIO(image_file))
    img.load()

    img = img.resize((224, 224), Image.LANCZOS)

    x = image.img_to_array(img)

    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x)
    print(x.shape)
    pred = model.predict(x)

    category_value = np.argmax(pred, axis=1)
    print(category_value)

    category_value = category_value[0]

    result = categories[category_value]

    return result


app = FastAPI()


@app.post("/api/process-image")
async def create_upload_file(file: UploadFile):
    if model is None:
        return {'error': 'model not added'}
    test = await file.read()
    help = classify_image(test)
    print('hello')
    return {"ripeness_level": help}


@app.get("/")
async def index():
    return FileResponse("../banana/static/index.html")
