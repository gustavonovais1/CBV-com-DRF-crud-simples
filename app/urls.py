from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls

"""
from app.views import todo_list, todo_default_change_and_delete, TodoListAndCreate, TodoChangeAndDelete
from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoChangeAndDelete.as_view())
]
"""