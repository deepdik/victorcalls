


def get_other_leads(leads):
    new_grouped_assignment_3 = dict()
    for row in leads:
        if row["lead_id"] not in new_grouped_assignment_3:
            new_grouped_assignment_3[row["lead_id"]] = [{'lead_id': row['lead_id'],
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
            new_grouped_assignment_3[row["lead_id"]] += [{'lead_id': row['lead_id'],
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
