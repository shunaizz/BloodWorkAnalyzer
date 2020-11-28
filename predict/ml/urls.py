from django.conf.urls import url
from .views import (SignUp,Diabetes_view,
                    profile_view,
                    cardiac_view,breast_view,cholesterol_view,
                    Result,History,Record)

app_name = 'ml'

urlpatterns = [
    url(r'Signup',SignUp.as_view(),name='signup'),
        url(r'Diabetes/$', Diabetes_view, name='diabetes'),
    url(r'profile_create/(?P<data>\d+)/$', profile_view, name='profile_create'),
    url(r'^Cardiac/$', cardiac_view, name='cardiac'),
    url(r'BreastCancer/$', breast_view, name='breast'),
    url(r'cholesterol/$', cholesterol_view, name='cholesterol'),
    url(r'^result/(?P<result>\d+)/(?P<model>\w+)/(?P<level>\w+)$', Result.as_view(), name='result'),
    url(r'^(?P<model>\w+)/history/$', History.as_view(), name='history'),
    url(r'^(?P<model>\w+)/record/(?P<pk>\d+)$', Record.as_view(), name='record'),
]