from django.db import models

# Create your models here.

class Station(models.Model):
    station_id = models.CharField('station-id', primary_key=True, max_length=10)
    label = models.CharField("station-label", max_length=40)

    def __str__(self):
        string = "{%s,%s}"%(self.station_id,self.label)
        return string
    
    
class Weather(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField('create-date')
    time = models.TimeField('create-time')
    speed = models.FloatField('wind-speed')
    direction = models.CharField('wind-direction',max_length=10)
    temperature = models.FloatField('temperature')
    humidity = models.FloatField('humidity')

    def __str__(self):
        string = "{}[{} {}] {}/{} {}/{}".format(
            self.station,
            self.date,
            self.time,
            self.speed,
            self.direction,
            self.temperature,
           self.humidity
        )
        return string