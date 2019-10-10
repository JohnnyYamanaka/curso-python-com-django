
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from app1.models import Emissor
from app1.models import Lancamento

class EmissorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Emissor, EmissorAdmin)

class LancamentoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lancamento, LancamentoAdmin)