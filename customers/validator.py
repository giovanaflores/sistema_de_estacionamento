import re 
from django.core.exceptions import ValidationError
from validate_docbr import CPF

def name_validation(value):
    clean_name = value.strip()
    if len(clean_name.split()) < 2:
        raise ValidationError("Insira o nome completo (Nome e Sobrenome com espaço).")
    
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+([\s]+[A-Za-zÀ-ÖØ-öø-ÿ]+)+$", clean_name):
        raise ValidationError("O nome deve conter apenas letras.")
    
def phone_validation(value):
    just_numbers = re.sub(r'\D', '', value)
    if len(just_numbers) not in [10,11]:
        raise ValidationError("O número de telefone deve conter o DDD e ter 10")
    
    if not re.match(r"^[1-9]{2}9[0-9]{8}", just_numbers):
        raise ValidationError(
            "O telefone deve incluir um DDD válido e ser um número de celular iniciado com o numero 9"
        )
    
def cpf_validation(value):
    cpf = CPF()
    print(cpf.generate())
    
    if not cpf.validate(value):
        raise ValidationError("CPF inválido")
    