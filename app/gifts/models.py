from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return f'{self.name}({self.pk})'


class GiftRequest(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='wishes'
    )
    gift = models.ForeignKey(
        Gift, 
        on_delete=models.CASCADE
    )
    santa = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='gifts'
    )

    def __str__(self):
        return f'{self.user}: {self.gift.name}'
