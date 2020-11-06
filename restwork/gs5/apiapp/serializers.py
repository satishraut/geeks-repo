from .models import Student
from rest_framework import serializers


def starts_with_r(value):   # Validators
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name Should be start with r or R')
        return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=30)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        #print(instance.name)
        instance.name=validate_data.get('name',instance.name)
        #print(instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance

    def validate_roll(self, value): # Field Level Validation it is automatically called when is_valid() called
        if value>=200:
            raise serializers.ValidationError('Value Cannot be greater than 200')
        return value

    def validate(self,data): # data comming in form of dictonary need to extact value
            nm = data.get('name')
            ct = data.get('city')
            if nm.lower()=="satish" and ct != "Basmath":
                raise serializers.ValidationError('City must be Basmath')
            return data
    
   