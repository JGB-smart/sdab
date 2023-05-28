# Generated by Django 4.2 on 2023-05-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=150, verbose_name='curso')),
                ('descripcion', models.CharField(max_length=150, verbose_name='descripcion')),
                ('Fcurso', models.DateField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='profesores.materias')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encargado', to='profesores.profesores')),
            ],
            options={
                'verbose_name': 'Cursos',
                'verbose_name_plural': 'Cursos',
            },
        ),
    ]