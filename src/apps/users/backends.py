from django.contrib.auth.hashers import check_password
from .models import CustomUser


class CustomAuthBackend:
    def authenticate(self, request, email=None, password=None):

        try:
            user = CustomUser.objects.get(email=email)

            if check_password(password, user.password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None