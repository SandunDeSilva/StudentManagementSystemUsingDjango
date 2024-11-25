from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# Create your tests here.

class StudentAPITestCase(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Sandun",
            last_name="de Silva",
            email="sandun@gmail.com",
            date_of_birth="1997-08-01"
        )
        self.create_url = "/api/students/create/"
        self.detail_url = f"/api/students/{self.student.id}/"

    def test_get_students(self):
        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        data = {
            "first_name": "Sanjaya",
            "last_name": "de Silva",
            "email": "sanjaya@gmail.com",
            "date_of_birth": "1997-08-02"
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_student_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], self.student.first_name)
        