from . import views
from django.conf.urls import url
app_name = "login"


urlpatterns = [
    url('^$' , views.login , name = 'login'),
    url("^forgot/" , views.forgotcredetials , name = 'forgot'),
    url("^logout/" , views.logout , name = "logout"),
    url("^updatereset/" , views.newcr , name = "newcreds")
]
