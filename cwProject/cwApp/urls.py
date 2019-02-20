from django.urls import path

from.import views


# path for dog
urlpatterns =[
    path("Dog", views.Dog, name='index'),
]

# path for account
urlpatterns =[
    path("Account", views.Account, name='index'),
]