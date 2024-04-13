import requests


def call_upload_pdf(path):
    url = "https://abridgedbook-api.onrender.com/uploadpdf"  # replace with your Flask app's URL

    # prepare headers for http request
    headers = {
        "Content-Type": "application/pdf",
    }

    with open(path, "rb") as f:
        response = requests.post(url, files={"file": f})
    print(response.status_code)
    print(response.text)
    return response


resp = call_upload_pdf('C:/Users/hongy/Documents/Work/Knowledgebase/refine/AW/AW.pdf')
print(resp)