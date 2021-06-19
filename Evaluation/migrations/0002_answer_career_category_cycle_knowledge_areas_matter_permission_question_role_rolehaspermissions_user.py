# Generated by Django 3.2.4 on 2021-06-18 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('School_Of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.school_of')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cycle_active', models.CharField(max_length=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('second_last_name', models.CharField(max_length=60)),
                ('identify', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
                ('profile_path_img', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('Career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.career')),
            ],
        ),
        migrations.CreateModel(
            name='UserHasRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.role')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserHasPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.permission')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.user')),
            ],
        ),
        migrations.CreateModel(
            name='RoleHasPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.permission')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.user')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.category')),
            ],
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('Career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.career')),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge_areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('University', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.university')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.PositiveSmallIntegerField()),
                ('Cycle', models.CharField(max_length=20)),
                ('Category', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('Knowledge_areas', models.CharField(max_length=30)),
                ('Observation', models.CharField(max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.question')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evaluation.user')),
            ],
        ),
    ]
