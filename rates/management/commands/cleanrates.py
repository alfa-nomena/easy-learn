from django.core.management.base import BaseCommand
from tqdm import tqdm
from rates.models import Rate

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for rate in tqdm(Rate.objects.all(), desc='Removing rates'):
            rate.delete()