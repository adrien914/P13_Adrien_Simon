from django.urls import path, include
from django.contrib import admin
from organigramme import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

app_name = "organigramme"

urlpatterns = [
    path("", views.ListePoles.as_view(), name="liste_poles"),
    path("login/", views.Login.as_view(), name="login"),
    path("organigramme/<str:pole>/", views.Organigramme.as_view(), name="organigramme"),
    path('search_engine/', views.SearchEngine.as_view(), name='search_engine'),
    path('page_admin/', views.Admin.as_view(), name='admin'),
    path('modify_fiche/', views.ModifyFiche.as_view(), name='modify_fiche'),
    path('remove_fiche/', views.RemoveFiche.as_view(), name='remove_fiche'),
    path('add_fonction/', views.AddFonction.as_view(), name='add_fonction'),
    path('add_grade/', views.AddGrade.as_view(), name='add_grade'),
    path('add_groupe/', views.AddGroupe.as_view(), name='add_groupe'),
    path('add_image/', views.add_image, name='add_image'),
    path('change_rank/', views.ChangeRank.as_view(), name='change_rank'),
    path('page_admin/<str:_id>/', views.Admin.as_view(), name='admin_param'),
    path('admin/', admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
