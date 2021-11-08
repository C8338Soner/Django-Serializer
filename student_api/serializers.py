from rest_framework import serializers
from .models import Student, Path

#Bu yöntem zahmetli bunun yerine .models fields kullanılacak
# class Student(serializers.Model):
#  first_name = serializers.CharField(max_length=100)
#  last_name = serializers.CharField(max_length=100)
#  number = serializers.IntegerField(required=False)

class PathSerializer(serializers.ModelSerializer):
 # students = serializers.PrimaryKeyRelatedField(read_only=True, many = True)
 students =  serializers.HyperlinkedIdentityField(view_name='detail', format='html', many=True, read_only=True)
 class Meta:
  model = Path
  fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
 path = serializers.StringRelatedField()
 path_id = serializers.IntegerField()
 paths = serializers.SerializerMethodField()
 class Meta:
  model = Student
  fields = ('first_name', 'last_name', 'number', 'path', 'path_id', "paths")
  # exclude = ('number',)
  #fields = '__all__'
 
 def get_paths(self,obj):
  paths_data = Path.objects.all()
  serializer = PathSerializer(paths_data, many = True)
  