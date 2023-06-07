from django import forms

MEDICINES_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 5)]


class CartAddMedicinesForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=MEDICINES_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)