from django.contrib import admin
from .models import Notice,User_details,Complain_table,House_holding_number
# Register your models here.


class NoticeAdmin(admin.ModelAdmin):
	list_display=('subject', 'description')
class holdingnumber(admin.ModelAdmin):
	list_display=('holder_name', 'holding_number')

class complain(admin.ModelAdmin):
	list_display=('complain_subject', 'complain')
admin.site.register(Notice,NoticeAdmin)
admin.site.register(User_details)
admin.site.register(Complain_table,complain)
admin.site.register(House_holding_number,holdingnumber)