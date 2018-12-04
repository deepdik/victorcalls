from django.test import TestCase






list_dict = list()
list_raw_leads = [
    {
        "assignedto": "77",
        "builderinterest": "1",
        "cmpctlabel": "remarks",
        "companyid": 1,
        "createdatetimeoffset": "",
        "createuser_id": "",
        "editdatetimeoffset": "",
        "edituser_id": "",
        "email": "test@test.com",
        "id": 77,
        "lead_id": 232,
        "leaditemid": 31,
        "name": "zzz",
        "phonenumber": "9818786400",
        "projname": "asd",
        "queryremarks": "query",
        "rangefrom": 10,
        "rangeto": 11,
        "receivedon": '',
        "rownumber": 1,
        "status": 1,
        "statusdate": "",
        "statusid": 1,
        "typeofproperty": 1,
        "username": "aarif faridi"
    },
    {
        "assignedto": "78",
        "builderinterest": "1",
        "cmpctlabel": "remarks",
        "companyid": 1,
        "createdatetimeoffset": "",
        "createuser_id": "",
        "editdatetimeoffset": "",
        "edituser_id": "",
        "email": "test@test.com",
        "id": 77,
        "lead_id": 232,
        "leaditemid": 32,
        "name": "zzz",
        "phonenumber": "9818786400",
        "projname": "asd",
        "queryremarks": "query",
        "rangefrom": 10,
        "rangeto": 11,
        "receivedon": "",
        "rownumber": 2,
        "status": 1,
        "statusdate": "",
        "statusid": 1,
        "typeofproperty": 1,
        "username": "aarif faridi"
    },
{
        "assignedto": "77",
        "builderinterest": "1",
        "cmpctlabel": "remarks",
        "companyid": 1,
        "createdatetimeoffset": "",
        "createuser_id": "",
        "editdatetimeoffset": "",
        "edituser_id": "",
        "email": "test@test.com",
        "id": 77,
        "lead_id": 233,
        "leaditemid": 33,
        "name": "zzz",
        "phonenumber": "9818786400",
        "projname": "asd",
        "queryremarks": "query",
        "rangefrom": 10,
        "rangeto": 11,
        "receivedon": "",
        "rownumber": 2,
        "status": 1,
        "statusdate": "",
        "statusid": 1,
        "typeofproperty": 1,
        "username": "aarif faridi"
    },
{
        "assignedto": "77",
        "builderinterest": "1",
        "cmpctlabel": "remarks",
        "companyid": 1,
        "createdatetimeoffset": "",
        "createuser_id": "",
        "editdatetimeoffset": "",
        "edituser_id": "",
        "email": "test@test.com",
        "id": 77,
        "lead_id": 238,
        "leaditemid": 34,
        "name": "zzz",
        "phonenumber": "9818786400",
        "projname": "asd",
        "queryremarks": "query",
        "rangefrom": 10,
        "rangeto": 11,
        "receivedon": "",
        "rownumber": 2,
        "status": 1,
        "statusdate": "",
        "statusid": 1,
        "typeofproperty": 1,
        "username": "aarif faridi"
    }
]
new_grouped_assignment = dict()
new_grouped_assignment_3 = dict()
for row in list_raw_leads:
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
#print(new_grouped_assignment_3)
for a in new_grouped_assignment_3:
    #print(a)
    l.append(a)
    #new_ld = dict()

#print(new_grouped_assignment_3[l[0]])
i=0
leadsss=list()
while(i<len(l)):
    new_ld = dict()
    new_ld['lead_id']=l[i]
    new_ld['createuser_id']=row['createuser_id']
    new_ld['createdatetimeoffset']=row['createdatetimeoffset']
    new_ld['edituser_id']=row['edituser_id']
    new_ld['editdatetimeoffset']=row['editdatetimeoffset']
    new_ld['name']=row['name']
    new_ld['email']=row['email']
    new_ld['phonenumber']=row['phonenumber']
    #new_ld['isassigned']=row['isassigned']
    new_ld['companyid']=row['companyid']
    new_ld['cmpctlabel']=row['cmpctlabel']
    new_ld['receivedon']=row['receivedon']
    new_ld['status']=row['status']
    new_ld['items'] = new_grouped_assignment_3[l[i]]
    leadsss.append(new_ld)
    i = i + 1

print(leadsss)
'''
 "assignedto": "77",
        "builderinterest": "1",
        "cmpctlabel": "remarks",
        "companyid": 1,
'''
# # Create your tests here.
# alphabet = ['a','d','o','f']
# def vovels(alpha):
#     vowels=['a','e','o','i','u']
#     if(alpha in vowels):
#         return True
#     else:
#         return False
#
# fvowels = filter(vovels, alphabet)
# #print(fvowels)
# for v in fvowels:
#     print(v)
#
# print('----------------------')
# '''
# output
# a
# o
# '''
# # example 2
# randomList = ['a','1',0,True,False,'0']
# filteredList = filter(None,randomList)
# for item in filteredList:
#     print(item)
#
# print('----------------------')
# i= 6
# # if filter(i):
# import datetime
# now = datetime.datetime.now()
# format_iso_now = now.isoformat()
# print(format_iso_now)