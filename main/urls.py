from django.contrib.auth.views import LoginView
from .forms import SignupFormCeo, SignupFormHr, SignupFormCto, SignupFormSeniorSE, SignupFormJuniorSE
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.index, name="main"),
    path('signup_ceo/', views.signup_ceo, kwargs={'Form': SignupFormCeo}, name='signup_ceo'),
    path('signup_hr/', views.signup_hr, kwargs={'Form': SignupFormHr}, name='signup_hr'),
    path('signup_cto/', views.signup_cto, kwargs={'Form': SignupFormCto}, name='signup_cto'),
    path('signup_sse/', views.signup_engineer, kwargs={'Form': SignupFormSeniorSE}, name='signup_sse'),
    path('signup_jse/', views.signup_engineer, kwargs={'Form': SignupFormJuniorSE}, name='signup_jse'),
    path("login", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('ceo_dashboard/', views.ceo_dashboard, name="ceo_dashboard"),
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('cto_dashboard/', views.cto_dashboard, name='cto_dashboard'),
    path('sse_dashboard/', views.sse_dashboard, name='sse_dashboard'),
    path('jse_dashboard/', views.jse_dashboard, name='jse_dashboard'),
    path('upload_post/', views.upload_post_view, name='upload_post'),
    path('ceo_admin/' , views.admin , name='ceo_admin'),
    path('create_hr/',views.create_hr , name='create_hr'),
    path('create_cto/',views.create_cto , name='create_cto'),
    path('create_sse/',views.create_engineers , kwargs={'Form': SignupFormSeniorSE}, name='create_sse'),
    path('create_jse/',views.create_engineers , kwargs={'Form': SignupFormJuniorSE}, name='create_jse'),


]
