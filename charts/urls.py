from charts import views
import django.conf.urls

urlpatterns = (
    django.conf.urls.url(r'^$', views.chartsView.as_view(), name='chartsView'),
)