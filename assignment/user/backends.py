# user/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(email)
        print(password)
        try:
            user = UserModel.objects.get(email=email)
            print(user.password)
        except UserModel.DoesNotExist:
            return None

        if user.password == password:
        
            return user
        return None
