from django.contrib import admin

# Register your models here.
from autheticatweb.models  import Contact,Product,Post,Message
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Message)
