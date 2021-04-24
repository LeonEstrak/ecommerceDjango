from django.urls import path

from . import views

app_name = "merchant"

urlpatterns = [
    # Create
    path("add/", views.CreateItemView.as_view(), name="add"),
    # Read
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Update
    path("<int:pk>/update/", views.UpdateItemView.as_view(), name="update"),
    # Delete
    path("<int:pk>/delete/", views.DeleteItemView.as_view(), name="delete"),
]
