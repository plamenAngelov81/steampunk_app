from django.urls import path, include

from nelly_app.users.views import home_page, AccountRegisterView, AccountLogin, AccountLogOut, AccountDetailsView, \
    AccountEditView, AccountDeleteView

urlpatterns = [
    path('', home_page, name='home page'),
    path('profile/', include([
        path('register/', AccountRegisterView.as_view(), name='account register'),
        path('login/', AccountLogin.as_view(), name='account login'),
        path('logout/', AccountLogOut.as_view(), name='account logout'),
        path('<int:pk>/', AccountDetailsView.as_view(), name='account details'),
        path('edit/<int:pk>/', AccountEditView.as_view(), name='account edit'),
        path('delete/<int:pk>/', AccountDeleteView.as_view(), name='account delete'),
    ])),
]