#fastscore.schema.0: input_schema.avsc

#fastscore.schema.1: output_schema.avsc

import json
import math

print("Starting program", flush=True)

#adding comment 11-12-2021 09:54am MST
#adding comment 11-12-2021 10:01am MST
#adding comment 11-12-2021 10:07am MST
#adding comment 11-12-2021 10:33am MST
#adding comment 11-12-2021 10:43am MST

#modelop.init
def begin():
    global coefs
    coefs = json.load(open('external_file_asset.json', 'r'))
    print("pass", flush=True)
    pass

#modelop.score
def action(datum):
    prediction = compute_prediction(datum)
    print("Can you hear me now?", flush=True)
    yield prediction

def compute_prediction(datum):
    x_score = coefs['x']*datum['x'] 
    y_score = coefs['y']*datum['y'] 
    prediction = x_score + y_score + coefs['intercept']
    return prediction

#modelop.metrics
def metrics(data):
    actuals = data.z.tolist()
    data = data.to_dict(orient='records')
    predictions = list(map(compute_prediction, data))
    diffs = [x[0] - x[1] for x in zip(actuals, predictions)]
    rmse = math.sqrt(sum(list(map(lambda x: x**2, diffs)))/len(diffs))
    mae = sum(list(map(abs, diffs)))/len(diffs)
    yield dict(MAE=mae, RMSE=rmse)

