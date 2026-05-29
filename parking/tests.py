from django.test import SimpleTestCase
from django.urls import resolve


class ParkingUrlsTests(SimpleTestCase):
    def test_parking_records_route_resolves(self):
        match = resolve('/api/v1/parking/records/')

        self.assertEqual(match.view_name, 'parkingrecord-list')
