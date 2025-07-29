from django.core.management.base import BaseCommand
from listings.models import Listing
from realtors.models import Realtor
from random import randint, choice
from datetime import datetime

class Command(BaseCommand):
    help = 'Add 20+ sample listings to the database'

    def handle(self, *args, **kwargs):
        realtors = list(Realtor.objects.all())
        if not realtors:
            self.stdout.write(self.style.ERROR('No realtors found. Please add at least one realtor first.'))
            return
        states = [
            'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
            'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh',
            'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
            'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
            'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 'Chandigarh',
            'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Jammu and Kashmir', 'Ladakh',
            'Lakshadweep', 'Puducherry'
        ]
        for i in range(1, 26):
            listing = Listing(
                realtor=choice(realtors),
                title=f'Sample Property {i}',
                address=f'{randint(1, 999)} Sample Street',
                city=f'City{i}',
                state=choice(states),
                zipcode=f'{randint(100000, 999999)}',
                description=f'This is a sample description for property {i}.',
                price=randint(100000, 1000000),
                bedrooms=randint(1, 10),
                bathrooms=randint(1, 5),
                garage=randint(0, 3),
                sqft=randint(500, 5000),
                lot_size=randint(1, 10),
                photo_main='photos/sample.jpg',
                is_published=True,
                list_date=datetime.now()
            )
            listing.save()
        self.stdout.write(self.style.SUCCESS('Successfully added 25 sample listings!'))
