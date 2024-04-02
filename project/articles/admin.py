from django.contrib import admin
from .models import Articles

# подключение нашей модели
admin.site.register(Articles)
