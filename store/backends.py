from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
from django.db.models import Q

class EmailOrPhoneBackend(ModelBackend):
    """
    Custom authentication backend that allows users to log in using either
    an email address, phone number, or username (for admins).
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Query to match email, phone, or username (for admins)
            user = CustomUser.objects.get(Q(email=username) | Q(phone=username) | Q(username=username))
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
