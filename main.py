# app.py
from flask import Flask, request, send_file
from pdf2docx import Converter
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    pdf = request.files['file']
    pdf_path = 'input.pdf'
    docx_path = 'output.docx'

    pdf.save(pdf_path)

    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

    return send_file(docx_path, as_attachment=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
