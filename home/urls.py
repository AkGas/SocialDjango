from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [

	# home page
	url(r'^$', views.IndexView.as_view(), name='index'),

	# user
	url(r'^user', views.UserView.as_view(), name='user') ,

	# forum
	url(r'^gochat$', views.GochatView.as_view(), name='gochat') ,

	# new user
	url(r'^signInUp/$', views.SignupView.as_view(), name='sign'),

	# tutos
	url(r'^filterinterest/$', views.FilterView.as_view(), name='interest'),

	# contacts
	url(r'^contacts/$', views.ContactsView.as_view(), name='contacts'),

	]