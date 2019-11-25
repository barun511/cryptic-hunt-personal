from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
MAX_ANSWER_LENGTH = 500
MAX_TITLE_LENGTH = 500
class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        level = models.IntegerField(default=0)
        time_of_level = models.DateTimeField(default=now)
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
    level_title = models.CharField(max_length=MAX_TITLE_LENGTH)
    description = models.TextField()
    level_number = models.IntegerField(primary_key=True)
    answer1 = models.CharField(max_length=MAX_ANSWER_LENGTH)
    answer2 = models.CharField(max_length=MAX_ANSWER_LENGTH)
    answer3 = models.CharField(max_length=MAX_ANSWER_LENGTH)
    def __str__(self):
        return self.level_title + " (" + str(self.level_number) + ")"
    #image = models.ImageField(upload_to="level/") # TODO get this done when you get back home
class Submission(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_of_submission = models.DateTimeField(auto_now_add=True)
    submitted_answer = models.CharField(max_length=MAX_ANSWER_LENGTH) # matches the answer field
    accepted = models.BooleanField()
    def __str__(self):
        return str(self.user.username) + " answered : " + str(self.submitted_answer) + " for Level : " + str(self.level.level_number) + "(" + str(self.time_of_submission) + ")"

class AppVariable(models.Model):
    success_sign_up = models.CharField(max_length=MAX_ANSWER_LENGTH)
