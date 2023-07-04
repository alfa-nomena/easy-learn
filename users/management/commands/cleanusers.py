from django.core.management.base import BaseCommand
from tqdm import tqdm
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options) -> str | None:
        for user in tqdm(User.objects.all(), desc='Removing Users'):
            user.delete()