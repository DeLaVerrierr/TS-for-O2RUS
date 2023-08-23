# import xlrd
# from django.core.management.base import BaseCommand
# from main.models import GasStation
#
# class Command(BaseCommand):
#     help = 'Load gas station data from Excel file'
#
#     def handle(self, *args, **options):
#         file_path = 'spisokAZS.xls'
#         wb = xlrd.open_workbook(file_path,formatting_info=True)
#         sheet = wb.sheet_by_index(0)
#
#         for row_num in range(1, sheet.nrows):
#             row = sheet.row_values(row_num)
#             region, issuer_number, gas_station_number, address, latitude, longitude, companion_service = row
#             GasStation.objects.create(
#                 region=region,
#                 Issuer_number=issuer_number,
#                 Gas_station_number=gas_station_number,
#                 Address=address,
#                 GPS_coordinates_latitude=latitude,
#                 GPS_coordinates_longitude=longitude,
#                 Companion_Service_Objects=companion_service
#             )
#
#         self.stdout.write(self.style.SUCCESS('Gas station data loaded successfully'))
