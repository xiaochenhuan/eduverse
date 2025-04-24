from django.test import TestCase, Client
from django.urls import reverse
from .models import District, School

class SchoolViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.district = District.objects.create(name="Sample District", state="XY")
        self.school = School.objects.create(
            name="Test School",
            city="Test City",
            state="XY",
            zip="12345",
            district=self.district,
            latitude=0.0,
            longitude=0.0,
            enrollment=500
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_school_list_view(self):
        response = self.client.get(reverse('school_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test School")

    def test_school_detail_view(self):
        response = self.client.get(reverse('school_detail', args=[self.school.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.school.name)
