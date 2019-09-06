from django.conf.urls import url
from .views import (
    index, 
    user, 
    login, 
    logout,
    register,
    createGoods,
    updateGoods,
    deleteGoods,
)

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^user/', user, name="user"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^logout/', logout, name="logout"),
    url(r'^createGoods/', createGoods, name="crtGoods"),
    url(r'^updateGoods/(?P<dynamicID>[0-9]{1,2})', updateGoods, name="uptGoods"),
    url(r'^deleteGoods/(?P<dynamicID>[0-9]{1,3})', deleteGoods, name="dltGoods")
]