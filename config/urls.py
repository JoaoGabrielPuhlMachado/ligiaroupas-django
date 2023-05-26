from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ligiaroupas.views import CategoriaViewset, CorViewset, ItemViewset, MarcaViewset, TamanhoViewset

router = DefaultRouter()
router.register(r"categorias", CategoriaViewset)
router.register(r"cores", CorViewset)
router.register(r"itens", ItemViewset)
router.register(r"marcas", MarcaViewset)
router.register(r"tamanhos", TamanhoViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]