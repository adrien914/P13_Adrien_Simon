from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from organigramme import views
# Create your tests here.


class TestUrl(SimpleTestCase):
    """Calss used to test the uls"""

    def test_liste_poles_is_resolved(self):
        url = reverse("organigramme:liste_poles")
        self.assertEquals(resolve(url).func.__name__, views.ListePoles.as_view().__name__)

    def test_login_is_resolved(self):
        url = reverse("organigramme:login")
        self.assertEquals(resolve(url).func.__name__, views.Login.as_view().__name__)

    def test_organigramme_is_resolved(self):
        url = reverse("organigramme:organigramme", args=["Pole"])
        self.assertEquals(resolve(url).func.__name__, views.Organigramme.as_view().__name__)

    def test_search_engine_is_resolved(self):
        url = reverse("organigramme:search_engine")
        self.assertEquals(resolve(url).func.__name__, views.SearchEngine.as_view().__name__)

    def test_page_admin_is_resolved(self):
        url = reverse("organigramme:admin")
        self.assertEquals(resolve(url).func.__name__, views.Admin.as_view().__name__)

    def test_modify_fiche_is_resolved(self):
        url = reverse("organigramme:modify_fiche")
        self.assertEquals(resolve(url).func.__name__, views.ModifyFiche.as_view().__name__)

    def test_remove_fiche_is_resolved(self):
        url = reverse("organigramme:remove_fiche")
        self.assertEquals(resolve(url).func.__name__, views.RemoveFiche.as_view().__name__)

    def test_add_fonction_is_resolved(self):
        url = reverse("organigramme:add_fonction")
        self.assertEquals(resolve(url).func.__name__, views.AddFonction.as_view().__name__)

    def test_add_grade_is_resolved(self):
        url = reverse("organigramme:add_grade")
        self.assertEquals(resolve(url).func.__name__, views.AddGrade.as_view().__name__)

    def test_add_groupe_is_resolved(self):
        url = reverse("organigramme:add_groupe")
        self.assertEquals(resolve(url).func.__name__, views.AddGroupe.as_view().__name__)

    def test_add_image_is_resolved(self):
        url = reverse("organigramme:add_image")
        self.assertEquals(resolve(url).func, views.add_image)

    def test_change_rank_is_resolved(self):
        url = reverse("organigramme:change_rank")
        self.assertEquals(resolve(url).func.__name__, views.ChangeRank.as_view().__name__)

    def test_page_admin_params_is_resolved(self):
        url = reverse("organigramme:admin_param", args=["1"])
        self.assertEquals(resolve(url).func.__name__, views.Admin.as_view().__name__)
