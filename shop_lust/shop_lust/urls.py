"""
URL configuration for shop_lust project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
# from wep_shop import views
#
# # urlpatterns = [
# #     path('', views.index),
# #     path('about', views.about, kwargs={"name": "Tom", "age": 38}),
# # ]
# urlpatterns = [
#     path("index", views.index),
# ]

# from django.urls import path, re_path
# from wep_shop import views

# urlpatterns = [
#     path("index", views.index),
# ]
# urlpatterns = [
#     path("", views.index),
# ]
# urlpatterns = [
#     path("", views.index),
#     path("user/<name>/<int:age>", views.user),
# ]
# urlpatterns = [
#     path("", views.index),
#     path("user", views.user),
#     path("user/<name>", views.user),
#     path("user/<name>/<int:age>", views.user),
# ]
# urlpatterns = [
#     path("", views.index),
#     re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
#     re_path(r"^user/(?P<name>\D+)", views.user),
#     re_path(r"^user", views.user),
# ]

# from django.urls import path, include
# from wep_shop import views

# product_patterns = [
#     path("", views.products),
#     path("new", views.new),
#     path("top", views.top),
# ]
#
# urlpatterns = [
#     path("", views.index),
#     path("products/", include(product_patterns)),
# ]

# product_patterns = [
#     path("", views.products),
#     path("comments", views.comments),
#     path("questions", views.questions),
# ]
#
# urlpatterns = [
#     path("", views.index),
#     path("products/<int:id>/", include(product_patterns)),
# ]

# urlpatterns = [
#     path("", views.index),
#     path("user/", views.user)
# ]

# urlpatterns = [
#     path("", views.index),
#     path("about/", views.about),
#     path("contact/", views.contact),
#     path("details/", views.details),
# ]
# urlpatterns = [
#     path("index/<int:id>", views.index),
#     path("access/<int:age>", views.access),
# ]
# urlpatterns = [
#     path("index", views.index),
# ]
# urlpatterns = [
#     path("set", views.set),
#     path("get", views.get),
# ]

# from django.urls import path
# from wep_shop import views
#
# urlpatterns = [
#     path("", views.index),
#     # path("about/", views.about),
#     # path("contact/", views.contact),
# ]

# from django.urls import path
# from django.views.generic import TemplateView
#
# # urlpatterns = [
# #     path("about/", TemplateView.as_view(template_name="about.html")),
# #     path("contact/", TemplateView.as_view(template_name="contact.html")),
# # ]
#
# urlpatterns = [
#     path("about/", TemplateView.as_view(template_name="about.html",
#         extra_context={"header": "О сайте"})),
#     path("contact/", TemplateView.as_view(template_name="contact.html")),
# ]

# from django.urls import path
# from wep_shop import views
#
# urlpatterns = [
#     path("", views.index),
# ]

from django.urls import path
from wep_shop import views

# urlpatterns = [
#     path("", views.index),
#     # path("contacts/", views.contacts),
# ]

# urlpatterns = [
#     path("", views.index),
#     path("postuser/", views.postuser),
# ]

# urlpatterns = [
#     # path("", views.index),
# ]

# from django.urls import path
# from wep_shop import views
#
# urlpatterns = [
#     path("", views.index),
#     path("create/", views.create),
#     path("edit/<int:id>/", views.edit),
#     path("delete/<int:id>/", views.delete),
# ]

from django.urls import path
from wep_shop import views

# urlpatterns = [
#     path("", views.index),
#     path("create/", views.create),
#     path("edit/<int:id>/", views.edit),
#     path("delete/<int:id>/", views.delete),
# ]

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
]