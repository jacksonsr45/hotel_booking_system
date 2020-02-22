from django.urls import path
from .views import home
from .views import about
from .views import contact
from .views import login_logout
from .views import your_booking


urlpatterns = [
    path('', home),
    path('sobre/', about),
    path('contato/', contact),
    path('login/', login_logout),
    path('suas_reservas/', your_booking),
]