from django.urls import path
from .views import InfoListAPiView, InfoDetailAPiView

urlpatterns = [
    path('info/', InfoListAPiView.as_view(), name='info-list'),
    path('info/<int:disease_id>', InfoDetailAPiView.as_view(), name='info-detail'),
]