from django.contrib import admin
from django.urls import path,include
from login_apis import urls
from .views import create_election,select_election
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",create)
    path("",views.create_unique_id,name="create_candidates"),
    # path("/do_votes",views.do_vote,name="do_votes"),
    path("create",views.create_election,name="create_id"),
    path("select_election",views.select_election,name="select_election"),
    path("extract",views.select_election,name="decode"),

]