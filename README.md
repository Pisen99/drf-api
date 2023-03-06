Installing Django:
* In terminal
- pip3 install 'django<4'
- django-admin startproject projectName .


Installing Cloudinary:
* In terminal
- pip3 install django-cloudinary-storage
- pip3 install Pillow (This library adds image processing images)

* In Settings.py
- Add 'cloudinary_storage' to 'INSTALLED_APPS'.
  Important! Add it above 'django.contrib.staticfiles'.
- Add 'cloudinary' to 'INSTALLED_APPS'.
  Important! Add it under 'django.contrib.staticfiles'.

- Add 'from pathlib import Path
       import os'.
- Under import add, 'if os.path.exists('env.py'):
    import env'.
- Under if statement add, 'CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}'.
- Directly Under The cloudinary library add, 'MEDIA_URL = '/media/'.' (Django folder to store media files like images)
- Directly under the variabel add, 'DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage''.


* In env.py
- First create 'env.py' file in the top level directory.
- Add 'import os'.
- Under the import, add os.environ['CLOUDINARY_URL'] = 'cloudinary://<cloudinary_key>'


Start Project:
* In terminal
- python manage.py startapp <projectname>
Obs! leave an empty row before adding <projectname> to 'INSTALLED_APPS'.

* In models.py
- Import 'from django.contrib.auth.models import User'
- Create the profile model like this:
  class Profiles(models.Model):
    owner = models.OneToOneField(User, on_delete=models.cascade)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        Upload_to='images/', default='../default_profile_yktfo7'
    )
- Inside profile model, add:
  class Meta:
    ordering = ['-created_at'] (minus sign indicates we want our result reversed)
- Create a dunder string after 'class Meta' still inside the profile model,
  def __str__(self):
    return f"{self.owner}'s profile".
- Above the second import, 'from django.db.models.signals import post_save'
- Outside the profile model, add 'post_save.connect(create_profile, sender=User)'
- above add,
  def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


* In admin.py:
- Add, "from .models import Profile
       
       admin.site.register(Profile)"


* In terminal:
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
- pip freeze > requirements.txt
- git add/commit/push.

* In browser:
- Go to '/admin' and log in.
- 