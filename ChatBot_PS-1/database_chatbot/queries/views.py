from django.contrib.auth.models import User                               
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from queries.serializers import  query1Serializer # Our Serializer Classes
from rest_framework.decorators import api_view
from .nlp_module import nlp_module
#from nlp_module import respond (not needed)
from .response_generator_1 import response_generation
import json


nlp_out = nlp_module()

@api_view(['GET', 'POST'])
@csrf_exempt                         
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    
    Args:
        request(Json): Contains the JSON of the user input
        sender:To store the id of the sender, default = None
        receiver : To store the id of the reciever, default = None
    Returns:
        body(dictionary): Returned as JSON to the frontend using JsonResponse subclass
    """
    if request.method == 'POST':
        print(request.body)
        var=json.loads(request.body) #converts from JSON and stores user input as a dictionary
        input_question=var["messages"] 
        nlp_output = nlp_out.respond(input_question) #calls nlp engine 
        final_out = response_generation(nlp_output, input_question) #calls the response generator and stores final response
        body = {"message": final_out}
        return JsonResponse(body, status=200) #returns response to frontend
