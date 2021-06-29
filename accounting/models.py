from django.db import models
from django.conf import settings


class Accounting(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField(verbose_name="Date of birth")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    finances = models.FileField(
        upload_to=settings.UPLOAD_TO, verbose_name="Finances Excel"
    )
    finance_data = models.JSONField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.date_of_birth}'
