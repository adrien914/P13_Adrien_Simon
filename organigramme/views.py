from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from organigramme.models import Pole, Fiche, Grade, Fonction, Groupe
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import traceback
from pathlib import Path
from django.contrib.auth import authenticate, login

class ListePoles(View):

    @staticmethod
    def get(request):
        poles = Pole.objects.all().order_by("classement")
        groups = [[], [], [], [], [], []]
        for pole in poles:
            try:
                groups[pole.group].append(pole.nom)
            except:
                groups.append([pole.nom])
        print(groups)
        context = {"groups": groups}
        return render(request, "index.html", context=context)


class Organigramme(View):

    @staticmethod
    def get(request, pole):
        try:
            pole = Pole.objects.get(nom=pole)
        except:
            return redirect("organigramme:liste_poles")
        fiches = Fiche.objects.filter(pole=pole).order_by("rang_affichage")
        groupes = set()  # we use a set at first because we want each group to be there only once
        for fiche in fiches:  # add only groups with published fiches to the list
            if fiche.groupe and fiche.etat == "pub":
                groupes.add(fiche.groupe)
        groupes = list(groupes)
        groupes.sort(key=lambda groupe: groupe.importance)  # sort the groups by importance
        context = {"pole": pole, "fiches": fiches, "groupes": groupes}
        return render(request, "organigramme.html", context=context)


class Admin(View):

    @staticmethod
    def get(request, _id=None):
        if request.user.is_superuser:
            context = {}
            # if there is an id in the url try to find the fiche
            if _id:
                try:
                    context = {"fiche": Fiche.objects.get(id=_id)}
                except:  # if we can't find the fiche redirect to the url without an id
                    return redirect('organigramme:admin')
            # Get all the poles
            context["poles"] = Pole.objects.all()
            context["fonctions"] = Fonction.objects.all()
            try:
                context["grades"] = Grade.objects.all()
            except:
                context["grades"] = []
            context["groupes"] = Groupe.objects.all()
            # Get all the images in media so we can show them in the modal
            images = []
            for extension in ['*.jpg', '*.jpeg', '*.png']:
                for path in Path('media/photos').rglob(extension):
                    image = ''
                    if path.parent.name.split('/')[-1] != 'photos':
                        image += path.parent.name + "/"
                    image += path.name
                    images.append(image)
            context["images"] = images
            return render(request, "admin.html", context)
        else:
            return redirect('organigramme:liste_poles')


class SearchEngine(View):

    @staticmethod
    def post(request):
        """
        Matches fiches based on the text sent in the request
        """
        context = {"propositions": []}
        text = request.POST.get("text", "")
        fiches = Fiche.objects.filter(nom__icontains=text)
        for fiche in fiches:
            context["propositions"].append(str(fiche.id) + ": " + fiche.nom)
        return JsonResponse(context)

class ModifyFiche(View):

    @staticmethod
    def post(request):
        try:
            data = request.POST.dict()
            try:
                data.pop("csrfmiddlewaretoken")
            except:
                pass
            try:
                fiche = Fiche.objects.filter(id=int(data["id"]))
            except:
                fiche = None
            try:
                pole = Pole.objects.get(nom__iexact=data["pole"].rstrip())
                data["pole"] = pole
            except:
                data["pole"] = None
            try:
                grade = Grade.objects.get(nom__iexact=data["grade"].rstrip())
                data["grade"] = grade
            except:
                data["grade"] = None
            try:
                fonction = Fonction.objects.get(nom__iexact=data["fonction"].rstrip())
                data["fonction"] = fonction
            except:
                data["fonction"] = None
            try:
                groupe = Groupe.objects.get(nom__iexact=data["groupe"])
                data["groupe"] = groupe
            except:
                data["groupe"] = None
            data.pop("id")
            if fiche:
                fiche.update(**data)
            else:
                Fiche.objects.create(**data)
            response = JsonResponse({"message": "Success"})
            response.status_code = 200
            return response
        except Exception as e:
            response = JsonResponse({"message": "Error"})
            response.status_code = 500
            return response

class RemoveFiche(View):

    @staticmethod
    def post(request):
        try:
            data = request.POST.dict()
            fiche = Fiche.objects.get(id=int(data["fiche_id"]))
            fiche.delete()
            response = JsonResponse({"message": "Success"})
            response.status_code = 200
            return response
        except Exception as e:
            print(traceback.format_exc())
            response = JsonResponse({"message": "Error"})
            response.status_code = 500
            return response

class AddFonction(View):

    @staticmethod
    def post(request):
        try:
            data = request.POST.dict()
            data.pop("csrfmiddlewaretoken")
            Fonction.objects.create(**data)
            response = JsonResponse({"message": "Success"})
            response.status_code = 200
            return response
        except Exception as e:
            print(traceback.format_exc())
            response = JsonResponse({"message": "Error"})
            response.status_code = 500
            return response


class AddGrade(View):

    @staticmethod
    def post(request):
        try:
            data = request.POST.dict()
            data.pop("csrfmiddlewaretoken")
            Grade.objects.create(**data)
            response = JsonResponse({"message": "Success"})
            response.status_code = 200
            return response
        except Exception as e:
            print(traceback.format_exc())
            response = JsonResponse({"message": "Error"})
            response.status_code = 500
            return response

class AddGroupe(View):

    @staticmethod
    def post(request):
        try:
            data = request.POST.dict()
            data.pop("csrfmiddlewaretoken")
            Groupe.objects.create(**data)
            response = JsonResponse({"message": "Success"})
            response.status_code = 200
            return response
        except Exception as e:
            print(traceback.format_exc())
            response = JsonResponse({"message": "Error"})
            response.status_code = 500
            return response


@csrf_exempt
def add_image(request):
    try:
        data = request.FILES
        image = data["file"]
        path = default_storage.save('photos/' + image._name, ContentFile(image.read()))
        response = JsonResponse({"message": "Success"})
        response.status_code = 200
        return response
    except Exception:
        print(traceback.format_exc())
        response = JsonResponse({"message": "Error"})
        response.status_code = 500
        return response

class ChangeRank(View):

    @staticmethod
    def post(request):
        try:
            data = request.POST
            id = data["id"]
            rank = data["rank"]
            fiche = Fiche.objects.filter(id=int(id)).update(rang_affichage=int(rank))
            response = JsonResponse({"message": "Success"})
            response.status_code = 200
            return response
        except Exception:
            print(traceback.format_exc())
            response = JsonResponse({"message": "Error"})
            response.status_code = 500
            return response

class Login(View):

    @staticmethod
    def post(request):
        try:
            data = request.POST
            user = authenticate(request, username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                response = JsonResponse({"message": "success"})
                response.status_code = 200
                return response
        except Exception as e:
            print(traceback.format_exc())
            response = JsonResponse({"message": "error"})
            response.status_code = 500
            return response
