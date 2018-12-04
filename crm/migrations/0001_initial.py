# Generated by Django 2.1.2 on 2018-10-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aspnetroles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'aspnetroles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aspnetusers',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=256)),
                ('passwordhash', models.CharField(blank=True, max_length=128, null=True)),
                ('securitystamp', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('emailconfirmed', models.TextField()),
                ('phonenumber', models.CharField(blank=True, max_length=15, null=True)),
                ('phonenumberconfirmed', models.TextField()),
                ('twofactorenabled', models.TextField()),
                ('lockoutenddateutc', models.DateTimeField(blank=True, null=True)),
                ('lockoutenabled', models.TextField()),
                ('accessfailedcount', models.IntegerField()),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('createddatetime', models.DateTimeField()),
                ('companyid', models.BigIntegerField(blank=True, null=True)),
                ('roleid', models.CharField(blank=True, max_length=10, null=True)),
                ('projectid', models.IntegerField(blank=True, null=True)),
                ('token', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aspnetusers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('userid', models.CharField(max_length=50)),
                ('distancein', models.FloatField()),
                ('attendence', models.TextField(blank=True, null=True)),
                ('datein', models.DateTimeField(blank=True, null=True)),
                ('dateout', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('distanceout', models.FloatField(blank=True, null=True)),
                ('attendanceid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'attendance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyid', models.AutoField(primary_key=True, serialize=False)),
                ('companyname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('companyaddress', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('contactpersonname', models.CharField(max_length=50)),
                ('contactphone', models.CharField(max_length=10)),
                ('contactemail', models.CharField(max_length=100)),
                ('activatedtill', models.DateTimeField()),
                ('isactivated', models.TextField()),
                ('logopath', models.TextField(blank=True, null=True)),
                ('companytype', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Companytype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'companytype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.IntegerField()),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'documents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Integrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceid', models.IntegerField(blank=True, null=True)),
                ('integrationkey', models.CharField(blank=True, max_length=50, null=True)),
                ('integrationvalue', models.CharField(blank=True, max_length=500, null=True)),
                ('companyid', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'integrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobruns',
            fields=[
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('noofleads', models.IntegerField()),
                ('errormessage', models.TextField(blank=True, null=True)),
                ('jobrunid', models.AutoField(primary_key=True, serialize=False)),
                ('companyid', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jobruns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kwdelhi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'kwdelhi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leaditems',
            fields=[
                ('lead_id', models.IntegerField(blank=True, null=True)),
                ('queryremarks', models.CharField(blank=True, max_length=200, null=True)),
                ('typeofproperty', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('rangefrom', models.IntegerField(blank=True, null=True)),
                ('rangeto', models.IntegerField(blank=True, null=True)),
                ('cmpctlabel', models.TextField(blank=True, null=True)),
                ('receivedon', models.DateTimeField(blank=True, null=True)),
                ('projname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignedto', models.CharField(blank=True, max_length=128, null=True)),
                ('builderinterest', models.TextField(blank=True, null=True)),
                ('statusid', models.IntegerField(blank=True, null=True)),
                ('statusdate', models.DateTimeField(blank=True, null=True)),
                ('leaditemid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'leaditems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('createuser_id', models.CharField(blank=True, max_length=128, null=True)),
                ('createdatetimeoffset', models.DateTimeField(blank=True, null=True)),
                ('edituser_id', models.CharField(blank=True, max_length=128, null=True)),
                ('editdatetimeoffset', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=80, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=14, null=True)),
                ('lead_id', models.AutoField(primary_key=True, serialize=False)),
                ('isassigned', models.TextField(blank=True, null=True)),
                ('companyid', models.BigIntegerField(blank=True, null=True)),
                ('cmpctlabel', models.TextField(blank=True, null=True)),
                ('receivedon', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('id', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'leads',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leadstatus',
            fields=[
                ('statusid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'leadstatus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('userid', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('longitude', models.CharField(max_length=100)),
                ('lattitude', models.CharField(max_length=100)),
                ('companyid', models.IntegerField()),
                ('locationid', models.AutoField(primary_key=True, serialize=False)),
                ('lastupdated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('lattitude', models.CharField(blank=True, max_length=100, null=True)),
                ('companyid', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'recording',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recordings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('createdatetime', models.DateTimeField()),
                ('createdby', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'recordings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Refreshtokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('clientid', models.CharField(max_length=50)),
                ('issuedutc', models.DateTimeField()),
                ('expiresutc', models.DateTimeField()),
                ('protectedticket', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'refreshtokens',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sourcetypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sourcetypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userattendance',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('attendance', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'userattendance',
                'managed': False,
            },
        ),
    ]
