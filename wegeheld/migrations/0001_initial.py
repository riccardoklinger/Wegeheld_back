# Generated by Django 2.0.2 on 2018-03-27 17:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_map', models.CharField(max_length=60)),
                ('name_app', models.CharField(max_length=60)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetnumber', models.CharField(max_length=40)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['town', 'street'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenseplate', models.CharField(max_length=70)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['brand', 'crdate'],
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tmstmp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['list_position', 'crdate'],
            },
        ),
        migrations.CreateModel(
            name='CarColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('hexValue', models.CharField(max_length=7)),
            ],
            options={
                'ordering': ['list_position', 'crdate'],
            },
        ),
        migrations.CreateModel(
            name='EmailText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postalcode', models.CharField(blank=True, max_length=255, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('template', models.CharField(max_length=16500)),
            ],
        ),
        migrations.CreateModel(
            name='Funnysaying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=180)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Offense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=7)),
                ('icon', models.CharField(max_length=120)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['list_position'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=90)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['list_position'],
            },
        ),
        migrations.CreateModel(
            name='PublicAffairsOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postalcode', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=11)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=11)),
                ('date', models.DateTimeField(verbose_name='meldung')),
                ('photos', models.IntegerField(default=0)),
                ('free_text', models.CharField(max_length=255)),
                ('tweet', models.CharField(blank=True, max_length=255)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Action')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Address')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Car')),
                ('funny_saying', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Funnysaying')),
                ('offense', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Offense')),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('list_position', models.IntegerField(default=90)),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['town', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tmstmp', models.DateTimeField(auto_now=True, verbose_name='last edit')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='create')),
                ('deleted', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('postalcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='street',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Town'),
        ),
        migrations.AddField(
            model_name='report',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Reporter'),
        ),
        migrations.AddField(
            model_name='photo',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Report'),
        ),
        migrations.AddField(
            model_name='funnysaying',
            name='valid_offenses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Offense'),
        ),
        migrations.AddField(
            model_name='emailtext',
            name='offense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Offense'),
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.CarBrand'),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.CarColor'),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Street'),
        ),
        migrations.AddField(
            model_name='address',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wegeheld.Town'),
        ),
    ]