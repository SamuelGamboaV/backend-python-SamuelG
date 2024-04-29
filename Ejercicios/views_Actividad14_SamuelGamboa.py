import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

class Product:
    opus = 0
    total = 0

    def __init__(self, name, manufacturer, provider, price, shelflife):
        Product.opus += 1
        self.name = name
        self.manufacturer = manufacturer
        self.provider = provider
        self.price = price
        self.shelflife = shelflife

    def __del__(self):
        Product.total -= 1

    def print_attributes(self):
        return f"Nombre: {self.name}, Precio: {self.price}"

class DiscountProduct(Product):
    def __init__(self, name, manufacturer, provider, price, shelflife, discount):
        super().__init__(name, manufacturer, provider, price, shelflife)
        self.discount = discount

    def apply_discount(self):
        discount_amount = self.price * (self.discount / 100)
        discounted_price = self.price - discount_amount
        return f"Descuento: {self.discount}%, Precio con descuento: {discounted_price}"

# Generar una instanciación
# product1 = Product("Mayonesa","McCormick","Productos de México",15.00,"12/31/2023")

def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + "PROBANDO CAMBIOS",
        "python_ver": os.environ["PYTHON_VERSION"] +"MÁS CAMBIOS",
    }

    return render(request, "pages/home.html", context)
