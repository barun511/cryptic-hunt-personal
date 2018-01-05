from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        level = models.IntegerField(default=0)
        time_of_level = models.DateTimeField(auto_now=True)
        def __str__(self):
            return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# TODO having level_title, but only description, seems a bit funny. I think we should make level_title just title, and level_number just number, but we need to change level_number to number in views as well.
class Level(models.Model):
	level_title = models.CharField(max_length=30)
	description = models.TextField()
	level_number = models.IntegerField(primary_key=True)
	answer1 = models.CharField(max_length=20)
	answer2 = models.CharField(max_length=20)
	answer3 = models.CharField(max_length=20)
	def __str__(self):
		return self.level_title
#	image = models.ImageField(upload_to="level/") # TODO get this done when you get back home
class Submission(models.Model):
	level = models.ForeignKey(Level, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time_of_submission = models.DateTimeField(auto_now=True)
	submitted_answer = models.CharField(max_length=20) # matches the answer field
	accepted = models.BooleanField()
	def __str__(self):
		return str(self.user.username) + " submitted the answer " + str(self.submitted_answer) + " for Level " + str(self.level.level_number) + " at time " + str(self.time_of_submission)
