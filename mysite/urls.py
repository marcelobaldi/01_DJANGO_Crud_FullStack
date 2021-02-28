from django.contrib import admin
from django.urls import path
from custumers import views as custumersViews

urlpatterns = [
    path('', custumersViews.save, name='Save'),
    path('custumers/read/', custumersViews.read, name='Read'),
    path('custumers/read/<int:idRoute>', custumersViews.sendUpdate, name='SendUpdate'),
    path('custumers/delete/<int:idRoute>', custumersViews.sendDelete, name='SendDelete'),
    path('custumers/delete/', custumersViews.delete, name='Delete'),
    path('admin/', admin.site.urls),
]


