import re
from django.contrib import admin
from customers.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'formatted_cpf', 'formatted_phone', 'created_at']
    search_fields = ['name', 'cpf', 'phone']
    
    def save_model(self, request, obj, form, change):
        obj.full_clean()
        super().save_model(request, obj, form, change)
        
    @admin.display(description='CPF', ordering='cpf')
    def formatted_cpf(self, obj):
        if not obj.cpf:
            return ""
        numbers = re.sub(r'\D', '', obj.cpf)
        if len(numbers) == 11:
            return f"{numbers[:3]}.{numbers[3:6]}.{numbers[6:9]}-{numbers[9:]}"
        return obj.cpf
    
    @admin.display(description='Telefone', ordering='phone')
    def formatted_phone(self, obj):
        if not obj.phone:
            return ""
        numbers = re.sub(r'\D', '', obj.phone)
        if len(numbers) == 11:
            return f"({numbers[:2]}) {numbers[2:7]}-{numbers[7:]}"
        elif len(numbers) == 10:
            return f"({numbers[:2]}) {numbers[2:6]}-{numbers[6:]}"
        return obj.phone