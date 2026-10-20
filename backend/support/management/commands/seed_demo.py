from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from support.models import Category, Role


class Command(BaseCommand):
    help = "Create local-development demo accounts and ticket categories."

    def handle(self, *args, **options):
        for name in ["Hardware", "Software", "Network", "Account Access", "Other"]:
            Category.objects.get_or_create(name=name)
        users = [("employee", Role.EMPLOYEE), ("technician", Role.TECHNICIAN), ("supervisor", Role.SUPERVISOR), ("admin", Role.ADMIN)]
        for username, role in users:
            user, created = User.objects.get_or_create(username=username, defaults={"first_name": role.title().replace("_", " ")})
            if created: user.set_password("ChangeMe123!"); user.save()
            if username == "admin":
                user.is_staff = True
                user.is_superuser = True
                user.save(update_fields=["is_staff", "is_superuser"])
            user.profile.role = role; user.profile.save()
        self.stdout.write(self.style.SUCCESS("Demo users and categories are ready."))
