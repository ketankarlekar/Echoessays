from django.contrib import admin
from .models import PostModel



class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')
    
    
    
    
admin.site.register(PostModel,PostModelAdmin)



# Register your models here.
