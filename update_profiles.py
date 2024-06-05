import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from userauths.models import User, Profile

# Update profiles
profiles_data = [
    {
        "user_email": "admin@example.com",
        "about": "Admin profile description",
        "gender": "Male",
        "country": "Germany",
        "state": "Berlin",
        "city": "Berlin",
        "address": "Admin Address"
    },
    {
        "user_email": "john.doe@example.com",
        "about": "John's profile description",
        "gender": "Male",
        "country": "Germany",
        "state": "Bavaria",
        "city": "Munich",
        "address": "John's Address"
    },
    {
        "user_email": "jane.smith@example.com",
        "about": "Jane's profile description",
        "gender": "Female",
        "country": "Germany",
        "state": "Hamburg",
        "city": "Hamburg",
        "address": "Jane's Address"
    }
]

for data in profiles_data:
    try:
        user = User.objects.get(email=data["user_email"])
        profile = Profile.objects.get(user=user)
        profile.about = data["about"]
        profile.gender = data["gender"]
        profile.country = data["country"]
        profile.state = data["state"]
        profile.city = data["city"]
        profile.address = data["address"]
        profile.save()
        print(f"Updated profile for user {user.email}")
    except User.DoesNotExist:
        print(f"User with email {data['user_email']} does not exist")
    except Profile.DoesNotExist:
        print(f"Profile for user {data['user_email']} does not exist")
