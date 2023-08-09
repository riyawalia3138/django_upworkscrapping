
from rest_framework import serializers
from upwork_app.models import upwork,dataa,my_table
  
class upworkSerializer(serializers.ModelSerializer):
    # up_id=serializers.ReadOnlyField() 
    up_name = serializers.CharField(max_length=50, required=True,min_length=3) 
    # up_url = serializers.CharField(max_length=50, required=True,min_length=3) 
    # def create(self, validated_data):  
    #     return upwork.objects.create(**validated_data)  
    class Meta:
        model = upwork
        fields = "__all__"
        
class dataSerializer(serializers.ModelSerializer):
    data_id=serializers.ReadOnlyField()   
    data_skills=serializers.CharField(max_length=500, required=True,min_length=3)  
    # def create(self, validated_data):  
    #     return data.objects.create(**validated_data)  
    class Meta:
        model = dataa
        fields = "__all__"  
        
class my_tableSerializer(serializers.ModelSerializer):
    Job_id = serializers.ReadOnlyField()
    JobName = serializers.CharField(max_length=50, required=True,min_length=3)
    JobDescription = serializers.CharField(max_length=50, required=True,min_length=3)
    # def create(self, validated_data):  
    #     return my_table.objects.create(**validated_data)  
    class Meta:
        model = my_table
        fields = "__all__"  
        