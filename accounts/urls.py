from django.conf.urls import url, include
from accounts.views import logout, user_profile, edit_profile
from accounts.views import login
from accounts.views import registration
from accounts import url_reset


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^edit/', edit_profile, name="edit_profile"),
    url(r'^password-reset/', include(url_reset))
]
