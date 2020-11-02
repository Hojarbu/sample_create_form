from django.db import models

# Create your models here.


class UserRequest(models.Model):
    name = models.CharField(max_length=128, verbose_name='Customer name')
    message = models.CharField(max_length=128, verbose_name='Customer name')
    phone_number = models.CharField(max_length=128, verbose_name='Telefon raqam')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Customer request'
        verbose_name_plural = 'Customer requests'
