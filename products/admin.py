from django.contrib import admin
from . models import Product,Offer,User,Form

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

class FormAdmin(admin.ModelAdmin):
    list_display = ('email','subject','message')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Form,FormAdmin)