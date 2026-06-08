from django.db import models
from datetime import timedelta
from vehicles.models import Vehicle, VehicleType


class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Numero da Vaga',
    )
    is_occupied = models.BooleanField(
        default=False,
        verbose_name='Ocupado',
    )
    created_at = models.DateTimeField(  # armazena quando o registro foi criado
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(  # DateTimeField armazena data e hora
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.spot_number


class Fare(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        related_name='parking_record',
        verbose_name='Tipo do Veículo',
    )
    hourly_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Valor por hora'
    )
    start_date = models.DateTimeField(
        verbose_name='Data de início'
    )
    end_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Data de término'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Ativa'
    )
    created_at = models.DateTimeField(  # armazena quando o registro foi criado
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(  # DateTimeField armazena data e hora
        auto_now=True,
        verbose_name='Atualizado em',
    )
    
    class Meta:
        verbose_name = 'Tarifa'
        verbose_name_plural = 'Tarifas'
    
    def __str__(self):
        return f'{self.vehicle_type} - {self.hourly_rate}'
    
    
class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Veículo'
    )
    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Vaga'
    )    
    fare = models.ForeignKey(
        Fare,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='fares',
        verbose_name='Tarifa'
    )
    total_amount = models.DecimalField(
        null=True,
        blank=True,
        max_digits=8,
        decimal_places=2,
        verbose_name='Total',
    )
    entry_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Horário de Entrada',
    )
    exit_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Horário de Saída',
    )

    def fare_count(self):
        if self.exit_time and self.fare:
            fare_calc = self.exit_time - self.entry_time # retorna um timedelta
            hours =  fare_calc.total_seconds() / 3600
            total = round(hours * self.fare.hourly_rate, 2)
            self.total_amount = total
            self.save(update_fields=['total_amount'])
        return None
             
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot} - {self.entry_time}'