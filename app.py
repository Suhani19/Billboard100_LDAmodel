from flask import Flask,request,render_template,redirect
import jsonify
import requests
import pickle
model = pickle.load(open("lda_model.pkl","rb"))
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict",methods = ['POST'])
def predict():
    if request.method == "POST":
        
        data1= (request.form["danceability "])
        data2= (request.form["energy "])
        data3= (request.form["loudness "])
        data4= (request.form["speechiness "])
        data5= (request.form["acoustiness "])
        data6= (request.form["instrumentalness "])
        data7= (request.form["liveness "])
        data8= (request.form["valence "])
        data9= (request.form["tempo "])
        data10= float(request.form["genre "])
        list_res = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]   
        pred = model.predict([list_res])
        if(pred == 1):
            res = "THE SONG IS GOING TO HIT THE BILLBOARD HOT100 LIST"
        else:
            res = "THE SONG IS NOT GOING TO HIT THE BILLBOARD HOT100 LIST"
        return render_template('index.html',result = res)

   

if  __name__ == '__main__':
    app.run(debug = True)