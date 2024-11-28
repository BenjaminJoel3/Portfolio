from django.conf.urls import url
from.import views

app_name='accounts'

urlpatterns = [
  url(r'^$',views.signup_view,name="signUp"),
  url(r'^$',views.logIn_view,name="login_view"),
  url(r'^$',views.logOut_view,name="logout_view")
]