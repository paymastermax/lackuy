# Generated by Django 3.0.6 on 2020-06-01 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('chat_uid', models.AutoField(primary_key=True, serialize=False)),
                ('chat_content', models.CharField(max_length=1024)),
                ('chat_time', models.DateTimeField(auto_now_add=True)),
                ('current_user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_user_bridge', to='signup.Signup')),
                ('opponent_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent_user_bridge', to='signup.Signup')),
            ],
            options={
                'db_table': 'Chats',
            },
        ),
    ]
