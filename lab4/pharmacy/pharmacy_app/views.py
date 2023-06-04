from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from .models import *
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from pharmacy_app.forms import RegisterUserForm, LoginUserForm, MedicinesForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from cart.forms import CartAddMedicinesForm
import requests


# Create your views here.

def index(request):
    medicines = Medicines.objects.all()[:3]
    return render(request, 'index.html',
                  context={'medicines': medicines})


def MedicinesList(request, type=None):
    medicines = Medicines.objects.all()
    medicines_type = None
    medicines_types = MedicinesType.objects.all()
    sort_type_price = request.GET.get('sort_price')

    if str(sort_type_price) == 'ascending':
        medicines = medicines.order_by('price')

    elif str(sort_type_price) == 'descending':
        medicines = medicines.order_by('-price')

    if type:
        medicines_type = get_object_or_404(MedicinesType, designation=type)
        medicines = medicines.filter(medicines_type=medicines_type)
        print(medicines_type)

    return render(request, 'medicines.html', {'medicines': medicines, 'medicines_type': medicines_type,'medicines_types':medicines_types})


class MedicinesDetailView(DetailView):
    model = Medicines
    cart_medicines_form = CartAddMedicinesForm()

    template_name = 'medicines_details.html'


def medicines_detail(request, id):
    medicines = get_object_or_404(Medicines, id=id)
    cart_medicines_form = CartAddMedicinesForm()

    return render(request,
                  'medicines_details.html',
                  {'medicines': medicines, 'cart_medicines_form': cart_medicines_form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('pharmacy_app:login')

    def form_valid(self, form):
        user = form.save()

        Client.objects.create(first_name=form.cleaned_data['first_name'],
                              last_name=form.cleaned_data['last_name'],
                              date_of_birth=form.cleaned_data['date_birthday'],
                              email=form.cleaned_data['email'],
                              phone_number=form.cleaned_data['phone_number']).save()

        login(self.request, user)
        return redirect('pharmacy_app:index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    success_url = reverse_lazy('pharmacy_app:login')

    def get_success_url(self):
        return reverse_lazy('pharmacy_app:index')


def logout_user(request):
    logout(request)
    return redirect('pharmacy_app:index')


def medicines_create(request):
    form = MedicinesForm()

    if request.method == "POST":
        medicines = Medicines.objects.create(code=request.POST.get('code'),
                                 name=request.POST.get('name'),
                                 description=request.POST.get('description'),
                                 price=request.POST.get('price'),
                                 instruction=request.POST.get('instruction'),
                                 medicines_type=MedicinesType.objects.get(id=request.POST.get('medicines_type')),
                                 supplier=Supplier.objects.get(id=request.POST.get('supplier')),
                                 photo=request.FILES.get('photo')),


    else:
        return render(request, "create_medicines.html", {"form": form})
    return HttpResponseRedirect("/")


def medicines_edit(request, id):
    try:
        medicines = Medicines.objects.get(id=id)

        form = MedicinesForm(initial={'code': medicines.code, 'name': medicines.name,
                                'description': medicines.description, 'price': medicines.price,
                                'instruction': medicines.instruction, 'medicines_type': medicines.medicines_type,
                                'supplier': medicines.supplier,'photo': medicines.photo})

        if request.method == "POST":
            medicines.code = request.POST.get('code')
            medicines.name = request.POST.get('name')
            medicines.description = request.POST.get('description')
            medicines.price = request.POST.get('price')
            medicines.instruction = request.POST.get('instruction')
            medicines.medicines_type = MedicinesType.objects.get(id=request.POST.get('medicines_type'))
            medicines.supplier = Supplier.objects.get(id=request.POST.get('supplier'))
            medicines.photo = request.FILES.get('photo')
            medicines.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_medicines.html", {"medicines": medicines, 'form': form})

    except medicines.DoesNotExist:
        return HttpResponseNotFound("<h2>Medicines not found :(</h2>")


def medicines_delete(request, id):
    try:
        medicines = Medicines.objects.get(id=id)
        medicines.delete()
        return HttpResponseRedirect("/")
    except medicines.DoesNotExist:
        return HttpResponseNotFound("<h2>medicines not found</h2>")
