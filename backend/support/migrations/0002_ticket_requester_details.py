# Generated manually to preserve existing ticket records while requiring these fields for new tickets.
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("support", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="requester_department",
            field=models.CharField(default="", max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticket",
            name="requester_position",
            field=models.CharField(default="", max_length=120),
            preserve_default=False,
        ),
    ]
