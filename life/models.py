from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch.dispatcher import receiver

User = settings.AUTH_USER_MODEL

class DiaryModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	your_day = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.timestamp.strftime('%d/%m/%Y'))

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

@receiver(pre_save)
def my_callback(sender, instance, *args, **kwargs):
	if not instance:
		import inspect
		for frame_record in inspect.stack():
			if frame_record[3]=='get_response':
				request = frame_record[0].f_locals['request']
				instance = request.user
				break
			else:
				request = None

# pre_save.connect(my_callback, sender=DiaryModel)


