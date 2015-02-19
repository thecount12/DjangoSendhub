# Create your views here.
import json
from django.core import serializers
from django.http import HttpResponse 
from jsonschema import validate, ValidationError

def hello_world(request):  
	return HttpResponse("Hello world!") 

def home(request):
	return HttpResponse("blank page")


schema = {
    "title": "Platform Developer Programming Challenge",
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "recipients": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "string", "pattern": "^[0-9]{3}-[0-9]{3}-[0-9]{4}$"},
        }
    },
    "required": ["message", "recipients"]
}

table = {
    'small': {'catname': 'Small', 'subnets': '10.0.1.', 'through': 1, 'cost': 0.01},
    'medium': {'catname': 'Medium', 'subnets': '10.0.2.', 'through': 5, 'cost': 0.05},
    'large': {'catname': 'Large', 'subnets': '10.0.3.', 'through': 10, 'cost': 0.1},
    'super': {'catname': 'Super', 'subnets': '10.0.4.', 'through': 25, 'cost': 0.25},
}

categories = ['super', 'large', 'medium', 'small']
through_dict = {25: 0, 10: 1, 5: 2, 1: 3}
MAXCON = 5000 # up to 5000 recipients

def greed(request):
    '''
    greedy is good
    '''
    #data = request.json
    data2 = json.dumps(request.body)
    sdata=str(data2)
    rdata=sdata.replace("\\","").replace("\"{","'{").replace("}\"","}'")
    #print rdata
    data=eval(rdata)
    data=json.loads(data)
    #data=json.loads(rdata)
   # print data
   # print type(data)
   # print "========="
    try:
        validate(data, schema)
    #except ValidationError:
    #    abort(400)
    except:
	 pass

    recipients = data['recipients'] 
    print recipients
    recipients_num = len(recipients)

    # calculate the routes
    routes = []
    start = 0
    for i in range(len(categories)):
        requests_needed = recipients_num / table[categories[i]]['through']
        if requests_needed > 0:
            for j in range(1, requests_needed + 1):
                ip = table[categories[i]]['subnets'] + str(j)
                end = start + table[categories[i]]['through']
                routes.append({'ip': ip, 'recipients': recipients[start : end]})
                start = end
        recipients_num = recipients_num % table[categories[i]]['through']
#    return jsonify({'message': 'SendHub Rocks', 'routes': routes})
    d={'message': 'SendHub Rocks', 'routes': routes}
    return HttpResponse(json.dumps(d), content_type='application/json') 
    #return response.content
