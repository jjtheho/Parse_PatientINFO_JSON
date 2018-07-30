import json
from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/')

def patientinfo():
    with open('data.json') as f:
        data = json.load(f)
        family_name = data['name'][0]['family'][0]
        given_name = data['name'][0]['given'][0]
        gender = data['gender']
        organization = data['managingOrganization']['display']
        numcond = len(data['conditions'])
        condlst = data['conditions']
        return render_template("fhir.html",
                               fn=family_name,
                               gn=given_name,
                               gdr=gender,
                               org=organization,
                               num=numcond,
                               lst=condlst)


if __name__ == "__main__":
    app.run()
