from rest_framework import serializers
from .models import Student

#Bu yöntem zahmetli bunun yerine .models fields kullanılacak
# class Student(serializers.Model):
#  first_name = serializers.CharField(max_length=100)
#  last_name = serializers.CharField(max_length=100)
#  number = serializers.IntegerField(required=False)

class StudentSerializer(serializers.ModelSerializer):
 class Meta:
  model = Student
  # fields = ('first_name', 'last_name', 'number')
  # exclude = ('number',)
  fields = '__all__'
 