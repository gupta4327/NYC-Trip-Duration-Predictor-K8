from flask import Flask, render_template, request
import requests
from logger import infologger


app = Flask(__name__)


@app.route('/')
def index():
    
    try:
        return render_template('index.html')
    
    except Exception as e:
         infologger.info(f'Home page has not been loaded : {e}')

@app.route('/predict', methods=['POST'])
def predict():

    form_data = dict()
    form_data['vendor_id'] = request.form.get('vendor_id', type=int)
    form_data['pickup_latitude'] = request.form.get('pickup_latitude',type=float)
    form_data['pickup_longitude'] = request.form.get('pickup_longitude',type=float)
    form_data['dropoff_latitude'] = request.form.get('dropoff_latitude',type=float)
    form_data['dropoff_longitude'] = request.form.get('dropoff_longitude',type=float)
    form_data['pickup_datetime'] = request.form.get('pickup_datetime')
    form_data['store_and_fwd_flag'] = request.form.get('store_and_fwd_flag')
    try:
        duration = requests.get("""http://ml_service:8082/api/trip_predictor?
                                vendor_id={}&pickup_latitude={}&pickup_longitude={}
                                &dropoff_latitude={}&dropoff_longitude={}
                                &pickup_datetime={}&store_and_fwd_flag={}""".format( form_data['vendor_id'], 
                                                                                     form_data['pickup_latitude'],
                                                                                     form_data['pickup_longitude'],
                                                                                     form_data['dropoff_latitude'],
                                                                                     form_data['dropoff_longitude'],
                                                                                     form_data['pickup_datetime'] ,
                                                                                     form_data['store_and_fwd_flag']))

        
        print(duration)
        duration = duration.json()
        
        duration = duration['pred_time']

        return render_template('predict.html',pred_time = duration)
    
    except Exception as e:
        
         infologger.info(f'Failed with error : {e}')


if __name__ == "__main__":
     
     try:
         app.run(host='0.0.0.0',port=8080, debug=True)
         
         
     except Exception as e:
       infologger.info(f'Application failure : {e}')		
