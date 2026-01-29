from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.DataView.as_view(), name='data-root'),
    path('model/', views.ModelView.as_view(), name='model-root'),
    path('attack/', views.AttackView.as_view(), name='attack-root'),
    path('eval/', views.EvalView.as_view(), name='eval-root'),
]
