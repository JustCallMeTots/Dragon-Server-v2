from django.contrib import admin
from django.urls import path
from dragonapi.views import register_user, check_user
from django.conf.urls import include
from rest_framework import routers
from dragonapi.views import RaceView
from dragonapi.views import CharacterView
from dragonapi.views import ClassesView
from dragonapi.views import EquipmentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'race', RaceView, 'race')
router.register(r'character', CharacterView, 'character')
router.register(r'classes', ClassesView, 'classes')
router.register(r'equipment', EquipmentView, 'equipment')


urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]