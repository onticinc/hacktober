
import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):

    body = request.body #byte string of JSON data
    data = {}
    try: 
        data = json.loads(body) # string of JSON data -> Python Dictionary
    except:
        pass
    print(data.keys())



    return JsonResponse(data)