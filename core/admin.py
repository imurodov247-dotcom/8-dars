from django.contrib import admin,messages
from .models import Expense
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.forms import AdminOwnPasswordChangeForm,UserChangeForm,UserCreationForm

admin.site.unregister(User)
@admin.register(User)


class UserAdmin(BaseUserAdmin,ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminOwnPasswordChangeForm




@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
    list_display = ["description","amount","category","status","created_at"]
    list_editable = ["amount","status"]
    actions = ['statusni_eski_qilish']
    search_fields = ["description"]
    list_filter = ["status","category"]
    
    @admin.action(description="Eskirtirish")
    def statusni_eski_qilish(self,request,queryset):
        queryset.update(status="eski")
        messages.add_message(request,messages.SUCCESS,"Status eskiga ozgartirildi")
        