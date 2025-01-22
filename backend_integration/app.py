from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_file():
    # Check if a file is in the request
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400

    # Get file and form data
    file = request.files['file']
    input_type = request.form.get('input_type')
    model = request.form.get('model')

    # Validate inputs
    if not file or input_type not in ['image', 'video'] or model not in ['yolov8s', 'yolov4']:
        return jsonify({'message': 'Invalid input data'}), 400

    # Process logic based on inputs
    if input_type == 'image' and model == 'yolov8s':
        result = "Image processed with YOLOv8s."
    elif input_type == 'video' and model == 'yolov4':
        result = "Video processed with YOLOv4."
    elif input_type == 'video':
        result = "Video processed with YOLO tiny model."
    else:
        result = "Unsupported combination."

    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True)
