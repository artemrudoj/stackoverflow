from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

__author__ = 'artem'



users = [
    "Ganaurnar",
    "Pemenefi",
    "Himyadl",
    "Yeneeaht",
    "Tulever",
    "Zanade",
    "Fano",
    "Varanidal",
    "Dyanebure",
    "Catryshal",
    "Orrlo",
    "Gokal",
    "Asla",
    "Zelyl",
    "Wipramahi",
    "Panyios",
    "Sulima",
    "Gima",
    "Ziu",
    "Jenigeve",
    "Xuiat",
    "Parrarax",
    "Friara",
    "Nnalw",
    "Oharl",
    "Uvirochut",
]


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def handle(self, *args, **options):
        for nick in users:
            User = get_user_model()
            user = User.objects.create_user(username=nick, email = nick + "@mail.ru", password = "1")
            user.save()
