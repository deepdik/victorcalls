from datetime import datetime, timedelta
from django.http import HttpRequest, HttpResponse
import jwt
from functools import wraps
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from functools import wraps
from django.http import HttpResponseRedirect

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
jwt_token = 'token' # fake token
new_token = 'zzz'
import requests
import json
#select * from AspnetUsers;

con = psycopg2.connect(dbname='LeadPolice', user='postgres', host='50.63.167.106', password='Modinagar@7')
def open():
    global con
    #cur = con.cursor()
    con = psycopg2.connect(dbname='LeadPolice', user='postgres', host='50.63.167.106', password='Modinagar@7')
    cur = con.cursor(cursor_factory=RealDictCursor)
    return cur


def close(cur):
    global con
    con.commit()
    cur.close()
    con.close()
    return True
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20


def create_token(user_name,company_id,role_id):
    global jwt_token
    payload = {
        "user": user_name,
        "comapnyid": company_id,
        "roleid": role_id,
        "exp": datetime.utcnow() + timedelta(seconds=900)
        }
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return jwt_token.decode('utf-8')


# def decorator(function):
#     @wraps(function)
#     def wrap(request):
#         print(request.META)
#         content = request.META['HTTP_AUTHORIZATION'].split()
#         token = content[1]
#         print(token)
#         data = jwt.decode(token, JWT_SECRET)
#         return function(request, *args, **kwargs)
#     return wrap

def Auth(request, *args, **kwargs):
    content =request.META['HTTP_AUTHORIZATION']
    #print(request.META)
    # h = json.dumps(content['HTTP_AUTHORIZATION'])
    # print(content)
    # print(type(content))
    sp=list(content.split(" "))
    token=(sp[1])
    #print(type(sp))
    data = jwt.decode(token,JWT_SECRET )
    #print (data)
    return True

def other_leads_company_id(company_id):
    queryset = "Select u.Id as  Id,(u.FirstName || ' ' || u.LastName) as userName,li.BuilderInterest,li.CmpctLabel," \
               "l.CompanyId,l.CreateDateTimeOffset,l.CreateUser_ID,l.EditDateTimeOffset,l.EditUser_ID,l.Email,l.Lead_ID," \
               "l.Name,l.PhoneNumber,li.ProjName,li.QueryRemarks,li.RangeFrom,li.RangeTo,li.ReceivedOn,l.Status, li.StatusDate," \
               "li.StatusId,li.TypeOfProperty,li.AssignedTo,li.LeadItemId from Leads l join LeadItems li on " \
               "li.Lead_ID = l.Lead_ID join AspNetUsers u on u.Id::varchar = li.AssignedTo where l.CompanyId = {} " \
               "and li.StatusId =1".format(company_id)
    cursor = open()
    cursor.execute(queryset)
    records = cursor.fetchall()
    r = json.dumps(records, indent=4, sort_keys=True, default=str)
    loaded_r = json.loads(r)
    result = get_other_leads(loaded_r)
    return result

def get_other_leads(leads):
    #print(leads)
    new_grouped_assignment_3 = dict()
    for row in leads:
        if row['lead_id'] not in new_grouped_assignment_3:
            new_grouped_assignment_3[row['lead_id']] = [{'lead_id': row['lead_id'],
                                                         'queryremarks': row['queryremarks'],
                                                         'typeofproperty': row['typeofproperty'],
                                                         'status': row['status'],
                                                         'rangefrom': row['rangefrom'],
                                                         'rangeto': row['rangeto'],
                                                         'cmpctlabel': row['cmpctlabel'],
                                                         'receivedon': row['receivedon'],
                                                         'projname': row['projname'],
                                                         'assignedto': row['assignedto'],
                                                         'statusid': row['statusid'],
                                                         'statusdate': row['statusdate'],
                                                         'leaditemid': row['leaditemid'],
                                                         }]
        else:
            new_grouped_assignment_3[row['lead_id']] += [{'lead_id': row['lead_id'],
                                                          'queryremarks': row['queryremarks'],
                                                          'typeofproperty': row['typeofproperty'],
                                                          'status': row['status'],
                                                          'rangefrom': row['rangefrom'],
                                                          'rangeto': row['rangeto'],
                                                          'cmpctlabel': row['cmpctlabel'],
                                                          'receivedon': row['receivedon'],
                                                          'projname': row['projname'],
                                                          'assignedto': row['assignedto'],
                                                          'statusid': row['statusid'],
                                                          'statusdate': row['statusdate'],
                                                          'leaditemid': row['leaditemid']
                                                          }]
    l = []
    # print(new_grouped_assignment_3)
    for a in new_grouped_assignment_3:
        # print(a)
        l.append(a)
        # new_ld = dict()

    # print(new_grouped_assignment_3[l[0]])
    i = 0
    leadsss = list()
    while (i < len(l)):
        new_ld = dict()
        new_ld['lead_id'] = l[i]
        new_ld['createuser_id'] = row['createuser_id']
        new_ld['createdatetimeoffset'] = row['createdatetimeoffset']
        new_ld['edituser_id'] = row['edituser_id']
        new_ld['editdatetimeoffset'] = row['editdatetimeoffset']
        new_ld['name'] = row['name']
        new_ld['email'] = row['email']
        new_ld['phonenumber'] = row['phonenumber']
        # new_ld['isassigned']=row['isassigned']
        new_ld['companyid'] = row['companyid']
        new_ld['cmpctlabel'] = row['cmpctlabel']
        new_ld['receivedon'] = row['receivedon']
        new_ld['status'] = row['status']
        new_ld['items'] = new_grouped_assignment_3[l[i]]
        leadsss.append(new_ld)
        i = i + 1
    return leadsss

def firebase_push_notification():
    headers = {"Content-type": "application/json",
               "Authorization": "key=AAAA3Mgl_0Y:APA91bFKigkhtGaXIKoGL60v8hTOT-a4u7OwZ_Y98jK8AlRcqQUcLjmtDHMCuY9i5am54h7XMQzgWSpQS5YusFJ5P5Nym2YqccghCf4EMeVtGcGemwKf_bOsXCqM86GK3r2hCSoDt3yAlp5v2UncAh6gQ1h3UF6YnA"}
    url = "https://fcm.googleapis.com/fcm/send"
    data = {
        "to": "c48U7eFCyLQ:APA91bFSgMTzQOnMD7EbGdMrxTm_y9I4RTskWVSpsqyk2fhYg5POE6sS0Octb8xY2QHsyHtsy00EXIC26wdtji_XFRsY-bDAWfj-Ee_4CUh8DpV1mIvgJd55P7BCyXCncBl2t5FTZ0Nx",
        "notification": {
            "title": "success",
            "body": "hello ",
            "story_id": "story_12345"
        }
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response_body = response.json()
    #print(response_body)
    return response_body