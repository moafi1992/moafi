# Generated by Django 3.0.3 on 2020-04-16 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(auto_created=True)),
                ('security_code', models.CharField(max_length=64)),
                ('seller_name', models.CharField(max_length=128)),
                ('seller_num', models.CharField(max_length=128)),
                ('seller_add', models.CharField(blank=True, max_length=512, null=True)),
                ('buyer_name', models.CharField(max_length=128)),
                ('buyer_num', models.CharField(max_length=128)),
                ('buyer_add', models.CharField(blank=True, max_length=512, null=True)),
                ('c_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.IntegerField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('dis_percent', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_invoice.Factor')),
            ],
        ),
        migrations.AddField(
            model_name='factor',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_invoice.Guest'),
        ),
    ]
