from django.urls import path
from veterinarios.views.veterinario_view import VeterinariosView, VeterinarioView

urlpatterns = [
    path('veterinarios/', VeterinariosView.as_view()),
    path('veterinarios/<int:pk>', VeterinarioView.as_view()),
]