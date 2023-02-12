from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(measure_pk, new_measurement):
    measurement = get_measurement(measure_pk)
    variablenew = Variable.objects.get(pk=new_measurement["variable"])

    measurement.variable = variablenew
    measurement.value = new_measurement["value"]
    measurement.unit = new_measurement["unit"]
    measurement.place = new_measurement["place"]
    measurement.dateTime = new_measurement["dateTime"]
    measurement.save()
    return measurement

def create_measurement(measure):
    variablenew = Variable.objects.get(pk=measure["variable"])
    measurement = Measurement(id=measure["id"], variable=variablenew,value=measure["value"],unit=measure["unit"],place=measure["place"],dateTime=measure["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    response = Measurement.objects.get(pk=var_pk).delete()
    return response