from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.dispatch import receiver


class BaseAction(models.Model):
    TYPE_BODY = 'body'
    TYPE_CASES = (
        TYPE_BODY,
    )

    type = models.Case(cases=TYPE_CASES)
    class Meta:
        abstract = True


class BodyAction(BaseAction):
    left_arm =  models.BooleanField(default=False)
    right_arm = models.BooleanField(default=False)
    body =      models.BooleanField(default=False)
    left_leg =  models.BooleanField(default=False)
    right_leg = models.BooleanField(default=False)


class Battle(models.Model):
    """
    Битва на арене
    """
    player1 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='battles1')
    player2 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='battles2')
    first_player_turn = models.BooleanField(default=True)
    # полиморфные ссылки
    action1_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='action1')
    action1_object_id = models.PositiveIntegerField()
    action1 = GenericForeignKey('action1_ct', 'action1_object_id')

    action2_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='action2')
    action2_object_id = models.PositiveIntegerField()
    action2 = GenericForeignKey('action2_ct', 'action2_object_id')


@receiver(models.signals.pre_save, sender=Battle)
def on_battle_change(sender: Battle, **kwargs):
    sender.first_player_turn = not sender.first_player_turn
