from django.shortcuts import render
from django.views.generic import TemplateView
import flask_excel as excel

from werkzeug.utils import secure_filename
from flask import Flask, request
from bunch import bunchify
import pyexcel
from django.db.models import Q
import os.path
from datetime import datetime
import pprint
from django.http import HttpResponse
from .authtoken import *

from django.core.paginator import Paginator
import pandas as pd
import xlrd
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework import status
import psycopg2
import json
from psycopg2.extras import RealDictCursor
#con = psycopg2.connect(dbname='leadpoliceb', user='postgres', host='localhost', password='Bismillah@123')
con = psycopg2.connect(dbname='LeadPolice', user='postgres', host='50.63.167.106', password='Modinagar@7')
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm
from facebookads.adobjects.leadgenform import LeadgenForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
token = 'zzzzz'
# def get_other_leads(leads):
#     print(leads)
#     new_grouped_assignment_3 = dict()
#     for row in leads:
#         if row['lead_id'] not in new_grouped_assignment_3:
#             new_grouped_assignment_3[row['lead_id']] = [{'lead_id': row['lead_id'],
#                                                          'queryremarks': row['queryremarks'],
#                                                          'typeofproperty': row['typeofproperty'],
#                                                          'status': row['status'],
#                                                          'rangefrom': row['rangefrom'],
#                                                          'rangeto': row['rangeto'],
#                                                          'cmpctlabel': row['cmpctlabel'],
#                                                          'receivedon': row['receivedon'],
#                                                          'projname': row['projname'],
#                                                          'assignedto': row['assignedto'],
#                                                          'statusid': row['statusid'],
#                                                          'statusdate': row['statusdate'],
#                                                          'leaditemid': row['leaditemid'],
#                                                          }]
#         else:
#             new_grouped_assignment_3[row['lead_id']] += [{'lead_id': row['lead_id'],
#                                                           'queryremarks': row['queryremarks'],
#                                                           'typeofproperty': row['typeofproperty'],
#                                                           'status': row['status'],
#                                                           'rangefrom': row['rangefrom'],
#                                                           'rangeto': row['rangeto'],
#                                                           'cmpctlabel': row['cmpctlabel'],
#                                                           'receivedon': row['receivedon'],
#                                                           'projname': row['projname'],
#                                                           'assignedto': row['assignedto'],
#                                                           'statusid': row['statusid'],
#                                                           'statusdate': row['statusdate'],
#                                                           'leaditemid': row['leaditemid']
#                                                           }]
#     l = []
#     # print(new_grouped_assignment_3)
#     for a in new_grouped_assignment_3:
#         # print(a)
#         l.append(a)
#         # new_ld = dict()
#
#     # print(new_grouped_assignment_3[l[0]])
#     i = 0
#     leadsss = list()
#     while (i < len(l)):
#         new_ld = dict()
#         new_ld['lead_id'] = l[i]
#         new_ld['createuser_id'] = row['createuser_id']
#         new_ld['createdatetimeoffset'] = row['createdatetimeoffset']
#         new_ld['edituser_id'] = row['edituser_id']
#         new_ld['editdatetimeoffset'] = row['editdatetimeoffset']
#         new_ld['name'] = row['name']
#         new_ld['email'] = row['email']
#         new_ld['phonenumber'] = row['phonenumber']
#         # new_ld['isassigned']=row['isassigned']
#         new_ld['companyid'] = row['companyid']
#         new_ld['cmpctlabel'] = row['cmpctlabel']
#         new_ld['receivedon'] = row['receivedon']
#         new_ld['status'] = row['status']
#         new_ld['items'] = new_grouped_assignment_3[l[i]]
#         leadsss.append(new_ld)
#         i = i + 1
#     return leadsss
#
# def other_leads_company_id(company_id):
#     queryset = "Select u.Id as  Id,(u.FirstName || ' ' || u.LastName) as userName,li.BuilderInterest,li.CmpctLabel," \
#                "l.CompanyId,l.CreateDateTimeOffset,l.CreateUser_ID,l.EditDateTimeOffset,l.EditUser_ID,l.Email,l.Lead_ID," \
#                "l.Name,l.PhoneNumber,li.ProjName,li.QueryRemarks,li.RangeFrom,li.RangeTo,li.ReceivedOn,l.Status, li.StatusDate," \
#                "li.StatusId,li.TypeOfProperty,li.AssignedTo,li.LeadItemId from Leads l join LeadItems li on " \
#                "li.Lead_ID = l.Lead_ID join AspNetUsers u on u.Id::varchar = li.AssignedTo where l.CompanyId = {} " \
#                "and li.StatusId =1".format(company_id)
#     cursor = open()
#     cursor.execute(queryset)
#     records = cursor.fetchall()
#     r = json.dumps(records, indent=4, sort_keys=True, default=str)
#     loaded_r = json.loads(r)
#     result = get_other_leads(loaded_r)
#     return result

# def open():
#     global con
#     #cur = con.cursor()
#     con = psycopg2.connect(dbname='LeadPolice', user='postgres', host='50.63.167.106', password='Modinagar@7')
#     cur = con.cursor(cursor_factory=RealDictCursor)
#     return cur
#
#
# def close(cur):
#     global con
#     con.commit()
#     cur.close()
#     con.close()
#     return True


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')

class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html')

class DocumentsList(APIView):
    def get(self,request):
        records = Projectdocument.objects.all()
        serializer = UploadDocSerializer(records,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentsSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Documents_of_project(APIView):
    def get(self,request, project_id):
        records = Projectdocument.objects.filter(projectid=project_id)
        serializer = UploadDocSerializer(records,many=True)
        return Response(serializer.data)

class Documents_of_project_List(APIView):
    def get(self,request, project_id):
        records = Documents.objects.filter(projectid= project_id)
        serializer = DocumentsSerializer(records,many=True)
        return Response(serializer.data)

    def post(self, request, project_id):
        save_path = 'E:/aarif/'
        f = request.FILES['file']
        print(f.name)
        #f.save(secure_filename(f.filename))
        #print(request.data)
        return Response('success')

class Cretae_document(CreateAPIView):
    serializer_class = UploadDocSerializer

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     pass


class Get_project_document(APIView):
    def get(self,request,project_id):
        record = Projectdocument.objects.filter(projectid=project_id)
        serializer = UploadDocSerializer(record,many=True)
        return Response(serializer.data)


class Document_with_projectid_documentid(APIView):
    def get(self,request, project_id,document_id):
        records = Documents.objects.filter(projectid= project_id,id=document_id)
        serializer = DocumentsSerializer(records,many=True)
        return Response(serializer.data)

#@decorator
@api_view(['get'])
def getcmp(request):
    #perm=Auth(request)
    param = True
    if(param==True):
        records = Company.objects.all()
        serializer = CompanySerializer(records, many=True)
        return Response(serializer.data)
    else:
        return "Wrong Token"

@api_view(['post'])
def postcmp(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyList(APIView):
    def get(self,request):
        records = Company.objects.all()
        serializer = CompanySerializer(records,many=True)
        #my_header(request.META['HTTP_TOKEN'])
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Company_company_id_get_update_delete(APIView):
    def get(self,request,company_id, Format=None):
        records = Company.objects.get(pk=company_id)
        serializer = CompanySerializer(records)
        return Response(serializer.data)

    def put(self,request,company_id, Format=None):
        records = Company.objects.get(pk=company_id)
        serializer = CompanySerializer(records,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, company_id, format=None):
        user = Company.objects.get(pk=company_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AspnetusersList(APIView):
    def get(self,request):
        documents = Aspnetusers.objects.all()
        serializer = AspnetusersSerializer(documents,many=True)
        return Response(serializer.data)

@api_view(['post'])
def post(request):
        data = request.data
        print('create user',data)
        now = datetime.now()
        format_iso_now = now.isoformat()
        newdate = now + timedelta(days=365)
        data['createddatetime'] = format_iso_now
        data['lockoutenddateutc']= newdate.isoformat()
        data['twofactorenabled']= "1"
        data['lockoutenabled']= "1"
        data['accessfailedcount'] =1
        data['securitystamp'] = "victor"
        data['emailconfirmed'] = "1"
        data['phonenumberconfirmed'] = "1"
        data['token'] = "asd"
        #print(data['lockoutenddateutc'])
        serializer = AspnetusersSerializer(data = data)
        #print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Aspnetusers_update_user(APIView):
    def put(self, request):
        data = request.data
        user = Aspnetusers.objects.get(pk=data['id'])
        print(user.username)
        serializer = AspnetusersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Aspnetusers_get_update_delete(APIView):
    def get(self, request, user_id, format=None):
        user = Aspnetusers.objects.get(pk=user_id)
        serializer = AspnetusersSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        user = Aspnetusers.objects.get(pk=user_id)
        print(request.data)
        serializer = AspnetusersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        user = Aspnetusers.objects.get(pk=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Aspnetusers_of_company(APIView):
    def get(self,request):
        username = request.GET.get('userName')
        company_id = Aspnetusers.objects.get(username=username).companyid
        cursor = open()
        join_query = "Select * from AspNetUsers u join AspNetRoles r on CAST(u.roleid AS INTEGER) = r.id " \
                     "where u.companyid  =" + str(company_id)
        cursor.execute(join_query)
        records = cursor.fetchall()
        dump_records = json.dumps(records, sort_keys=True, default=str)
        loaded_records = json.loads(dump_records)
        return Response(loaded_records)
        # documents = Aspnetusers.objects.filter(companyid=company_id)
        # serializer = AspnetusersSerializer(documents,many=True)
        # return Response(serializer.data)


class AspnetusersWrole(APIView):
    def get(self,request):
        documents = Aspnetusers.objects.all()
        serializer = AspnetusersWrolesSerializer(documents,many=True)
        return Response(serializer.data)


class AspnetusersWithrole(APIView):
    def get(self,request):
        username = request.GET.get('userName')
        company_id = Aspnetusers.objects.get(username=username).companyid
        documents = Aspnetusers.objects.filter(companyid=company_id)
        serializer = AspnetusersWithrolesSerializer(documents,many=True)
        r = json.dumps(serializer.data)
        loaded_r = json.loads(r)
        new_res = list()
        for info in loaded_r:
            mydict = info
            mydict1=mydict['role'][0]
            mydict['role']=mydict1
            new_res.append(mydict)
        #pprint.pprint(new_res, width=4)
        #print(loaded_r[0]['role'][0])
        return Response(new_res)

class users_by_projectid(APIView):
    def get(self,request,project_id):
        users = Aspnetusers.objects.filter(projectid=project_id)
        serializer = AspnetusersSerializer(users, many=True)
        return Response(serializer.data)

class Aspnetusers_of_username(APIView):
    def get(self,request,user_name):
        documents = Aspnetusers.objects.filter(username=user_name)
        serializer = AspnetusersSerializer(documents,many=True)
        return Response(serializer.data)


class AspnetrolesList(APIView):
    def get(self,request):
        documents = Aspnetroles.objects.all()
        serializer = AspnetrolesSerializer(documents,many=True)
        return Response(serializer.data)

    def post(self, request, Format=None):
        serializer = AspnetrolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    def get(self, request, user_name):
        print(user_name)
        records = Project.objects.all()
        serializer = ProjectSerializer(records,many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Project_project_id_get_update_delete(APIView):
    def get(self,request,project_id,Format=None):
        records = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(records)
        return Response(serializer.data)

    def put(self,request,project_id, Format=None):
        record = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(record,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, format=None):
        record = Project.objects.get(pk=project_id)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Projects_of_company(APIView):
    def get(self,request):
        username = request.GET.get('userName')
        company_id = Aspnetusers.objects.get(username=username).companyid
        records = Project.objects.filter(companyid=company_id)
        serializer = ProjectSerializer(records,many=True)
        return  Response(serializer.data)

class Projects_Create(APIView):
    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersJoinList(APIView):
    def get(self,request):
        cursor = open()
        query = "SELECT documents.projectid FROM documents INNER JOIN project on documents.projectid = project.projectid"
        cursor.execute(query)
        records = cursor.fetchall()
        r = json.dumps(records)
        loaded_r = json.loads(r)
        return Response(loaded_r)


class Aspnetusers_join_aspnetroles(APIView):
    def get(self,request, user_name):
        cursor = open()
        join_query = "select r.name, U.* from (select * from aspnetusers where companyid in " \
                "(select companyid from aspnetusers where username=" + "'" + user_name + "'" + "limit 1)) as U " \
                "join aspnetroles r on CAST(U.roleid AS INTEGER)=r.id;"
        cursor.execute(join_query)
        records = cursor.fetchall()
        dump_records = json.dumps(records,sort_keys=True, default=str)
        loaded_records = json.loads(dump_records)
        return Response(loaded_records)


class function_of_postgres(APIView):
    def get(self,request):
        cursor = open()
        function_query = "select * from dataget1()"
        cursor.execute(function_query)
        records = cursor.fetchall()
        dump_records = json.dumps(records,sort_keys=True, default=str)
        loaded_records = json.loads(dump_records)
        return Response(loaded_records)


class complex_join_of_postgres(APIView):
    def get(self,request,company_id,status_id):
        cursor = open()
        function_query = "Select u.Id as  Id,(u.FirstName || ' ' || u.LastName) as AssignedTo," \
                         "li.BuilderInterest,li.CmpctLabel,l.CompanyId, l.CreateDateTimeOffset," \
                         "l.CreateUser_ID,l.EditDateTimeOffset,l.EditUser_ID,l.Email,l.Lead_ID," \
                         "l.Name,l.PhoneNumber, li.ProjName,li.QueryRemarks,li.RangeFrom,li.RangeTo," \
                         "li.ReceivedOn,l.Status, li.StatusDate,li.StatusId,li.TypeOfProperty," \
                         "li.LeadItemId from Leads l join LeadItems li on li.Lead_ID = l.Lead_ID" \
                         " join AspNetUsers u on u.Id = li.AssignedTo" \
                         " where li.StatusId =" + str(status_id) + " and u.companyId =" + str(company_id)
        #print(function_query)
        cursor.execute(function_query)
        records = cursor.fetchall()
        dump_records = json.dumps(records,sort_keys=True, default=str)
        loaded_records = json.loads(dump_records)

        return Response(loaded_records)

class LeadsListAll(APIView):
    def get(self,request):
        documents = Leads.objects.all()
        serializer = LeadsSerializer(documents,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class LeadsOneLeads(APIView):
    def get(self,request,lead_id):
        documents = Leads.objects.get(pk=lead_id)
        serializer = LeadsSerializer(documents)
        return Response(serializer.data)

class LeadsListAllCmp(APIView):
    def get(self,request,company_id):
        documents = Leads.objects.filter(companyid=company_id)
        serializer = LeadsSerializer(documents,many=True)
        return Response(serializer.data)

class OtherLeadsByUsername(APIView):
    def get(self,request):
        username = request.GET.get('userName')
        status_id = request.GET.get('statusID')
        #company_id = Aspnetusers.objects.get(username=username).companyid
        cursor = open()
        queryset = "Select y.* from (Select Row_Number() over (order by l.Lead_ID desc) " \
                   "as RowNumber, u.Id as  Id,(u.FirstName || ' ' ||  u.LastName) as userName,li.BuilderInterest," \
                   "li.CmpctLabel,l.CompanyId,l.CreateDateTimeOffset,l.CreateUser_ID, l.EditDateTimeOffset,l.EditUser_ID," \
                   "l.Email,l.Lead_ID,l.Name,l.PhoneNumber,li.ProjName,li.QueryRemarks,li.RangeFrom,li.RangeTo," \
                   "li.ReceivedOn,l.Status,li.StatusDate,li.StatusId,li.TypeOfProperty,li.AssignedTo,li.LeadItemId" \
                   " from Leads l join LeadItems li on li.Lead_ID = l.Lead_ID join AspNetUsers u on u.Id::varchar = li.AssignedTo" \
                   " where u.UserName = '{}' and li.Statusid= {})as y".format(username,status_id)
        cursor.execute(queryset)
        records = cursor.fetchall()
        r = json.dumps(records, indent=4, sort_keys=True, default=str)

        loaded_r = json.loads(r)
        result = get_other_leads(loaded_r)

        return Response(result)
class OtherLeadsC(APIView):
    def get(self,request):
        company_id = request.GET.get('companyid')
        result = other_leads_company_id(company_id)

        return Response(result)

class Add_token(APIView):
    def put(self,request,user_name,token):
        #data = request.data['token']
        Aspnetusers.objects.filter(username = user_name).update(token=token)
        return Response('success')


class Leadsitemss(APIView):
    def get(self,request):
        user_name = request.GET.get('userName')
        pagesize = request.GET.get('pagesize')
        pagenumber = request.GET.get('pagenumber')
        company_id = Aspnetusers.objects.get(username= user_name).companyid
        status = 16
        documents = Leads.objects.filter(companyid=company_id, status=status)
        #serializer = Leads_with_itemsSerializer(documents,many=True)
        # r = json.dumps(serializer.data)
        # loaded_r = json.loads(r)
        serializers = LeadsSerializer(documents, many=True)
        leads_json = json.dumps(serializers.data)
        final_json_leads= json.loads(leads_json)
        user_documents = Aspnetusers.objects.filter(Q(roleid='3') | Q(roleid='4'),companyid= company_id)
        user_serializer = AspnetusersSerializer(user_documents, many=True)
        user_json = json.dumps(user_serializer.data)
        user_json_list = json.loads(user_json)
        print('items user',len(user_json_list))
        #user_len = len(user_json_list)
        #new_res = list(user_len)
        items = list()
        leads_list =list()
        for info in final_json_leads:
            #info = dict()
            info['nextlink'] = ''
            info['assignees'] = ''
            info['leadSource']= 'raw'
            info['pageNumber'] = '0'
            info['pageSize'] = '0'
            info['totalCount'] = '0'
            info['assignedUsers'] = []
            items_list = list()
            for new_user in user_json_list:
                item= dict()
                item['leaditemid']= 0
                item['lead_id']= 0
                item['queryremarks']= "testdata"
                item['typeofproperty']= 2
                item['status']= 10
                item['rangefrom']= 2
                item['rangeto']= 3
                item['cmpctlabel']= "test"
                item['receivedon']= "2018-10-10T00:00:00Z"
                item['projname']= "Himan"
                item['assignedto']= new_user['id']
                item['builderinterest']= "1"
                item['statusid']= 10
                item['statusdate']= "2018-10-10T00:00:00Z"
                item['companyid']= 1
                item['isAssigned'] = False
                item['token'] = ''
                item['userName'] = new_user['firstname'] + new_user['lastname']
                item['leaditemid'] = 0


                # item['lead_id'] = 0
                # item['queryremarks'] = ''
                # item['typeofproperty'] = 0
                # item['status'] = 0
                # item['rangefrom'] = 0
                # item['rangeto'] = 0
                # item['cmpctlabel'] = ''
                # item['receivedon'] = ''
                # item['projname'] = ''
                # item['assignedto'] = new_user['id']
                # item['builderinterest'] = ''
                # item['statusid'] = 0
                # item['statusdate'] = ''
                # item['isAssigned'] = False
                # item['token'] = ''
                # item['userName'] = new_user['firstname'] + new_user['lastname']
                # item['companyid'] = 0
                # item['leaditemid'] = 0
                items_list.append(item)
            info['items']= items_list
            leads_list.append(info)
        paginator = Paginator(leads_list, pagesize)
        page = paginator.page(pagenumber)
        g = page.object_list
        return Response(g)

class LeadsList(APIView):
    def get(self,request,company_id, page_num, status):
        documents = Leads.objects.filter(companyid=company_id, status=status)
        serializer = Leads_with_itemsSerializer(documents,many=True)
        r = json.dumps(serializer.data)
        loaded_r = json.loads(r)
        new_res = list()
        for info in loaded_r:
            #mydict = info
            #mydict1 = mydict['role'][0]
            info['nextlink'] = 'vc.com/abv'
            info['assignees'] = ''
            info['leadSource']= 'raw'
            info['pageNumber'] = '0'
            info['pageSize'] = '0'
            info['totalCount'] = '0'
            info['assignedUsers'] = []
            new_info_item = list()
            for item in info['items']:
                item['companyId'] = 0
                item['isAssigned'] = False
                item['token'] = ''
                item['userName'] = 'Alok Kumar'
                new_info_item.append(item)
            new_res.append(info)
        paginator = Paginator(new_res, 10)
        page = paginator.page(page_num)
        g = page.object_list
        return Response(g)

    def post(self, request, format=None):
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class LeadsWithStatus(APIView):
    def get(self, request, company_id, status_id):
        records = Leads.objects.filter(companyid=company_id, status = status_id)
        serializer = LeadsWithItemsSerializer(records, many=True)
        return Response(serializer.data)



class Leads_items_List(APIView):
    def get(self,request):
        documents = Leaditems.objects.all()
        serializer = LeaditemsSerializer(documents,many=True)
        return  Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeaditemsSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class Upload_excel_file(APIView):
    def post(self,request):
        f = request.FILES['file']
        username= request.GET.get('userName')
        company_id = Aspnetusers.objects.get(username=username).companyid
        #print(f.name)
        myfile = pd.read_excel(f)
        leads = myfile.to_json(orient='records')
        leads= json.loads(leads)
        for lead in leads:
            lead['companyid'] = company_id
            lead['cmpctlabel'] = lead['remarks']
            lead['status'] = 16
            lead['isassigned'] = False

            #print(leads)
        serializer = LeadsExcelSerializer(data=leads, many=True)
        if serializer.is_valid():
            serializer.save()
        #item_data=dict()
        # #item_data['lead_id']=leads[0]['']
        # item_serializer = LeaditemsSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        return Response('success')
# Create your views here.
#select * from leaditems;
from django.shortcuts import render


class Integration_of_company(APIView):
    def get(sself, request ,ccompany_id):
        records = Integrations.objects.filter(companyid=ccompany_id)
        serializer = IntegrationsSerializer(records,many=True)
        return Response(serializer.data)


class Integration_by_integrationid(APIView):
    def get(self, request ,integration_id):
        records = Integrations.objects.filter(id=integration_id)
        serializer = IntegrationsSerializer(records,many=True)
        return Response(serializer.data)


class Recordingsleadid(APIView):
    def get(self, request ,lead_id):
        records = Recordings.objects.filter(id=lead_id)
        serializer = RecordingsSerializer(records,many=True)
        return Response(serializer.data)
    def post(self):
        pass


class AddRecordings(APIView):
    def get(self, request):
        records = Recordings.objects.all()
        serializer = RecordingsSerializer(records,many=True)
        return Response(serializer.data)


    def post (self,request):
        serializer = RecordingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getattendance(APIView):
    def get(self,request,date,username):
        cursor = open()
        query = "Select (u.FirstName + '' + u.LastName) as Name,a.DistanceIn,a.Attendence,a.DateIn,a.DateOut,a.Date,a.DistanceOut,a.AttendanceId from Attendence a join AspNetUsers u on a.UserId = u.UserName where a.Date =" +(date) +" and u.UserName ="+(username)
        cursor.execute(query)
        records = cursor.fetchall()
        r = json.dumps(records, indent=4, sort_keys=True, default=str)
        loaded_r = json.loads(r)
        con.close()
        return Response(loaded_r)


class Token(APIView):
    def post(self, request):
        global token
        token=login(request)
        return HttpResponse(json.dumps(token))


def check_token(func):
   def inner(received_token):
      global token
      print("I am going to check token")
      if received_token != token:
         print("Whoops! Not Authorized")
         return

      return func(token)
   return inner



@api_view(['post'])
def login(request):
    #print(request.META)
    if (request.META['CONTENT_TYPE'] == 'application/x-www-form-urlencoded' and request.data['grant_type']=='password'):
        user_name = request.data['username']
        #print(user_name)
        user = Aspnetusers.objects.get(username=user_name)
        if(user.passwordhash==request.data['password']):
            response = dict()
            response['CompanyId'] = user.companyid
            response['roleid'] = user.roleid
            response['userName'] = user.username
            response['token_type'] = 'bearer'
            response['access_token'] = create_token(user.username,user.companyid,user.roleid)
    return Response(response)




from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


class LeadstatusCountAPIView(APIView):
    def get(self,request):
        username= request.GET.get('username')
        company_id = Aspnetusers.objects.get(username=username).companyid
        cursor = open()
        query = "Select n.PhoneNumberCount, s.Name,s.StatusID from(Select COUNT(DISTINCT l.Lead_ID) " \
                "as PhoneNumberCount,StatusId from Leads l join LeadItems li on li.Lead_ID = l.Lead_ID  where " \
                "l.CompanyId in ({}) Group by StatusId) as n join LeadStatus s on n.StatusId = s.StatusID UNION Select" \
                " count(Lead_ID) as PhoneNumberCount,'Raw Leads' as Name,{} as StatusID from Leads where CompanyID = {} and" \
                " IsAssigned ={}".format(company_id, 16, company_id, False)
        print(query)
        cursor.execute(query)
        records = cursor.fetchall()
        r = json.dumps(records, indent=4, sort_keys=True, default=str)
        loaded_r = json.loads(r)
        j = len(loaded_r)
        print(loaded_r)
        print(j)
        response = dict()
        response['currentLeadsCount'] = 0
        response['noWorkCount'] = 0
        response['notConnectedCount'] = 0
        response['followUpsCount'] = 0
        response['visitOnCounts'] = 0
        response['visitDoneCount'] = 0
        response['visitDeadCount'] = 0
        response['otherProjectsCount'] = 0
        response['resaleCount'] = 0
        response['alreadyBookedCount'] = 0
        response['bookedDone'] = 0
        response['deadCount'] = 0
        response['rentCount'] = 0
        response['plotCount'] = 0
        response['duplicateCount'] = 0
        response['rawLeadsCount'] = 0
        print('working')
        print('next working')
        i = 0
        while i <= j - 1:
            if loaded_r[i]['statusid'] == 16:
                print(loaded_r[i])
                response['rawLeadsCount'] = loaded_r[i]['phonenumbercount']
                print(response['rawLeadsCount'])
            elif loaded_r[i]['statusid'] == 1:
                print(loaded_r[i])
                response['currentLeadsCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 2:
                response['noWorkCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 3:
                response['notConnectedCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 4:
                response['followUpsCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 5:
                response['visitOnCounts'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 6:
                response['visitDoneCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 7:
                response['visitDeadCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 8:
                response['otherProjectsCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 9:
                response['resaleCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 10:
                response['alreadyBookedCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 11:
                response['bookedDone'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 12:
                response['deadCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 13:
                response['rentCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 14:
                response['plotCount'] = loaded_r[i]['phonenumbercount']
            elif loaded_r[i]['statusid'] == 15:
                response['duplicateCount'] = loaded_r[i]['phonenumbercount']
            i = i + 1
        con.close()
        print('end')
        print(type(response))
        return Response(response)
@api_view(['get'])
def lead_status_count(request,company_id):
    cursor = open()
    query = "Select n.PhoneNumberCount, s.Name,s.StatusID from(Select COUNT(DISTINCT l.Lead_ID) " \
            "as PhoneNumberCount,StatusId from Leads l join LeadItems li on li.Lead_ID = l.Lead_ID  where " \
            "l.CompanyId in ({}) Group by StatusId) as n join LeadStatus s on n.StatusId = s.StatusID UNION Select" \
            " count(Lead_ID) as PhoneNumberCount,'Raw Leads' as Name,{} as StatusID from Leads where CompanyID = {} and" \
            " IsAssigned ={}".format(company_id, 16, company_id, False)
    print(query)
    cursor.execute(query)
    records = cursor.fetchall()
    r = json.dumps(records, indent=4, sort_keys=True, default=str)
    loaded_r = json.loads(r)
    j = len(loaded_r)
    print(loaded_r)
    print(j)
    response = dict()
    response['currentLeadsCount'] = 0
    response['noWorkCount'] = 0
    response['notConnectedCount'] = 0
    response['followUpsCount'] = 0
    response['visitOnCounts'] = 0
    response['visitDoneCount'] = 0
    response['visitDeadCount'] = 0
    response['otherProjectsCount'] = 0
    response['resaleCount'] = 0
    response['alreadyBookedCount'] = 0
    response['bookedDone'] = 0
    response['deadCount'] = 0
    response['rentCount'] = 0
    response['plotCount'] = 0
    response['duplicateCount'] = 0
    response['rawLeadsCount'] = 0
    print('working')
    print('next working')
    i = 0
    while i <= j - 1:
        if loaded_r[i]['statusid'] == 16:
            print(loaded_r[i])
            response['rawLeadsCount'] = loaded_r[i]['phonenumbercount']
            print(response['rawLeadsCount'])
        elif loaded_r[i]['statusid'] == 1:
            print(loaded_r[i])
            response['currentLeadsCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 2:
            response['noWorkCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 3:
            response['notConnectedCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 4:
            response['followUpsCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 5:
            response['visitOnCounts'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 6:
            response['visitDoneCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 7:
            response['visitDeadCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 8:
            response['otherProjectsCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 9:
            response['resaleCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 10:
            response['alreadyBookedCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 11:
            response['bookedDone'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 12:
            response['deadCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 13:
            response['rentCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 14:
            response['plotCount'] = loaded_r[i]['phonenumbercount']
        elif loaded_r[i]['statusid'] == 15:
            response['duplicateCount'] = loaded_r[i]['phonenumbercount']
        i = i + 1
    con.close()
    print('end')
    print(type(response))
    return Response(response)


@api_view(['get'])
def mobile_status_count(request, company_id):
    response = 'mobile_status_count: ' + str(company_id)
    return Response(response)

class Leads_update_delete(APIView):
    def put(self, request, lead_id, format=None):
        # record = Leads.objects.get(pk=lead_id)
        # item12=
        leads_serializer = LeadsUpdataSerializer(data=request.data)
        # leads_item_serializer = LeaditemsSerializer(record)
        # leads = json.dumps(request.data)
        # leads_list = json.loads(leads)
        # if leads_serializer.is_valid():
        #     print('working',leads_serializer.data)
        #
        # items_list = leads_list['items']
        # for item in items_list:
        #     if(item['lead_id'] != 0):
        #         #print('item',item)
        #         item_serializer = LeaditemsSerializer(data=item)
        #         if item_serializer.is_valid():
        #             #print('items_ser',item_serializer.data)
        #             #item_serializer.validated_data
        #             item_serializer.save()
        if leads_serializer.is_valid():
            leads_serializer.save()
            return Response(leads_serializer.data)
        return Response(leads_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['post'])
def create_lead(request, company_id):
    response = 'new lead: ' + str(company_id)
    return Response(response)


@api_view(['put'])
def Leads_update(request, lead_id):
    #print('type',type(request.data))
    leads = json.dumps(request.data)
    leads_json = json.loads(leads)
    record = Leads.objects.get(pk=lead_id)
    lead_serializer = LeadsSerializer(record, data=leads_json)
    print('received items',leads_json['items'])
    print('items length',len(leads_json['items']))
    lead_items = leads_json['items']
    #item_serializer = LeaditemsSerializer(data=leads_json['items'])
    for item in lead_items:
        if(item['lead_id'] != 0):
            item_serializer = LeaditemsSerializer(data=item)
            if item_serializer.is_valid():
                item_serializer.save()
                print('success item inserted')
    print('type=',type(leads_json))
    if lead_serializer.is_valid():
        lead_serializer.save()
        send_firebase_push_notification = firebase_push_notification()
        return Response(lead_serializer.data)
    return Response(lead_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class locationbyuser(APIView):
    def get(self,request):
        username = request.GET.get('userName')
        cursor = open()
        function_query = "Select * from Location where CompanyId in " \
                         "(Select  CompanyId from AspNetUsers where userName = '{}' LIMIT 1 )".format(username)
        cursor.execute(function_query)
        records = cursor.fetchall()
        dump_records = json.dumps(records,sort_keys=True, default=str)
        loaded_records = json.loads(dump_records)
        print(loaded_records)
        final_output = list()

        for item in loaded_records:
            newd = dict()
            newd['locationID'] = item['locationid']
            newd['title'] = item['username']
            newd['lat'] = item['lattitude']
            newd['lng'] = item['longitude']
            newd['companyID'] = item['companyid']
            newd['description'] = item['username']
            final_output.append(newd)
        return Response(final_output)


@api_view(['get'])
def gtest(request, username):
    response = 'mobile_status_count: ' + username
    return Response(response)

class LeadItems(APIView):

    def put(self,request,Format=None):
        data = request.data
        leaditemid = data['leaditemid']
        records = Leaditems.objects.get(pk = leaditemid)
        serializer = LeaditemsSerializer(records,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)