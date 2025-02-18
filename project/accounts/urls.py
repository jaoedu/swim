from django.urls import path
from accounts import views


urlpatterns = [
    path("create/", views.UserCreateView.as_view(), name="user_create"),
    path(
        "user/update/<int:pk>/",
        views.CustomUserUpdateView.as_view(),
        name="user_update",
    ),
    path(
        "user/deactivate/<int:pk>/",
        views.CustomUserDeleteView.as_view(),
        name="user_deactivate",
    ),
    path("selecao/", views.selectionView.as_view(), name="selecao_success"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("atleta/create/", views.AtletaCreateView.as_view(), name="atleta_create"),
    path(
        "atleta/update/<int:pk>/",
        views.AtletaUpdateView.as_view(),
        name="atleta_update",
    ),
    path(
        "atleta/deactivate/<int:pk>/",
        views.AtletaDeleteView.as_view(),
        name="atleta_deactivate",
    ),
    path(
        "treinador/create/",
        views.TreinadorCreateView.as_view(),
        name="treinador_create",
    ),
    path(
        "treinador/update/<int:pk>/",
        views.TreinadorUpdateView.as_view(),
        name="treinador_update",
    ),
    path(
        "treinador/deactivate/<int:pk>/",
        views.TreinadorDeleteView.as_view(),
        name="treinador_deactivate",
    ),
    path(
        "patrocinador/create/",
        views.PatrocinadorCreateView.as_view(),
        name="patrocinador_create",
    ),
    path("user/success/", views.UserCreateView.as_view(), name="user_success"),
    path("atleta/success/", views.AtletaCreateView.as_view(), name="atleta_success"),
    path(
        "treinador/success/",
        views.TreinadorCreateView.as_view(),
        name="treinador_success",
    ),
    path(
        "patrocinador/success/",
        views.PatrocinadorCreateView.as_view(),
        name="patrocinador_success",
    ),
    path(
        "patrocinador/update/<int:pk>/",
        views.PatrocinadorUpdateView.as_view(),
        name="patrocinador_update",
    ),
    path(
        "patrocinador/deactivate/<int:pk>/",
        views.PatrocinadorDeleteView.as_view(),
        name="patrocinador_deactivate",
    ),
]
