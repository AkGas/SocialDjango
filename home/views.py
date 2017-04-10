from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Users, Files, Contributions, Posts


class IndexView(generic.ListView):
	template_name = 'home/index.html'

	def get_queryset(self):
		return Users.objects.all()
	

class UserView(generic.DetailView):
	model = Users
	template_name = 'home/user.html'


class UserCreate(CreateView):
	model = Users
	field = ['name', 'login', 'email']
	template_name = 'home/sign.html'

class GochatView(generic.ListView):
	template_name = 'home/gochat.html'
	context_object_name = 'all_users'

	def get_queryset(self):
		return Users.objects.all()


class FilterView(generic.ListView):
	template_name = 'home/interest.html'

	def get_queryset(self):
		return Posts.objects.all()


class SignupView(generic.ListView):
	template_name = 'home/sign.html'

	def get_queryset(self):
		return Users.objects.all()


class ContactsView(generic.ListView):
	template_name = 'home/contacts.html'

	def get_queryset(self):
		return 0

class Error404View(generic.ListView):
	template_name = 'home/404.html'
