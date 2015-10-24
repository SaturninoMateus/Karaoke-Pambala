from django.contrib import admin
from models import Pambaleiro

class PambaleiroAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','birth_date', 'country', 'city',]

    class Meta:
        model = Pambaleiro

    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = 'First name'

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = 'Last name'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'

admin.site.register(Pambaleiro, PambaleiroAdmin)
