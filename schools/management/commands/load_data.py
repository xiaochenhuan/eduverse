import csv
from django.core.management.base import BaseCommand
from schools.models import School, District

class Command(BaseCommand):
    help = 'Loads cleaned school data from schools.csv'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        count = 0

        try:
            with open(csv_file, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    district_name = row['district_name'].strip()
                    state = row['state'].strip()

                    if not district_name or not state:
                        continue

                    district, _ = District.objects.get_or_create(
                        name=district_name,
                        state=state
                    )

                    try:
                        School.objects.create(
                            name=row['school_name'].strip(),
                            city=row['city'].strip(),
                            state=state,
                            zip=row['zip'].strip(),
                            district=district,
                            latitude=float(row['latitude']),
                            longitude=float(row['longitude']),
                            enrollment=int(float(row['enrollment']) if row['enrollment'] else 0)
                        )
                        count += 1
                        if count >= 5000:  # Only load first 5000 for cloud friendliness
                            break
                    except Exception as e:
                        self.stderr.write(f"Skipping row due to error: {e}")

            self.stdout.write(self.style.SUCCESS(f"✅ Successfully loaded {count} schools."))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"❌ File not found: {csv_file}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ Error: {e}"))
