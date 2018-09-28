from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def data_view(request):
    if not request.user.is_authenticated:
        return JsonResponse(dict(details="no auth"), status=403)

    # save to pull
    # find pair
    # links
    # wait for pull (we are ready?) and return battle info

    payload = dict(data='one')
    return JsonResponse(payload)

@api_views(['GET'])
def battle_wait(request):
    pass
