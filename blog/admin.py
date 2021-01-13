from django.contrib import admin

# Register your models here.
from .models import article
from .models import author
from .models import category


admin.site.register(article)
admin.site.register(author)
admin.site.register(category)