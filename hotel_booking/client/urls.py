from django.urls import path
from .views import home
from .views import about
from .views import contact
from .views import login_logout
from .views import your_booking



urlpatterns = [
    path('', home, name='home'),
    path('sobre/', about, name='about'),
    path('contato/', contact,name='contact'),
    path('validation/', login_logout, name='validation'),
    path('suas_reservas/', your_booking, name='your_booking'),
]