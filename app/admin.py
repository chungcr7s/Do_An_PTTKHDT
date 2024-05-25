from django.contrib import admin
from .models import Customer
from .models import *
# from django.urls import reverse

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Profile)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display= ['id','user','locality','city','state','zipcode']
