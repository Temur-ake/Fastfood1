import pytz
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView

from .forms import BookingForm, SearchForm
from .models import MenuItem, Category, About, Booking


class BookView(TemplateView):
    template_name = 'book.html'


def menu_l_view(request):
    menu_items = MenuItem.objects.all()
    categories = Category.objects.all()

    context = {
        'menu_items': menu_items,
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def menu_view(request):
    menu_items = MenuItem.objects.all()
    categories = Category.objects.all()
    about = About.objects.first()
    context = {
        'menu_items': menu_items,
        'categories': categories,
        'about': about
    }
    return render(request, 'index.html', context)


def about_view(request):
    about_info = About.objects.first()
    return render(request, 'about.html', {'about': about_info})


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        form.save()
        return redirect('success')

    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})


def search_view(request):
    form = SearchForm(request.GET or None)
    query = request.GET.get('query', '')

    menu_items = MenuItem.objects.all()

    if query:
        menu_items = menu_items.filter(
            name__icontains=query
        ) | menu_items.filter(
            description__icontains=query
        )
    template_name = 'menu.html'
    return render(request, template_name, {
        'form': form,
        'menu_items': menu_items,
        'query': query
    })


class OfferListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'data.html'
    context_object_name = 'data'
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('data')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
