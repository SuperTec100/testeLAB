from flask import Flask, request, render_template
import fitz  # PyMuPDF
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    if request.method == "POST":
        file = request.files["pdf"]
        if file and file.filename.endswith(".pdf"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            with fitz.open(filepath) as doc:
                text = "\n".join(page.get_text() for page in doc)
    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
