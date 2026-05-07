from django.contrib import admin

from .models import Place, Restaurant, Reporter, Article


admin.site.register([Place, Restaurant, Reporter, Article])

