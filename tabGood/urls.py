from django.urls import path
from rest_framework import routers
from .views import UserListCreateView, UpdateCountView

router = routers.DefaultRouter()

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('update_count/', UpdateCountView.as_view(), name='update_count'),

]

urlpatterns += router.urls

