from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name','city','roll']
        #read_only_fields = ['name','roll']
        #extra_kwargs={'name':{'read_only':True}}

        # Field Level validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Value cannot greater than 200')
        return value

