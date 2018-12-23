from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .puller import pull_out
import json

@api_view(['POST', 'GET'])
def link_list(request):
    if request.method == 'POST':
        return Response(pull_out(
                            request.data['uri'],
                            int(request.data['depth'])),
                        status=status.HTTP_200_OK)

    if request.method == 'GET':
        lead_to_POST_page = 'You need to send POST requests instead of GET request.'
        return Response('GET request 200 OK', status=status.HTTP_200_OK)
