from django.test import TestCase, Client
from django.urls import reverse
from organigramme.models import Pole, Fiche, Groupe, Fonction, Grade
from django.contrib.auth.models import User


class TestListePoles(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_poles = reverse('organigramme:liste_poles')

    def test_ListePoles_GET(self):
        response = self.client.get(self.list_poles)
        self.assertEquals(response.status_code, 200)
        response = self.client.get('/zfqfzq')
        self.assertEquals(response.status_code, 404)


class TestOrganigramme(TestCase):

    def setUp(self):
        self.client = Client()
        self.pole = Pole.objects.create(nom="test", group=1, classement=1)

    def test_get_organigramme_page(self):
        response = self.client.get(reverse('organigramme:organigramme', args=['test']))
        self.assertEqual(response.status_code, 200)

    def test_registration_invalid_pole(self):
        response = self.client.get(reverse('organigramme:organigramme', args=['tes']))
        self.assertEqual(response.status_code, 302)


class TestAdmin(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test", is_superuser=True)
        self.fiche = Fiche.objects.create(id=1, nom="test", rang_affichage=1)

    def test_page_admin_redirect_not_connected_users(self):
        self.client.login()
        self.client.logout()
        response = self.client.get(reverse("organigramme:admin"))
        self.assertEqual(response.status_code, 302)

    def test_page_admin_connected_no_id_specified(self):
        self.client.login(username="test", password="test") 
        response = self.client.get(reverse("organigramme:admin"))
        self.assertEqual(response.status_code, 200)

    def test_page_admin_connected_right_id_specified(self):
        self.client.login(username="test", password="test")
        response = self.client.get(reverse("organigramme:admin_param", args=["1"]))
        self.assertEqual(response.status_code, 200)

    def test_page_admin_connected_wrong_id_specified(self):
        self.client.login(username="test", password="test")
        response = self.client.get(reverse("organigramme:admin_param", args=["2"]))
        self.assertEqual(response.status_code, 302)

class TestSearchEngine(TestCase):

    def setUp(self):
        self.client = Client()
        self.fiche = Fiche.objects.create(id=1, nom="test", rang_affichage=1)

    def test_search_engine(self):
        response = self.client.post(reverse("organigramme:search_engine"), {"text": "test"})
        self.assertEqual(response.status_code, 200)


class TestModifyFiche(TestCase):

    def setUp(self):
        self.client = Client()
        self.fiche = Fiche.objects.create(id=1, nom="fiche", rang_affichage=1)
        self.pole = Pole.objects.create(id=1, nom="pole", group=1, classement=1)
        self.groupe = Groupe.objects.create(id=1, nom="groupe", importance=1)
        self.fonction = Fonction.objects.create(id=1, nom="fonction")
        self.grade = Grade.objects.create(id=1, nom="grade")

    def test_ModifyFiche_exists(self):
        data = {
            "id": 1,
            "nom": "modified fiche",
            "email": "email",
            "pole": "pole",
            "groupe": "groupe",
            "fonction": "fonction",
            "grade": "grade",
            "rang_affichage": 1,
        }
        response = self.client.post(reverse("organigramme:modify_fiche"), data)
        self.assertEqual(response.status_code, 200)
        for key in data:
            self.assertTrue(data[key] == self.fiche[key])
