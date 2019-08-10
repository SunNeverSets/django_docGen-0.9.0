from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    # path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("upload/", views.upload, name="upload"),
    path("create/<slug>/", views.doc_gen, name="detail" ),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)