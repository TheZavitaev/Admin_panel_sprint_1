import random

import cowsay
from django.db import transaction
from django.core.management.base import BaseCommand

from .models import Product, Order, OrderProduct
from supershop.factories import (
    ProductFactory,
    OrderFactory,
    OrderProductFactory
)



class Command(BaseCommand):
    help = "Создаем тестовые данные"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляем старые данные...")