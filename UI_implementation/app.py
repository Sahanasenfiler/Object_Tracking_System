from flask import Flask, request, jsonify
import os
from obj_det import detect_objects  # Import your object detection script for images
from od_yolo_tiny_w import detect_objects_tiny  # Import your YOLO Tiny detection script for videos
from tracking import track_objects  # Import your tracking script for YOLOv4 video tracking
import torch
from PIL import Image

app = Flask(__name__)
# Ensure the directory exists for uploads
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return "Object Tracking System API"

@app.route('/process', methods=['POST'])
def process_file():
    input_type = request.form['input_type']
    model_name = request.form['model']
    file = request.files['file']

    if not file:
        return jsonify({"message": "No file uploaded!"}), 400
    
    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    try:
        # Process image with YOLOv8s
        if input_type == 'image' and model_name == 'yolov8s':
            result_message = detect_objects(file_path)  # Call the detect_objects function from obj_det.py

        # Process video with YOLOv4 (tracking)
        elif input_type == 'video' and model_name == 'yolov4':
            result_message = track_objects(file_path)  # Call the track_objects function from tracking.py

        # Process video with YOLO Tiny (object detection)
        elif input_type == 'video' and model_name == 'od_yolo_tiny_w':
            result_message = detect_objects_tiny(file_path)  # Call from od_tiny_yolo_w.py

        else:
            result_message = "Unsupported input or model"

        return jsonify({"message": result_message})

    except Exception as e:
        return jsonify({"message": f"Error processing file: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

