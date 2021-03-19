from organigramme.models import Fiche, Pole, Groupe, Fonction, Grade
from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class ModelsTestCase(TestCase):
    def setUp(self) -> None:
        self.pole = Pole.objects.create(
            nom="pole test",
            group=1,
            classement=1,
        )
        self.fonction = Fonction.objects.create(
            nom="fonction test",
        )
        self.groupe = Groupe.objects.create(
            nom="groupe test",
            importance=1,
        )
        self.grade = Grade.objects.create(
            nom="grade test"
        )
        self.fake_pole = Pole.objects.create(
            nom="fake_pole test",
            group=1,
            classement=1,
        )
        self.fake_fonction = Fonction.objects.create(
            nom="fake_fonction test",
        )
        self.fake_groupe = Groupe.objects.create(
            nom="fake_groupe test",
            importance=1,
        )
        self.fake_grade = Grade.objects.create(
            nom="fake_grade test"
        )
        self.fiche = Fiche.objects.create(
            nom="pedro sancho",
            email="test@test.test",
            telephone="0123456789",
            fax="fax test",
            rang_affichage=1,
            image="pas_image.jpg",
            pole=self.pole,
            fonction=self.fonction,
            groupe=self.groupe,
            grade=self.grade,
        )

    def test_pole_valid(self):
        pole = self.pole
        self.assertEqual(pole.nom, "pole test")
        self.assertEqual(pole.group, 1)
        self.assertEqual(pole.classement, 1)
        self.assertNotEqual(pole.nom, "pole teste")
        self.assertNotEqual(pole.group, 2)
        self.assertNotEqual(pole.classement, 2)

    def test_pole_no_duplicates(self):
        self.assertRaises(
            IntegrityError,
            lambda: Pole.objects.create(
                nom="pole test",
                group=1,
                classement=1,
            )
        )

    def test_fonction_valid(self):
        fonction = self.fonction
        self.assertEqual(fonction.nom, "fonction test")
        self.assertNotEqual(fonction.nom, "fonction teste")

    def test_fonction_no_duplicates(self):
        self.assertRaises(
            IntegrityError,
            lambda: Fonction.objects.create(
                nom="fonction test",
            )
        )

    def test_groupe_valid(self):
        groupe = self.groupe
        self.assertEqual(groupe.nom, "groupe test")
        self.assertEqual(groupe.importance, 1)
        self.assertNotEqual(groupe.nom, "groupe teste")
        self.assertNotEqual(groupe.importance, 2)

    def test_groupe_no_duplicates(self):
        self.assertRaises(
            IntegrityError,
            lambda: Groupe.objects.create(
                nom="groupe test",
                importance=2,
            )
        )

    def test_grade_valid(self):
        grade = self.grade
        self.assertEqual(grade.nom, "grade test")
        self.assertNotEqual(grade.nom, "grade teste")

    def test_grade_no_duplicates(self):
        self.assertRaises(
            IntegrityError,
            lambda: Grade.objects.create(
                nom="grade test",
            )
        )

    def test_fiche_valid(self):
        fiche = self.fiche
        self.assertEqual(fiche.nom, "pedro sancho")
        self.assertEqual(fiche.email, "test@test.test")
        self.assertEqual(fiche.telephone, "0123456789")
        self.assertEqual(fiche.fax, "fax test")
        self.assertEqual(fiche.rang_affichage, 1)
        self.assertEqual(fiche.image, "pas_image.jpg")
        self.assertEqual(fiche.pole, self.pole)
        self.assertEqual(fiche.fonction, self.fonction)
        self.assertEqual(fiche.grade, self.grade)
        self.assertEqual(fiche.groupe, self.groupe)

        self.assertNotEqual(fiche.nom, "pedro sanchez")
        self.assertNotEqual(fiche.email, "test@test.teste")
        self.assertNotEqual(fiche.telephone, "0123456781")
        self.assertNotEqual(fiche.fax, "fax teste")
        self.assertNotEqual(fiche.rang_affichage, 2)
        self.assertNotEqual(fiche.image, "pas_imagee.jpg")
        self.assertNotEqual(fiche.pole, self.fake_pole)
        self.assertNotEqual(fiche.fonction, self.fake_fonction)
        self.assertNotEqual(fiche.grade, self.fake_grade)
        self.assertNotEqual(fiche.groupe, self.fake_groupe)

    def test_fiche_no_duplicates(self):
        try:
            Fiche.objects.create(
                nom="pedro sancho",
                email="test@test.test",
                telephone="0123456789",
                fax="fax test",
                rang_affichage=1,
                image="pas_image.jpg",
                pole=self.pole,
                fonction=self.fonction,
                groupe=self.groupe,
                grade=self.grade,
            )
        except IntegrityError:
            self.fail()
