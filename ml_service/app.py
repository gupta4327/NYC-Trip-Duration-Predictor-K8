from flask import Flask, jsonify, request
from predictor import TripDurationPredictor
from logger import infologger

app = Flask(__name__)

@app.route('/')
def index():

    return "Hello world"


@app.route('/api/trip_predictor')
def predict():

    form_data = dict()
    form_data['vendor_id'] = request.args.get('vendor_id', type=int)
    form_data['pickup_latitude'] = request.args.get('pickup_latitude',type=float)
    form_data['pickup_longitude'] = request.args.get('pickup_longitude',type=float)
    form_data['dropoff_latitude'] = request.args.get('dropoff_latitude',type=float)
    form_data['dropoff_longitude'] = request.args.get('dropoff_longitude',type=float)
    form_data['pickup_datetime'] = request.args.get('pickup_datetime')
    form_data['store_and_fwd_flag'] = request.args.get('store_and_fwd_flag')
    try:
        duration = TripDurationPredictor()
        pred = duration.predict_duration(form_data)[0].item()
        pred_time = round(pred/60,2)
        return jsonify({'pred_time':pred_time})
    
    except Exception as e:
         infologger.info(f'Failed with error : {e}')
         print(f'Failed with error : {e}')


if __name__ == "__main__":
     
     try:
         app.run(host='0.0.0.0',port=8082)
         
         
     except Exception as e:
        infologger.info(f'Application failure : {e}')		
