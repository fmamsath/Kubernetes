from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/resize', methods=['POST'])
def resize_image():
    file = request.files['image']
    width = int(request.form.get('width', 100))
    height = int(request.form.get('height', 100))

    img = Image.open(file.stream)
    resized_img = img.resize((width, height))

    img_io = io.BytesIO()
    resized_img.save(img_io, 'JPG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)