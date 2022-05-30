import json
from types import NoneType
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



# connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


@api_view(['GET'])
def check_multiples(request):
    if request.method == 'GET':
        if request.data.get('integer') is None or request.data.get('integer') == '':
            response = {
                'error': 'Please provide a number to check'
            }
            return Response(response, status=400)
        elif type(request.data.get('integer')) is not int:
            response = {
                'error': 'Please provide a valid number to check'
            }
            return Response(response, status=400)
        else:
            number_to_check = int(request.data.get('integer'))

            if number_to_check:
                value = redis_instance.get(number_to_check)
                if value:
                    response = {
                        'result': value
                    }
                    return Response(response, status=200)
                else:
                    if number_to_check % 5 == 0 and number_to_check % 7 == 0:
                        response = {
                        'result': 'LR'
                        }
                        redis_instance.set(number_to_check, 'LR')
                        return Response(response, status=200)
                    elif number_to_check % 5 == 0:
                        response = {
                            'result': 'L'
                        }
                        redis_instance.set(number_to_check, 'L')
                        return Response(response, status=200)
                    elif number_to_check % 7 == 0:
                        response = {
                            'result': 'R'
                        }
                        redis_instance.set(number_to_check, 'R')
                        return Response(response, status=200)
                    else:
                        response = {
                            'result': number_to_check
                        }
                        return Response(response, status=200)
            elif not number_to_check:
                response = {
                    'error': 'Please provide a number to check'
                }
                return Response(response, status=400)
            else:
                response = {
                    'error': 'Please provide a number to check'
                }
                return Response(response, status=400)

