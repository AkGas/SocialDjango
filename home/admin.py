from django.contrib import admin
from .models import Users, Contributions, Files, Posts#, Reactions


admin.site.register(Users)
admin.site.register(Files)
admin.site.register(Contributions)
admin.site.register(Posts)
#admin.site.register(Reactions)
