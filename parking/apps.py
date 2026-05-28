from django.apps import AppConfig


class ParkingConfig(AppConfig):
    name = 'parking'
    verbose_name=''

    def ready(self):
        import parking.signals