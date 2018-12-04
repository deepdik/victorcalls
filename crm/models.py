# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms

class Projectdocument(models.Model):
    name = models.CharField(max_length=50)
    projectid = models.CharField(max_length=20)
    link = models.FileField()

    class Meta:
        managed = True
        db_table = 'projectdocument'


class Aspnetroles(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'aspnetroles'


class Aspnetusers(models.Model):
    #companyid = models.AutoField(primary_key=True)
    #id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256,unique=True)
    passwordhash = models.CharField(max_length=128, blank=True, null=True)
    securitystamp = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    emailconfirmed = models.TextField()  # This field type is a guess.
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    phonenumberconfirmed = models.TextField()  # This field type is a guess.
    twofactorenabled = models.TextField()  # This field type is a guess.
    lockoutenddateutc = models.DateTimeField(blank=True, null=True)
    lockoutenabled = models.TextField()  # This field type is a guess.
    accessfailedcount = models.IntegerField()
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    createddatetime = models.DateTimeField()
    companyid = models.BigIntegerField(blank=True, null=True)
    roleid = models.CharField(max_length=10, blank=True, null=True)
    projectid = models.IntegerField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aspnetusers'


class Attendance(models.Model):
    userid = models.CharField(max_length=50)
    distancein = models.FloatField()
    attendence = models.TextField(blank=True, null=True)  # This field type is a guess.
    datein = models.DateTimeField(blank=True, null=True)
    dateout = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    distanceout = models.FloatField(blank=True, null=True)
    attendanceid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'attendance'


class Company(models.Model):
    companyid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    companyaddress = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    contactpersonname = models.CharField(max_length=50)
    contactphone = models.CharField(max_length=10)
    contactemail = models.CharField(max_length=100)
    activatedtill = models.DateTimeField()
    isactivated = models.TextField()  # This field type is a guess.
    logopath = models.TextField(blank=True, null=True)
    companytype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Companytype(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'companytype'


class Documents(models.Model):
    projectid = models.IntegerField()
    link = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class Integrations(models.Model):
    sourceid = models.IntegerField(blank=True, null=True)
    integrationkey = models.CharField(max_length=50, blank=True, null=True)
    integrationvalue = models.CharField(max_length=500, blank=True, null=True)
    companyid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integrations'


class Jobruns(models.Model):
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    noofleads = models.IntegerField()
    errormessage = models.TextField(blank=True, null=True)
    jobrunid = models.AutoField(primary_key=True)
    companyid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobruns'


class Kwdelhi(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    telephone_number = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kwdelhi'


class Leaditems(models.Model):
    lead_id = models.IntegerField(blank=True, null=True)
    queryremarks = models.CharField(max_length=200, blank=True, null=True)
    typeofproperty = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    rangefrom = models.IntegerField(blank=True, null=True)
    rangeto = models.IntegerField(blank=True, null=True)
    cmpctlabel = models.TextField(blank=True, null=True)
    receivedon = models.DateTimeField(blank=True, null=True)
    projname = models.CharField(max_length=100, blank=True, null=True)
    assignedto = models.CharField(max_length=128, blank=True, null=True)
    builderinterest = models.TextField(blank=True, null=True)  # This field type is a guess.
    statusid = models.IntegerField(blank=True, null=True)
    statusdate = models.DateTimeField(blank=True, null=True)
    leaditemid = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'leaditems'


class Leads(models.Model):
    createuser_id = models.CharField(max_length=128, blank=True, null=True)
    createdatetimeoffset = models.DateTimeField(blank=True, null=True)
    edituser_id = models.CharField(max_length=128, blank=True, null=True)
    editdatetimeoffset = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    phonenumber = models.CharField(max_length=14, blank=True, null=True)
    lead_id = models.AutoField(primary_key=True)
    isassigned = models.NullBooleanField(default=False)  # This field type is a guess.
    companyid = models.BigIntegerField(blank=True, null=True)
    cmpctlabel = models.TextField(blank=True, null=True)
    receivedon = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=150, blank=True, null=True)
    projectname = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    locality = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'leads'


class Leadstatus(models.Model):
    statusid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'leadstatus'


class Location(models.Model):
    userid = models.CharField(max_length=100)
    username = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100)
    companyid = models.IntegerField()
    locationid = models.AutoField(primary_key=True)
    lastupdated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Project(models.Model):
    projectid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    lattitude = models.CharField(max_length=100, blank=True, null=True)
    companyid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class Recording(models.Model):
    record = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording'


class Recordings(models.Model):
    lead_id = models.IntegerField()
    name = models.CharField(max_length=250)
    createdatetime = models.DateTimeField()
    createdby = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'recordings'


class Refreshtokens(models.Model):
    subject = models.CharField(max_length=50)
    clientid = models.CharField(max_length=50)
    issuedutc = models.DateTimeField()
    expiresutc = models.DateTimeField()
    protectedticket = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'refreshtokens'


class Sourcetypes(models.Model):
    source = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sourcetypes'


class Userattendance(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    date = models.DateTimeField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    attendance = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userattendance'