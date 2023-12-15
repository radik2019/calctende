from django.core.management.base import BaseCommand, CommandError
from core.models import ServiceType, Discount, Cost, Product


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        print("parser")
        parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        for poll_id in options["poll_ids"]:
            print("\n\n\n\n************\n\n\n\n")