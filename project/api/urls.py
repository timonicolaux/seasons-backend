from django.urls import path
from api.views import MonthView, MonthListView

urlpatterns = [
	path('month/<int:id>/', MonthView.as_view(), name="month_view"),
	path('month_list/', MonthListView.as_view(), name="month_list_view"),
]
