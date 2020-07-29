from django.contrib import admin
from .models import Account, Stock
# Register your models here.

@admin.register(Account)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'call', 'address']

@admin.register(Stock)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'image','price','amount']