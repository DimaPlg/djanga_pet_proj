# from django.http import HttpResponse
#
#
# # def index(request):
# #     host = request.META["HTTP_HOST"]  # получаем адрес сервера
# #     user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные бразера
# #     path = request.path  # получаем запрошенный путь
# #
# #     return HttpResponse(f"""
# #         <p>Host: {host}</p>
# #         <p>Path: {path}</p>
# #         <p>User-agent: {user_agent}</p>
# #     """)

# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello")

# from django.http import HttpResponse

# def index(request):
#     # return HttpResponse("Hello METANIT.COM", headers={"SecretCode": "21234567"})
#     # return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")
#     return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
#
# def user(request, name, age):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст:{age}</h2>")

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
#
# def user(request, name="Undefined", age=0):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
#
# def user(request, name="Undefined", age =0):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

# def index(request):
#     return HttpResponse("Главная страница")
#
#
# def products(request):
#     return HttpResponse("Список товаров")
#
#
# def new(request):
#     return HttpResponse("Новые товары")
#
#
# def top(request):
#     return HttpResponse("Наиболее популярные товары")

# def index(request):
#     return HttpResponse("Главная страница")
#
#
# def products(request, id):
#     return HttpResponse(f"Товар {id}")
#
#
# def comments(request, id):
#     return HttpResponse(f"Комментарии о товаре {id}")
#
#
# def questions(request, id):
#     return HttpResponse(f"Вопросы о товаре {id}")

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
#
# def user(request):
#     age = request.GET.get("age", 0)
#     name = request.GET.get("name", "Undefined")
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

# from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
#
#
# def index(request):
#     return HttpResponse("Index")
#
#
# def about(request):
#     return HttpResponse("About")
#
#
# def contact(request):
#     return HttpResponseRedirect("/about")
#
#
# def details(request):
#     return HttpResponsePermanentRedirect("/")
# from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
#
# def index(request, id):
#     people = ["Tom", "Bob", "Sam"]
#     # если пользователь найден, возвращаем его
#     if id in range(0, len(people)):
#         return HttpResponse(people[id])
#     # если нет, то возвращаем ошибку 404
#     else:
#         return HttpResponseNotFound("Not Found")
#
#
# def access(request, age):
#     # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
#     if age not in range(1, 111):
#         return HttpResponseBadRequest("Некорректные данные")
#     # если возраст больше 17, то доступ разрешен
#     if (age > 17):
#         return HttpResponse("Доступ разрешен")
#     # если нет, то возвращаем ошибку 403
#     else:
#         return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")

# from django.http import JsonResponse
#
#
# def index(request):
#     return JsonResponse({"name": "Tom", "age": 38})

# from django.http import JsonResponse
# from django.core.serializers.json import DjangoJSONEncoder
#
#
# def index(request):
#     bob = Person("Bob", 41)
#     return JsonResponse(bob, safe=False, encoder=PersonEncoder)
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name  # имя человека
#         self.age = age  # возраст человека
#
#
# class PersonEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "age": obj.age}
#             # return obj.__dict__
#         return super().default(obj)

# from django.http import HttpResponse

#
# # установка куки
# def set(request):
#     # получаем из строки запроса имя пользователя
#     username = request.GET.get("username", "Undefined")
#     # создаем объект ответа
#     response = HttpResponse(f"Hello {username}")
#     # передаем его в куки
#     response.set_cookie("username", username)
#     return response


# установка куки
# def set(request):
#     # получаем из строки запроса имя пользователя
#     username = request.GET.get("username", "Undefined")
#     response = HttpResponse(f"Hello {username}")
#     # передаем его в куки
#     response.set_cookie("username", username)
#     return response
#
#
# # получение куки
# def get(request):
#     # получаем куки с ключом username
#     username = request.COOKIES["username"]
#     return HttpResponse(f"Hello {username}")

# from django.shortcuts import render
# from django.template.response import TemplateResponse

# def index(request):
#     return render(request, "index.html")

# def index(request):
#     return TemplateResponse(request, "index.html")
#
#
# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return render(request, "contact.html")

# def index(request):
#     data = {"header": "Hello Django", "message": "Welcome to Python"}
#     return render(request, "index.html", context=data)

# def index(request):
#     header = "Данные пользователя"  # обычная переменная
#     langs = ["Python", "Java", "C#"]  # список
#     user = {"name": "Tom", "age": 23}  # словарь
#     address = ("Абрикосовая", 23, 45)  # кортеж
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return render(request, "index.html", context=data)
#
# def index(request):
#     header = "Данные пользователя"  # обычная переменная
#     langs = ["Python", "Java", "C#"]  # список
#     user = {"name": "Tom", "age": 23}  # словарь
#     address = ("Абрикосовая", 23, 45)  # кортеж
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return TemplateResponse(request, "index.html", data)

# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, "index.html", context={"person": Person("Tom")})
#
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name  # имя человека

# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, "index.html", context={"body": "<h1>Hello World!</h1>"})

# from django.shortcuts import render
#
#
# def index(request):
#     langs = ["Python", "JavaScript", "Java", "C#", "C++"]
#     return render(request, "index.html", context={"langs": langs})

# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, "index.html")

# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, "index.html")
#
# #
# # def contacts(request):
# #     return render(request, "contacts.html")

# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, "index.html", context={"site": "METANIT.COM"})

# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# def index(request):
#     return render(request, "index.html")
#
#
# # def postuser(request):
# #     # получаем из данных запроса POST отправленные через форму данные
# #     name = request.POST.get("name", "Undefined")
# #     age = request.POST.get("age", 1)
# #     return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")
#
# def postuser(request):
#     # получаем из строки запроса имя пользователя
#     name = request.POST.get("name", "Undefined")
#     age = request.POST.get("age", 1)
#     langs = request.POST.getlist("languages", ["python"])
#
#     return HttpResponse(f"""
#                 <div>Name: {name}  Age: {age}<div>
#                 <div>Languages: {langs}</div>
#             """)
#
# from django.shortcuts import render
# from .forms import UserForm
#
#
# def index(request):
#     userform = UserForm()
#     return render(request, "index.html", {"form": userform})

# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import UserForm


# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
#     else:
#         userform = UserForm()
#         return render(request, "index.html", {"form": userform})

# from .models import Person
#
# # получаем все объекты
# people = Person.objects.all()
# print(people.query)
#
# # получаем объекты с именем Tom
# people = people.filter(name="Tom")
# print(people.query)
#
# # получаем объекты с возрастом, равным 31
# people = people.filter(age=31)
# print(people.query)
#
# # здесь происходит выполнения запроса в БД
# for person in people:
#     print(f"{person.id}.{person.name} - {person.age}")

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponseNotFound
# from .models import Person
#
#
# # получение данных из бд
# def index(request):
#     people = Person.objects.all()
#     return render(request, "index.html", {"people": people})
#
#
# # сохранение данных в бд
# def create(request):
#     if request.method == "POST":
#         person = Person()
#         person.name = request.POST.get("name")
#         person.age = request.POST.get("age")
#         person.save()
#     return HttpResponseRedirect("/")
#
#
# # изменение данных в бд
# def edit(request, id):
#     try:
#         person = Person.objects.get(id=id)
#
#         if request.method == "POST":
#             person.name = request.POST.get("name")
#             person.age = request.POST.get("age")
#             person.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"person": person})
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")
#
#
# # удаление данных из бд
# def delete(request, id):
#     try:
#         person = Person.objects.get(id=id)
#         person.delete()
#         return HttpResponseRedirect("/")
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("<h2>Person not found</h2>")

# from django.shortcuts import render
# from .models import Company, Product
# from django.http import HttpResponseRedirect, HttpResponseNotFound
#
#
# # получение данных из бд
# def index(request):
#     products = Product.objects.all()
#     return render(request, "index.html", {"products": products})
#
#
# # добавление данных из бд
# def create(request):
#     create_companies()  # добавляем начальные данные для компаний
#
#     # если запрос POST, сохраняем данные
#     if request.method == "POST":
#         product = Product()
#         product.name = request.POST.get("name")
#         product.price = request.POST.get("price")
#         product.company_id = request.POST.get("company")
#         product.save()
#         return HttpResponseRedirect("/")
#     # передаем данные в шаблон
#     companies = Company.objects.all()
#     return render(request, "create.html", {"companies": companies})
#
#
# # изменение данных в бд
# def edit(request, id):
#     try:
#         product = Product.objects.get(id=id)
#
#         if request.method == "POST":
#             product.name = request.POST.get("name")
#             product.price = request.POST.get("price")
#             product.company_id = request.POST.get("company")
#             product.save()
#             return HttpResponseRedirect("/")
#         else:
#             companies = Company.objects.all()
#             return render(request, "edit.html", {"product": product, "companies": companies})
#     except Product.DoesNotExist:
#         return HttpResponseNotFound("<h2>Product not found</h2>")
#
#
# # удаление данных из бд
# def delete(request, id):
#     try:
#         product = Product.objects.get(id=id)
#         product.delete()
#         return HttpResponseRedirect("/")
#     except Product.DoesNotExist:
#         return HttpResponseNotFound("<h2>Product not found</h2>")
#
#
# # добавление начальных данных в таблицу компаний
# def create_companies():
#     if Company.objects.all().count() == 0:
#         Company.objects.create(name="Apple")
#         Company.objects.create(name="Asus")
#         Company.objects.create(name="MSI")

from datetime import date
from django.shortcuts import render
from .models import Student, Course
from django.http import HttpResponseRedirect


# получение данных из бд
def index(request):
    # фильтрация
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


# добавление данных в бд
def create(request):
    initialize()
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        student = Student()
        student.name = request.POST.get("name")
        course_ids = request.POST.getlist("courses")
        student.save()
        # получаем все выбранные курсы по их id
        courses = Course.objects.filter(id__in=course_ids)
        student.courses.set(courses, through_defaults={"date": date.today(), "mark": 0})
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    courses = Course.objects.all()
    return render(request, "create.html", {"courses": courses})


def initialize():
    # Student.objects.all().delete()
    # Course.objects.all().delete()
    if Course.objects.all().count() == 0:
        Course.objects.create(name="Python")
        Course.objects.create(name="Django")
        Course.objects.create(name="FastAPI")