from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect
from rest_framework.decorators import api_view

from rest_framework.generics import get_object_or_404

from game.models import Battle
from game.serializers import SERIALIZER_CASE

poll = defaultdict(list)


@api_view(['POST'])
@login_required
def search_battle(request):
    """
    Регистрация в битве
    :param request: запрос
    :return: урл для пулинга
    """
    user = request.user
    level = user.level
    poll[level].append(user)
    payload = dict(pull_url=reverse('pull-battle'))
    return JsonResponse(payload)


@api_view(['GET'])
@login_required
def battle_wait(request):
    """
    Ищем зарегистрированных игроков, если есть пара - сообщаем им уникальный
    урл их битвы и выкидываем их из списка ищущих битвы
    """
    user = request.user
    level = user.level
    users = poll[level]
    if user not in users:
        return JsonResponse(dict(detail='you are not registered in search'),
                            status=400)
    # remove first pair
    poll[level] = users[2:]

    new_battle = Battle.objects.create(player1=users[0], palyer2=users[1])
    return redirect(reverse('battle', id=new_battle.id))


@api_view(['POST'])
@login_required
def battle_view(request, id):
    """
    Принимает действия игроков и запоминает и изменяет состояния игроков в зависимости от действий.
    :param request: запрос
    :param id: идентификатор битвы
    :return: Урл для пулинга
    """

    battle = get_object_or_404(Battle, id=id)
    data = request.data
    if not isinstance(data.get('type'), str):
        return JsonResponse(details='type should be a string')
    serializer = SERIALIZER_CASE[type]
    ser = serializer(data=data.get('payload'))
    if ser.is_valid():
        object = ser.validated_data
        print(object)
        return JsonResponse(data=True)
    else:
        return JsonResponse(ser.errors, 400)


@api_view(['GET'])
@login_required
def battle_pull(request, id):
    """
    суда приходятзапросы ожидания результатов каждого хода в битве с идентификатором uuid
    :param request: запрос
    :param id: идентификатор битвы
    :return:
    """

