from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from apps.views import BookView, menu_view, about_view, book_table, menu_l_view, search_view, OfferListView, \
    custom_login_view

urlpatterns = [
    path('admin/', admin.site.urls),  # Ensure you have the admin URL
    path('book/', BookView.as_view(), name='book'),  # This will use the `BookView` class-based view
    path('menu/', menu_l_view, name='menu'),  # The menu view, lists the menu items

    path('', menu_view, name='index'),  # Homepage view
    path('menu/<slug:category_slug>/', menu_view, name='index_by_c'),  # Menu by category slug
    path('about/', about_view, name='about'),  # About page view
    path('book_table/', book_table, name='book'),  # Booking form view, using a function-based view
    path('book/success/', TemplateView.as_view(template_name='success.html'), name='success'),  # Booking success page
    path('search/', search_view, name='search'),
    path('login/', custom_login_view, name='login'),  # Search view
    path('data/', OfferListView.as_view(), name='data')
]
