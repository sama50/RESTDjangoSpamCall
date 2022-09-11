from django.contrib import admin
from api.models import User , spanNumber
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class spanNumberList(admin.ModelAdmin):
    list_display = ('id','name','number')
#     # list_filter = ('number',)
#     # search_fields = ('number',)
#     # ordering = ('number', 'id')
admin.site.register(spanNumber,spanNumberList)


class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'phone', 'name', 'email', 'is_admin')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('phone', 'password')}),
      ('Personal info', {'fields': ('name', 'email')}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name', 'phone', 'password1', 'password2'),
      }),
  )
  search_fields = ('phone',)
  ordering = ('phone', 'id')
  filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)