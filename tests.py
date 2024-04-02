import requests


def call_upload_pdf(path):
    url = "http://127.0.0.1:5000/uploadpdf"  # replace with your Flask app's URL



    with open(path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
    print(response.status_code)
    print(response.text)
    return response


resp = call_upload_pdf("AW.pdf")
print(resp)