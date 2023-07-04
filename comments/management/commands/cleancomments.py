from django.core.management.base import BaseCommand
from tqdm import tqdm
from comments.models import Comment

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for comment in tqdm(Comment.objects.all(), desc='Removing comments'):
            comment.delete()