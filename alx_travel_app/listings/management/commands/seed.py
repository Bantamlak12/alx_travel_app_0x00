from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title = fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2),
                available=random.choice([True, False])
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded listings.'))
