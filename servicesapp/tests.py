from django.test import TestCase
from django.core.mail import send_mail
from django.conf import settings
from .views import email_inquiry
from .forms import ContactForm
# Create your tests here.

class EmailTesting(TestCase):
    def test_send_mail(self):
        print("\nTesting email sending functionality...")
        send_mail(subject='Example subject here', message='Here is the message body.', from_email='from@example.com', recipient_list=['to@example.com'])
        #email_inquiry(name=name, email=email, message=message, serviceType="Inquiry")
        print("Done testing email functionality!")


