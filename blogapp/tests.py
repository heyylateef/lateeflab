from django.test import TestCase, override_settings, Client
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import os, shutil
from .models import Blogpost
from blogapp.middleware import TimezoneMiddleware

# Create your tests here.

TEST_DIR = os.path.join(settings.BASE_DIR, 'testmedia/') #Defines test media root, will be deleted on successful testing

class blogTests(TestCase):
    
    def test_timezone_middleware(self):
        print("\nTesting timezone activation...")
        client = Client() #Defines a mock client
        client.post("/settimezone", {'timezone': 'US/Eastern'}) #Uses the mock client to mock a HTTP POST request; for testing the timezone activation
        if client.request == 'POST':
            client.request.session['django_timezone'] = client.request.POST['timezone'] #Sets the mock timezone
            return TimezoneMiddleware(get_response=client.request) #Tests the TimezoneMiddleware with the mock client's HTTP POST request
        print("Done testing timezone activation!")

    @override_settings(MEDIA_ROOT=(TEST_DIR))
    def test_create_blogpost(self):
        print("\nTesting blog post creation...")
        
        testUser = User.objects.create_user(username='testUser', password='12345') #Creates test user
        self.client.login(username='testuser', password='12345') #Logs in testUser
        
        PNGtestpic = SimpleUploadedFile(name="pngtest.png", content=open(settings.MEDIA_ROOT + "pngtest.png", 'rb').read(), content_type='image/png') #Uploads test picture to media root
        Blogpost.objects.create(title="How to run tests", cover_image= PNGtestpic, author=testUser)
        print("Done testing blog post creation!")


def tearDownModule():
    print("Deleting temporary files...\n")
    try:
        #shutil.rmtree(TEST_DIR + '/django-summernote/') #Comepletly deletes the Test media root's "django-summernote" folder and files
        shutil.rmtree(TEST_DIR + '/uploads/') #Completely deletes the Test media root's "uploads" folders and files
        print("Done deleting temp files!")
    except OSError:
        print("Error. Could not delete temp files/folders")
        pass