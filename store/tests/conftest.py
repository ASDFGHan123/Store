import os
import django
import pytest
from django.conf import settings
from rest_framework.test import APIClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

if not settings.configured:
    django.setup()




@pytest.fixture
def api_client():
    return APIClient()