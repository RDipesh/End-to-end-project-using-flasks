
from flask import Flask,render_template,request
import pandas as pd 
import pickle 
import numpy as np 
import warnings
import sklearn

warnings.filterwarnings("ignore")
 
app=Flask(__name__)
#model=pickle.load(open("rf_model.pkl","rb"))

@app.route("/",methods=["GET"])
def home_fun():
    return render_template("home.html")

@app.route("/predict",methods=["POST"])
def predict():
    Fuel_Type_Diesel=0
    if request.method=="Post":
        Year=int(request.from(["Age"]))
        Age=2023-Year
        Present_Price=float(request.from("Present_Price"))
        Kms_Driven=int(request.from(["Kms_Driven"]))
        Owner=int(request.from(["Owner"]))
        Fuel_Type_Petrol=request.from(["Fuel_Type_Petrol"]):
        if ((Fuel_Type_Petrol)=="Petrol"):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        else: 
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        seller_type_Individual=request.from(["seller_type_Individual"])
        if seller_type_Individual=="Individual":
            seller_type_Individual=1
        else:
            seller_type_Individual=0   
        Transmission_Manul=request.from(["Tranmission_Munal"])
        if Transmission_Manul=="Manual":
            Transmission_Manul=1
        else:
            Transmission_Manul=0




            
                
if __name__=="__main__":
   app.run(debug=True)