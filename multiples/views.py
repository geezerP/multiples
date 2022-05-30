import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



# connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


@api_view(['GET'])
def check_multiples(request, *args, **kwargs):
    # mock response to what will be implemented when extracting the integer from the request
    response = {
        'status': 'success',
    }
    return Response(response, status=200)

