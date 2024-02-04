from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phonenumber', 'image', 'country', 'password']
        read_only_fields = (['id'])
        extra_kwargs = {
                'password': {
                    'write_only': True,
                  'style': {'input_type': 'password'}
                }
            }

    def create(self, validated_data):

        password = validated_data.pop('password')
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user
    

class YuridikSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Yuridik
        fields = ['id', 'user', 'company', 'company_boss', 
        'company_certificat', 'certificat_period', 'company_address']
        read_only_fields = (['id'])
    
    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        user_instance = UserSerializer().create(user_data) if user_data else None
        yuridik_instance = Yuridik.objects.create(user=user_instance, **validated_data)
        return yuridik_instance

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user
            UserSerializer().update(user_instance, user_data)

        instance.company_boss = validated_data.get('company_boss', instance.company_boss) 
        instance.company = validated_data.get('company', instance.company)
        instance.company_certificat = validated_data.get('company_certificat', instance.company_certificat)
        instance.certificat_period = validated_data.get('certificat_period', instance.certificat_period)
        instance.company_address = validated_data.get('company_address', instance.company_address)

        instance.save()
        return instance
    
    def partial_update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user
            UserSerializer().update(user_instance, user_data)

        instance.company_boss = validated_data.get('company_boss', instance.company_boss) 
        instance.company = validated_data.get('company', instance.company)
        instance.company_certificat = validated_data.get('company_certificat', instance.company_certificat)
        instance.certificat_period = validated_data.get('certificat_period', instance.certificat_period)
        instance.company_address = validated_data.get('company_address', instance.company_address)

        instance.save()
        return self.update(instance, validated_data)


class Jismoniy_ShaxsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Jismoniy_Shaxs
        fields = ['id', 'user', 'gender']
        read_only_fields = (['id'])

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        user_instance = UserSerializer().create(user_data) if user_data else None
        jismoniy_shaxs_instance = Jismoniy_Shaxs.objects.create(user=user_instance, **validated_data)
        return jismoniy_shaxs_instance
        
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user
            UserSerializer().update(user_instance, user_data)

        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance
    
    def partial_update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_instance = instance.user
            UserSerializer().update(user_instance, user_data)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return self.update(instance, validated_data)