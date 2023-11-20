import pickle
import datetime
import base64
data = {}
data ['current'] = str(datetime.datetime.now())
data['people'] = ["Ahmad", "Rezaei"]
pickle_data = pickle.dumps(data)
print(pickle_data)
with open('my.data', 'wb') as file:
    file.write(base64.b64encode(pickle_data))