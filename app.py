from flask import Flask, render_template, request, redirect, jsonify
import json
import requests
app = Flask(__name__)
s = ""
j = {"data": ""}


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":

        return render_template("index.html")
    else:

        x = request.form.get("creditscore")
        s = str(x)
        x = request.form.get("geography")
        s = s+","+str(x)
        x = request.form.get("gender")
        s = s+","+str(x)
        x = request.form.get("age")
        s = s+","+str(x)
        x = request.form.get("tenure")
        s = s+","+str(x)
        x = request.form.get("balance")
        s = s+","+str(x)
        x = request.form.get("products")
        s = s+","+str(x)
        x = request.form.get("hascredit")
        s = s+","+str(x)
        x = request.form.get("activemember")
        s = s+","+str(x)
        x = request.form.get("salary")
        s = s+","+str(x)

        print(s)
        j = {"data": s}
        print(type(j))
        print(j)

        j = json.dumps(j, indent=4)
        headers = {
            'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
            'X-Amz-Date': '20201119T073602Z',
            'Authorization': 'AWS4-HMAC-SHA256 Credential=AKIA4GBBQNNS2B2YLV2K/20201119/us-east-2/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=5200ecbe3c04c6bad217594cba67df08159bc91b36df9058b45e271314617cec',
            'Content-Type': 'text/plain'
        }
        r = requests.post(
            'https://l0qbgio5tf.execute-api.us-east-1.amazonaws.com/test', headers=headers, data=j)
        print(r)
        if r.text == '1':
            res = "Yes, the customer is likely to leave"
        else:
            res = "No, the customer is unlikely to leave"
        print(r.text)
        return render_template("predict.html", res=res)


if __name__ == '__main__':
    app.run(debug=True)
