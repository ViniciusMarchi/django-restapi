from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pets.views.animal_view import AnimaisView, AnimalView
from pets.views.cachorro_view import CachorrosView, CachorroView
from pets.views.gato_view import GatosView, GatoView
from pets.views.passaro_view import PassarosView, PassaroView

urlpatterns = [
    # -------------- animais ------------------------
    path('animais/', AnimaisView.as_view()),
    path('animais/<int:pk>', AnimalView.as_view()),
    
    # -------------- cachorros ----------------------
    path('cachorros/', CachorrosView.as_view()),
    path('cachorros/<int:pk>', CachorroView.as_view()),
    
    # -------------- gatos --------------------------
    path('gatos/', GatosView.as_view()),
    path('gatos/<int:pk>', GatoView.as_view()),
   
    # -------------- passaros -----------------------
    path('passaros/', PassarosView.as_view()),
    path('passaros/<int:pk>', PassaroView.as_view())
]