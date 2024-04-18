from django.core.management.base import BaseCommand
import requests
import pandas as pd
from io import BytesIO, StringIO
from zipfile import ZipFile
from chatbot.models import EconomicIndicator

class Command(BaseCommand):
    help = "Fetches and stores data from the World Bank API"

    def handle(self, *args, **options):
        urls = {
            "Poverty headcount ratio at $2.15 a day": "https://api.worldbank.org/v2/en/indicator/SI.POV.DDAY?downloadformat=csv",
            "Individuals using the Internet": "https://api.worldbank.org/v2/en/indicator/IT.NET.USER.ZS?downloadformat=csv",
            "Unemployment rate": "https://api.worldbank.org/v2/en/indicator/SL.UEM.TOTL.ZS?downloadformat=csv"
        }

        for name, url in urls.items():
            self.stdout.write(self.style.SUCCESS(f"Fetching data for: {name}"))
            response = requests.get(url)
            if response.status_code == 200:
                # Check if the response is compressed
                if 'application/zip' in response.headers.get('Content-Type', ''):
                    # Handle ZIP file
                    with ZipFile(BytesIO(response.content)) as z:
                        # Extract the first CSV file found
                        for filename in z.namelist():
                            if filename.endswith('.csv'):
                                with z.open(filename) as file:
                                    csv_file = StringIO(file.read().decode('utf-8'))
                                    self.process_csv(csv_file, name)
                                    break
                else:
                    # Handle as plain text CSV
                    csv_file = StringIO(response.content.decode('utf-8'))
                    self.process_csv(csv_file, name)
            else:
                self.stdout.write(self.style.ERROR('Failed to fetch data'))

    def process_csv(self, csv_file, indicator_name):
        for _ in range(4):  # Skip initial non-data lines if necessary
            next(csv_file)

        df = pd.read_csv(csv_file)
        for _, row in df.iterrows():
            if pd.isna(row['Country Code']):
                continue

            for year in range(1960, 2022):
                year_str = str(year)
                if pd.isna(row[year_str]):
                    continue

                EconomicIndicator.objects.update_or_create(
                    name=indicator_name,
                    country=row['Country Name'],
                    year=year,
                    defaults={'value': row[year_str]}
                )

        self.stdout.write(self.style.SUCCESS(f"Processed data for: {indicator_name}"))
