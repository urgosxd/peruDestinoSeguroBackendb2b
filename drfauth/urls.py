
from dj_rest_auth.registration.views import SocialAccountListView
from dj_rest_auth.views import LoginView
from django.urls import path
from .views import CustomLoginEmailView, GoogleConnect,GoogleLoginView


urlpatterns = [
        path("login/",CustomLoginEmailView.as_view(),name="rest_login"),
        path('google/',GoogleLoginView.as_view(),name="google"),
        path('connect/google/connect/', GoogleConnect.as_view(), name='google_conect'),
         path(
        'socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
        ]
