import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django

django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for _ in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        usr = User.objects.get_or_create(FirstName=fake_fname, LastName=fake_lname, Email=fake_email)[0]
        # print(usr)


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populate complete!")
