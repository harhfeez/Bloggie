from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('post/<str:slug>/comment/', views.add_comment, name='add_comment'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)