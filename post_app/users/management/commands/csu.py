from django.core.management import BaseCommand
from django.conf import settings
from users.models import CustomUser


class Command(BaseCommand):
    help = "Создает суперпользователя с указанным email и паролем"

    def handle(self, *args, **options):
        email = settings.ROOT_EMAIL
        password = settings.ROOT_PASSWORD

        if not CustomUser.objects.filter(email=email).exists():
            CustomUser.objects.create_superuser(
                email=email,
                password=password,
                first_name="Admin",
                last_name="SkyPro",
            )
            self.stdout.write(self.style.SUCCESS(f"Superuser {email} создан."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser {email} уже существует."))
