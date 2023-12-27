from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.db.models.base import MultipleObjectsReturned

from drfauth.models import CustomUser
class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(
                Q(email__iexact=email))
            print(dir(user),"GAA")
            print(user.password == password)
        except CustomUser.DoesNotExist:
            CustomUser().set_password(password)
        except MultipleObjectsReturned:
            return CustomUser.objects.filter(email=email).order_by('id').first()
        else:
            # print(user)
            # print(user.check_password(password))
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
