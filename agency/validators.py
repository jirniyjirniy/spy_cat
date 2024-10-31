import requests
from django.core.exceptions import ValidationError


def validate_breed(breed):
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    breeds = [b['name'].lower() for b in response.json()]

    if breed.lower() not in breeds:
        raise ValidationError(f"{breed} is not a valid cat breed.")
