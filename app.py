from flask import Flask, render_template, request
import os
from nlp_engine import extract_text_from_pdf, get_frequent_tags, get_important_tags

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    frequent_tags = []
    important_tags = []
    file_name = ""
    message = ""
    advice = ""

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename:
            file_name = file.filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            text = extract_text_from_pdf(filepath)

            if text.strip():
                frequent_tags = get_frequent_tags(text)
                important_tags = get_important_tags(text)
                message = "Tags generated successfully."

                if important_tags:
                    advice = (
                        f"This research paper mainly focuses on {important_tags[0]}. "
                        f"It is recommended to explore related topics like "
                        f"{', '.join(important_tags[:3])} for better understanding."
                    )
            else:
                message = "No readable text was found in the PDF."
        else:
            message = "Please choose a PDF file."

    return render_template(
        "index.html",
        frequent_tags=frequent_tags,
        important_tags=important_tags,
        file_name=file_name,
        message=message,
        advice=advice
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)