from django.contrib import admin

from .models import *


admin.site.register(Bill)
admin.site.register(Card)
admin.site.register(Report)
admin.site.register(AdminReport)

admin.site.register(Worker)
admin.site.register(Accountant)
admin.site.register(Admin)
