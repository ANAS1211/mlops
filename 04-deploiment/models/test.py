import predict
import requests
ride ={
"PULocationID": 10,
"DOLocation": 50 ,
"trip_distance": 40
    
}

url= "localhost:9696/predict"
response= requests.post(url,json=ride)
print(response.json())
features= predict.prepare_features(ride)
pred=predict.predict(ride)
print(pred)