from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .forms import MembershipApplicationForm, VoteForm, InsuranceSurveyForm
from .models import Motion
import os


class ClubMemberLoginTests(TestCase):
    def setUp(self):
        user = User.objects.create_user('omar', 'omar@ace.org', 'omaramente')

    def test_login_required(self):
        response = self.client.get(reverse('panel'))
        self.assertRedirects(response, '/login/?next=/panel/')

    def test_panel_render_when_logged_in(self):
        self.client.login(username='omar', password='omaramente')
        response = self.client.get(reverse('panel'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Panel")
        self.assertContains(response, "omar")

    def test_init_valid_with_entry(self):
        data = {
            'username': 'omar',
            'password': 'omaramente',
        }
        form = LoginForm(data)
        self.assertTrue(form.is_valid())

    def test_init_invalid_username(self):
        data = {
            'username': 'omar',
            'password': 'wrong',
        }
        form = LoginForm({data})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['Username is incorrect.'],
        })

    def test_init_invalid_password(self):
        data = {
            'username': 'ramo',
            'password': 'omaramente',
        }
        form = LoginForm({data})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'password': ['Password is incorrect.'],
        })

    def test_init_invalid_username_and_password(self):
        form = LoginForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['Username is incorrect.'],
            'password': ['Password is incorrect.'],
        })


class MembershipApplicationViewTests(TestCase):
    def test_membership_application_form_render(self):
        response = self.client.get(reverse('application'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please note that you will need a")


class MembershipApplicationFormTests(TestCase):
    def test_init_invalid_without_entry(self):
        form = MembershipApplicationForm({})
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
        form = MembershipApplicationForm(data, upload_file)
        self.assertFalse(form.is_valid())

    def test_init_invalid_missing_data_returns_errors(self):
        data = {
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
            'medical_expiration': '2016-09-01',
            'reference_name': 'brez',
            'reference_relation': 'Friend',
            'reference_phone': '2122231232',
        }
        form = MembershipApplicationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['Please enter your full name'],
            'email': ['Please enter your email address'],
            'drivers_license_report': ['This field is required.'],
        })


class InsuranceSurveyViewTests(TestCase):
    def test_insurance_survey_form_render(self):
        User.objects.create_user('omar', 'omar@ace.org', 'omaramente')
        self.client.login(username='omar', password='omaramente')
        response = self.client.get(reverse('insurance'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Do have a current BFR")


class InsuranceSurveyFormTests(TestCase):
    def test_init_invalid_without_entry(self):
        form = InsuranceSurveyForm({})
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
        form = MembershipApplicationForm(data, upload_file)
        self.assertFalse(form.is_valid())

    def test_init_invalid_missing_data_returns_errors(self):
        data = {
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
            'medical_expiration': '2016-09-01',
            'reference_name': 'brez',
            'reference_relation': 'Friend',
            'reference_phone': '2122231232',
        }
        form = MembershipApplicationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['Please enter your full name'],
            'email': ['Please enter your email address'],
            'drivers_license_report': ['This field is required.'],
        })


class VoteViewTests(TestCase):
    def setUp(self):
        user = User.objects.create_user('omar', 'omar@ace.org', 'omaramente')
        Motion.objects.create(made_by=user, body='Motion test')

    def test_login_required(self):
        response = self.client.get(reverse('vote', kwargs={'motion': '1'}))
        self.assertRedirects(response, '/login/?next=/vote/1/')

    def test_vote_form_render_when_logged_in(self):
        self.client.login(username='omar', password='omaramente')
        response = self.client.get(reverse('vote', kwargs={'motion': '1'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Motion test")

    def test_init_valid_with_entry(self):
        data = {
            'yay': True
        }
        form = VoteForm(data)
        self.assertTrue(form.is_valid())

    def test_init_invalid_without_entry(self):
        form = VoteForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'yay': ['This field is required.'],
        })
