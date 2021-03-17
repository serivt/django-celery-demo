from django.urls import path

from demo.views import CountPrimeNumbersView

app_name = "demo"

urlpatterns = [
    path(
        "count-prime-numbers/",
        CountPrimeNumbersView.as_view({"get": "list", "post": "create"}),
    ),
]
