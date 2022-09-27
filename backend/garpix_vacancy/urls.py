from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('vacancy', views.VacancyListView)
router.register('vacancy_application', views.VacancyApplicationView)

urlpatterns = router.urls
