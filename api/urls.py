from django.conf.urls import url
from rest_framework import routers
from api.views import createEventViewSet, createLocationViewSet, createTicketViewSet, getEventViewSet, ScheduleViewSet, createTransactionViewSet, getTransactionViewSet, CustomView
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'event/create', createEventViewSet)
router.register(r'location/create', createLocationViewSet)
router.register(r'event/ticket/create', createTicketViewSet)
router.register(r'event/getinfo', getEventViewSet)
router.register(r'transaction/purchase', createTransactionViewSet)
router.register(r'transaction/get_info', getTransactionViewSet)
router.register(r'schedule', ScheduleViewSet)

schema_view = get_swagger_view(title='Loket Event API')

urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'^docs/', schema_view),
]

urlpatterns += router.urls