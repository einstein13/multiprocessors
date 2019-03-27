from django.contrib import admin

from commons.models import Variable

# Register your models here.

class VariableAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'value_string', 'value_int', 'value_boolean')
    search_fields = ('keyword', 'value_string', 'value_int', 'value_boolean')

admin.site.register(Variable, VariableAdmin)