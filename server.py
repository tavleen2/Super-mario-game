from flask import Flask, request, render_template_string
import os
from datetime import datetime
from uuid import uuid4

app = Flask(__name__)

# Folder where screenshots will be stored
UPLOAD_FOLDER = os.path.join('static', 'screenshots')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/screenshot', methods=['POST'])
def upload_screenshot():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Give each file a UNIQUE name (timestamp + random id)
    unique_name = (
        datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        + "_" + str(uuid4())[:8]
        + ".png"
    )

    save_path = os.path.join(UPLOAD_FOLDER, unique_name)
    file.save(save_path)
    print(f"Screenshot saved as {save_path}")  # Debug print
    return "File successfully uploaded", 200


@app.route('/')
def index():
    # List all files in the screenshots folder
    files = sorted(os.listdir(UPLOAD_FOLDER))

    # Simple HTML gallery
    html = """
    <html>
    <head><title>Screenshots</title></head>
    <body>
      <h1>Screenshots</h1>
      {% if files %}
        {% for f in files %}
          <div style="margin-bottom: 10px;">
            <img src="{{ url_for('static', filename='screenshots/' + f) }}" width="300">
          </div>
        {% endfor %}
      {% else %}
        <p>No screenshots yet.</p>
      {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, files=files)


if __name__ == '__main__':
    app.run(port=5000)
