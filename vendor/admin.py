from django.contrib import admin
from .models import Vendor
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'name', 'mobile', 'active', 'date')
    list_filter = ('active', 'date')
    search_fields = ('user__email', 'name', 'mobile')
    ordering = ('-date',)

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'
    user_email.admin_order_field = 'user__email'

admin.site.register(Vendor, VendorAdmin)
