from django.core.validators import ValidationError


class Validators:
    @staticmethod
    def phone_num(value):
        for ch in value:
            if not ch.isdigit():
                raise ValidationError('Phone number must have only digits!')
