from django.contrib import admin
from django.urls import path, include
from auth_app.api.views import RegistrationView, CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registration/', RegistrationView.as_view(), name='registration'),
    path('api/login/', CustomLoginView.as_view(), name='login'),
]
