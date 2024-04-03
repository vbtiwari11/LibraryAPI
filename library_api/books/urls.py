from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'books/user_data',views.AllCrashes.as_view({'get':'get_user_data'})),
    re_path(r'books/borrow_book',views.AllCrashes.as_view({'get':'get_borrow_data'})),
    re_path(r'books/return_book',views.AllCrashes.as_view({'get':'get_return_data'})),
    re_path(r'books/renew_book',views.AllCrashes.as_view({'get':'get_renew_data'})),
    re_path(r'books/borrow_history_book',views.AllCrashes.as_view({'get':'get_borrow_history_data'})),
    re_path(r'books/library_data',views.AllCrashes.as_view({'get':'get_library_data'})),
    re_path(r'books/available_book',views.AllCrashes.as_view({'get':'get_book_available_data'}))
    #path('userdata/', UserData.as_view(), name='user-data'),
]



