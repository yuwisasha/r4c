from django.urls import path

from robots.views import create_robot, get_report

urlpatterns = [
    path("create", create_robot, name="create_robot"),
    path("report", get_report, name="get_report"),
]
