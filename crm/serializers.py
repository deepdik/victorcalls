from rest_framework import serializers
from .models import *
import json
from rest_framework.response import Response
from rest_framework.serializers import SerializerMethodField

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'
        #fields = ('name',)


class AspnetrolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspnetroles
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanytypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companytype
        fields = '__all__'

class AspnetusersSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField()
    # def get_role(self, instance):
    #     #print('dfsgds',instance.roleid)
    #     data= Aspnetroles.objects.filter(id= int(instance.roleid))
    #     #print('data',data)
    #     return AspnetrolesSerializer(data,many=True).data

    class Meta:
        model = Aspnetusers
        fields = '__all__'
        # fields = [
        #     'id',
        #     'username',
        #     'email',
        #     'passwordhash',
        #     'companyid',
        #     'roleid'
        #     'role'
        # ]


class AspnetusersWrolesSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    def get_role(self, instance):
        data= Aspnetroles.objects.filter(id= int(instance.roleid))
        return AspnetrolesSerializer(data,many=True).data
    class Meta:
        model = Aspnetusers
        fields = [
            'id',
            'username',
            'email',
            'passwordhash',
            'companyid',
            'roleid',
            'role'
        ]

class AspnetusersWithrolesSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    def get_role(self, instance):
        data= Aspnetroles.objects.filter(id= int(instance.roleid))
        # for d in data:
        #     print(d.name)
        return AspnetrolesSerializer(data,many=True).data
    class Meta:
        model = Aspnetusers
        fields = [
            'id',
            'username',
            'email',
            'passwordhash',
            'companyid',
            'roleid',
            'projectid',
            'createddatetime',
            'accessfailedcount',
            'firstname',
            'lastname',
            'lockoutenabled',
            'lockoutenddateutc',
            'twofactorenabled',
            'phonenumberconfirmed',
            'phonenumber',
            'emailconfirmed',
            'securitystamp',
            'token',
            'role'
        ]


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'


class LeadsWithItemsSerializer(serializers.ModelSerializer):
    items= SerializerMethodField()
    def get_items(self,instance):
        items= Leaditems.objects.filter(lead_id=instance.lead_id)
        data = LeaditemsSerializer(items,many=True).data
        return data

    class Meta:
        model = Leads
        fields = [
            'lead_id',
            'createuser_id',
            'edituser_id',
            'createdatetimeoffset',
            'editdatetimeoffset',
            'name',
            'email',
            'phonenumber',
            'isassigned',
            'companyid',
            'cmpctlabel',
            'receivedon',
            'status',
            'id',
            'items'
        ]


class LeadsUpdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'
    def update(self, instance, validated_data):
        items = validated_data.pop('items')
        lead_id= self.context['request'].data['lead_id']
        lead = Leads.objects.get(pk=lead_id)
        leads_serializer = LeadsSerializer(lead, data=self.context['request'].data)
        if leads_serializer.is_valid():
            leads_serializer.save()
        print('items',items)
        return lead

class UploadDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projectdocument
        fields = '__all__'




class Leads_with_itemsSerializer(serializers.ModelSerializer):
    items= serializers.SerializerMethodField()
    def get_items(self,instance):
        data = Leaditems.objects.filter(lead_id=int(instance.lead_id))
        return LeaditemsSerializer(data,many=True).data
    class Meta:
        model = Leads
        fields = [
            'lead_id',
            'createuser_id',
            'edituser_id',
            'createdatetimeoffset',
            'editdatetimeoffset',
            'name',
            'email',
            'phonenumber',
            'isassigned',
            'companyid',
            'cmpctlabel',
            'receivedon',
            'status',
            'id',
            'items'
        ]

class LeadsExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = [
            'name',
            'email',
            'phonenumber',
            'companyid',
            'cmpctlabel',
            'status'
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class IntegrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrations
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class LeaditemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaditems
        fields = '__all__'



class RecordingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordings
        fields = '__all__'