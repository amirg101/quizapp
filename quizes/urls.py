from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    save_quiz_view,home_view,logout_request,
    add_questions,loginPage,registerView
)
from django.conf import settings
from django.conf.urls.static import static
app_name='quizes'
urlpatterns = [
    path('',QuizListView.as_view(),name="main-view"),

    path('login/',loginPage,name="login"),
    path('logout/',logout_request,name="logout"),

    path('register/',registerView,name="register"),
    path('create-quiz/',home_view,name="new_quiz"),
    path('add-questions/',add_questions,name="add-q"),

    path('<int:pk>/',quiz_view,name="quiz_view"),

    path('<int:pk>/save/',save_quiz_view,name="save_view"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)