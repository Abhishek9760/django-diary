from django.db import models
from django.urls import reverse
from django.conf import settings
from django.dispatch.dispatcher import receiver

User = settings.AUTH_USER_MODEL

class DiaryModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	your_day = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	adventure = models.TextField(null=True, blank=True)

	def __str__(self):
		return str(self.user) + ' on ' + str(self.timestamp.strftime('%d/%m/%Y')) 

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-timestamp']



