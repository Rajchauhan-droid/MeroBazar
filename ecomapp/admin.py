from django.contrib import admin
from .models import Customer, Category, Product, Cart, CartProduct,BookmarkProduct, Order, Brand, Admin, Carousel, ProductImage, Review
# Register your models here.


admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Admin)
admin.site.register(ProductImage)


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(Carousel, CarouselAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'status',
                    'is_featured', 'image_tag')
    list_editable = ('status', 'is_featured')


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'discount', 'order_status', 'payment_method')


admin.site.register(Order, OrderAdmin)


admin.site.register(Review)


class BookmarkProductAdmin(admin.ModelAdmin):
    list_display = ('cart','user','timestamp')
admin.site.register(BookmarkProduct,BookmarkProductAdmin)