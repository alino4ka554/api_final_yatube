# Generated by Django 3.2.16 on 2025-03-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_follow_prevent_self_follow'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='prevent_self_follow',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]
