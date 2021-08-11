import random

from django.db import transaction
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создаем тестовые данные"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляем старые данные...")
