#Custom app config to use OTP in admin page
from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = "lateeflab.admin.OTPAdmin"