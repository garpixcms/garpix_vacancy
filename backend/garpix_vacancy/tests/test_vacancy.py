from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from .data_generation import generate_employment_types, generate_vacancies, generate_tags, generate_contact_types, \
    generate_contacts, generate_applications
from ..models import EmploymentType, Tag, ContactType, Contact, Vacancy
from ..models.application import VacancyApplication


class VacancyApiTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.employment_types = [EmploymentType.objects.create(**data) for data in generate_employment_types()]

        self.tags = [Tag.objects.create(**data) for data in generate_tags()]

        self.contacts_types = [ContactType.objects.create(**data) for data in generate_contact_types()]

        contacts_data = generate_contacts()

        self.contacts = []

        for i in range(len(contacts_data)):
            self.contacts.append(Contact.objects.create(
                contact_type=self.contacts_types[i],
                **contacts_data[i]
            ))

        self.vacancies = [Vacancy.objects.create(**data) for data in generate_vacancies()]

        for vac in self.vacancies:
            vac.employment_types.set(self.employment_types)
            vac.contacts.set(self.contacts)
            vac.tags.set(self.tags)
            vac.save()

        self.vacancy_applications = [VacancyApplication.objects.create(**data) for data in generate_applications()]

        for app in self.vacancy_applications:
            app.vacancy = self.vacancies[0]
            app.save()

    def test_templates(self):
        response = self.client.get(
            reverse("garpix_vacancy:vacancies")
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse("garpix_vacancy:vacancy", args=[self.vacancies[0].pk])
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse("garpix_vacancy:vacancy_application", args=[self.vacancy_applications[0].pk])
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse("garpix_vacancy:vacancy_applications")
        )
        self.assertEqual(response.status_code, 200)

    def test_api(self):
        response = self.client.get(
            reverse("garpix_vacancy:api_vacancy-detail", args=[self.vacancies[0].pk])
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse("garpix_vacancy:api_vacancy-list")
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse("garpix_vacancy:api_vacancy_application-detail", kwargs={"vacancy_pk": self.vacancies[0].pk, "pk": self.vacancy_applications[0].pk})
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            reverse("garpix_vacancy:api_vacancy_application-list", kwargs={"vacancy_pk": self.vacancies[0].pk})
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse("garpix_vacancy:api_vacancy_application-list", kwargs={"vacancy_pk": self.vacancies[0].pk}),
            data=generate_applications()[0]
        )
        self.assertEqual(response.status_code, 201)
