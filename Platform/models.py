from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# TODO: add bio, profile image, fraction
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)

    def __str__(self):
        return self.user.username


# Create a new profile if a user is registered
@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)  # add the user to their own follows, so they see their own posts
        user_profile.save()


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING, default="")
    text_content = models.CharField(max_length=500)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text_content) > 30:
            return (f"{self.owner} "
                    f"({self.publication_date:%Y-%m-%d %H:%M}): "
                    f"{self.text_content[:30]}...")
        else:

            return (f"{self.owner} "
                    f"({self.publication_date:%Y-%m-%d %H:%M}): "
                    f"{self.text_content}")


class Song(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title


class Radio(models.Model):
    owner = models.ForeignKey(User, related_name='radios', on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    songs = models.ForeignKey(Song,
                              related_name='listeners',
                              on_delete=models.CASCADE),
    cover = models.ImageField(verbose_name='coverImage',)

    def __str__(self):
        return f'{self.title} by {self.owner.username}'
