from flask import Flask,render_template,request,url_for
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello():
    if request.method=='POST':
        cs=request.form['a']
        geo=request.form['r2']
        gen=request.form['r1']
        age=request.form['b']
        tenure=request.form['c']
        balance=request.form['d']
        np=request.form['e']
        hc=request.form['r3']
        im=request.form['r4']
        es=request.form['f']
        try:
            cs=int(cs)
            geo=int(geo)
            gen=int(gen)
            age=int(age)
            tenure=int(tenure)
            balance=float(balance)
            np=int(np)
            hc=int(hc)
            im=int(im)
            es=float(es)
        except:
            return render_template('data.html',err_msg='Enter Valid Data')
        url = " https://gwc4o0irzj.execute-api.ap-south-1.amazonaws.com/test"
        payload = " {\"data\":\"" + str(cs) + ',' + str(geo) + ',' + str(gen) + ',' + str(age) + ',' + str(tenure) + ',' + str(balance) + ',' + str(np) +','+str(hc)+ ','+str(im)+',' + str(es) + "\"" + "}"

        headers = {
             'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
             'X-Amz-Date': '20201123T083338Z',
             'Authorization': 'AWS4-HMAC-SHA256 Credential=AKIA4GBBQNNS2B2YLV2K/20201123/us-east-2/execute-api/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=fa2d8dc5ed30cfa0a88c96caf9035b2a59fa147cc95aeb968c258b21d1282268',
             'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response=response.text.encode('utf8')
        response=str(response)
        print(response)
        result=response[3]
        print(result)
        if result=='N':
            return render_template('data.html',result='Not Likely to Leave')
        else:
            return render_template('data.html',result='Likely To Leave')
    else:
        return render_template('data.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
