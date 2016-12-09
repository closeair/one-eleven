from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .forms import DocumentForm
from .models import Document
import os


class CommonsUploadFormTests(TestCase):
    def test_init_invalid_without_entry(self):
        form = DocumentForm({})
        self.assertFalse(form.is_valid())

    def test_init_valid_with_entry(self):
        data = {
            'name': 'Robert Clements',
            'email': 'roger@ace.org',
            'phone': '212-123-1232',
            'birth_date': '1942-09-01',
            'address': '234 Omar Road',
            'city': 'Brooklyn',
            'state_abbreviation': 'NY',
            'zipcode': '11209',
            'united_states_citizen': True,
            'faa_certificate_number': '1234567F',
            'total_flight_hours': '200',
            'bfr_expiration': '2017-09-01',
            'medical_expiration': '2016t-09-01',
            'reference_name': 'brez',
            'reference_relation': 'Friend',
            'reference_phone': '2122231232',
        }
        fixture_file = open('%s/club/fixtures/illegitimi.pdf' % os.getcwd(), 'rb')
        upload_file = {'drivers_license_report': SimpleUploadedFile(fixture_file.name, fixture_file.read())}
        form = DocumentForm(data, upload_file)
        self.assertFalse(form.is_valid())

class CommonsUploadedViewTests(TestCase):
    def test_uploaded_view(self):
        document = Document(name='example', uploaded_file="example.jpg")
        response = self.client.get(reverse('uploaded'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "successfully uploaded")


class AircraftFleetViewTests(TestCase):
    fixtures = ['aircraft']
    def test_public_display_of_fleet(self):
        response = self.client.get(reverse('fleet'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "N5272R")
