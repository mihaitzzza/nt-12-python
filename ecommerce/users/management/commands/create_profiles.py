from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Profile

AuthUser = get_user_model()


class Command(BaseCommand):
    help = 'Create profile for existing users if they do not have already one.'

    def handle(self, *args, **options):
        users_without_profile = AuthUser.objects.filter(profile=None)
        for user in users_without_profile:
            Profile.objects.create(user=user)
