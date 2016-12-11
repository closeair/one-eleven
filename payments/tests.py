from django.test import TestCase
from django.urls import reverse


class InvoiceGenerationTests(TestCase):
    def test_generation_of_montly_invoice_for_member(self):
        self.assertTrue(False)

    def test_ensure_invoice_as_individual_items(self):
        self.assertTrue(False)

    def test_ensure_invoice_as_recurring_charges(self):
        self.assertTrue(False)


class InvoiceDisplayTests(TestCase):
    def test_list_of_historical_invoices_for_member(self):
        self.assertTrue(False)

    def test_display_unpaid_status_on_invoice_in_list(self):
        self.assertTrue(False)

    def test_specific_invoice_and_invoice_items(self):
        self.assertTrue(False)


class InvoicePaymentTests(TestCase):
    def test_payment_of_invoice_with_new_card(self):
        self.assertTrue(False)

    def test_payment_of_invoice_with_card_on_file(self):
        self.assertTrue(False)

    def test_payment_of_invoice_as_recurring_charge(self):
        self.assertTrue(False)


class InvoicePaymentWithStripeTests(TestCase):
    def test_payment_of_invoice_with_new_card(self):
        self.assertTrue(False)

    def test_payment_of_invoice_with_card_on_file(self):
        self.assertTrue(False)

    def test_payment_of_invoice_as_recurring_charge(self):
        self.assertTrue(False)
