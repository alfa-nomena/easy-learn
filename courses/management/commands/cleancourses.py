from django.core.management.base import BaseCommand
from tqdm import tqdm
from courses.models import Course

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for course in tqdm(Course.objects.all(), desc='Removing Courses'):
            course.delete()