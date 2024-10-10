from sys import path_hooks

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views import BookViewSet, BookCategoryViewSet

router = DefaultRouter()
router.register('category', BookCategoryViewSet)
router.register('book', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
