from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer, CharField
from rest_framework.authtoken.models import Token


class CredentialsSerializer(Serializer):
    username = CharField()
    password = CharField()


@api_view(['POST'])
def token(request):
    creds = request.data
    ser = CredentialsSerializer(data=request.data)
    if not ser.is_valid():
        return JsonResponse(ser.errors, status=400)
    payload = ser.validated_data
    user = authenticate(username=payload['username'], password=payload['password'])
    # get token
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse(dict(token=token.key))
    else:
        return JsonResponse(dict(details='no valid user'), status=403)
