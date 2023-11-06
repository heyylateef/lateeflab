#Custom Admin settings to use OTP in admin page
from django.contrib import admin
from django.contrib.auth.models import User
from django_otp.admin import OTPAdminSite
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

class OTPAdmin(OTPAdminSite):
   pass

    



