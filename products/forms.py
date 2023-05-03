from django import forms


PAYMENT_TYPES = (
        ('Банковской картой', 'Банковской картой'),
        ('Наличными', 'Наличными')
    )


class PaymentType(forms.Form):
    payment_type = forms.ChoiceField(choices=PAYMENT_TYPES)
    place_number = forms.IntegerField()


