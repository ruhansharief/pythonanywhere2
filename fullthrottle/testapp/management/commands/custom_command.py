# main/management/commands/populatestocks.py
import datetime
import random
import pytz
import string

from django.core.management.base import BaseCommand

from testapp.models import UserModel, ActivityPeroidModel


first = ('Providencia', 'Tajuana', 'Jayne', 'Russel', 'Raul', 'Laurena', 'Jacquiline', 'Sadye', 'Fatima', 'Charolette', 'Chantal', 'Staci', 'Concepcion', 'Karole')

second = ('Trevino', 'Hamilton', 'Newman', 'Henderson', 'Erickson', 'Nielsen', 'Roach', 'Stuart')





class Command(BaseCommand):
    help = "Save randomly generated activity data."


    def get_start_time(self):
        # Naively generating a random date
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        hour = random.randint(0,23)
        minutes = random.randint(0,59)
        seconds = random.randint(0,59)
        return datetime.datetime(2020, month, day, hour, minutes, seconds)
    
    def get_end_time(self, start_time):

        return start_time + datetime.timedelta(hours=random.randint(3,6))
    
    def get_timezone(self):
        tz = pytz.all_timezones
        #tz = list(tz)
        return tz[random.randint(0,len(tz))]

    def get_user_name(self):
        first_name = random.choice(first)
        second_name = random.choice(second)
        return first_name + " " + second_name

    def get_user_id(self):
        choices = string.ascii_uppercase + string.digits
        return ''.join((random.choice(choices) for i in range(9)))

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            'model_to_update',
            type=int,
            help="Which model to update with random values. 1 for users 2 for activity")


    def handle(self, *args, **options):
        records = []
        import pdb;pdb.set_trace()
        model_to_update = options['model_to_update']
        if model_to_update == 1:
            for i in range(0,5):
                kwargs = {
                    'id': self.get_user_id(),
                    'real_name': self.get_user_name(),
                    'tz': self.get_timezone(),
                }
                record = UserModel(**kwargs)
                records.append(record)
            UserModel.objects.bulk_create(records)
        elif model_to_update == 2:
            user_ids = list(UserModel.objects.values_list('id',flat=True))
            for user_id in user_ids:
                user_instance = UserModel.objects.get(id=user_id)
                for i in range(0,3):
                    start_time = self.get_start_time()
                    end_time = self.get_end_time(start_time)
                    kwargs = {
                        'user': user_instance,
                        'start_time': start_time,
                        'end_time': end_time
                    }
                    record = ActivityPeroidModel(**kwargs)
                    records.append(record)
                ActivityPeroidModel.objects.bulk_create(records)

        self.stdout.write(self.style.SUCCESS('Added successfully'))
