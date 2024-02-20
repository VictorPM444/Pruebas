"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# se importa la vista de la API desde el Home que hicimos antes
from api.views import (
    login,
    recuperacion_contra,
    home,
    my_account,
    account_details,
    addresses,
    cart,
    order_list,
    wishlist,
    shop,
    checkout_complate,
    checkout_1,
    checkout_2,
    checkout_4,
    checkout_5,
    graficas_formulario,
    graficas_powerbi,
    formularioProducto,
    formularioDatos,
    formularioTalla,
    formularioMarca,
    formularioColor,
    checkout,
)


urlpatterns = [
    # lo comentamos para que no se inicie con la ventana de django
    # path('admin/', admin.site.urls),
    # se crea, el path de vista con el home creado nombrandolo login
    path("login/", login.as_view(), name="login"),
    path("", home.as_view(), name="home"),
    path("my_account/", my_account.as_view(), name="my_account"),
    path("formularioColor/", formularioColor.as_view(), name="formularioColor"),
    path("formularioMarca/", formularioMarca.as_view(), name="formularioMarca"),
    path("formularioTalla/", formularioTalla.as_view(), name="formularioTalla"),
    path("account_details/", account_details.as_view(), name="account_details"),
    path("addresses/", addresses.as_view(), name="addresses"),
    path("cart/", cart.as_view(), name="cart"),
    path("order_list/", order_list.as_view(), name="order_list"),
    path("wishlist/", wishlist.as_view(), name="wishlist"),
    path("shop/", shop.as_view(), name="shop"),
    path("checkout_complate/", checkout_complate.as_view(), name="checkout_complate"),
    path("checkout_1/", checkout_1.as_view(), name="checkout_1"),
    path("checkout_2/", checkout_2.as_view(), name="checkout_2"),
    path("checkout_4/", checkout_4.as_view(), name="checkout_4"),
    path("checkout_5/", checkout_5.as_view(), name="checkout_5"),
    path("recuperacion_contra/", recuperacion_contra.as_view(), name="recuperacion_contra"),
    path("graficas_formulario/", graficas_formulario.as_view(), name="graficas_formulario"),
    path("graficas_powerbi/", graficas_powerbi.as_view(), name="graficas_powerbi"),
    path("formularioProducto/", formularioProducto.as_view(), name="formularioProducto"),
    path("formularioDatos/", formularioDatos.as_view(), name="formularioDatos"),



    path('checkout/', checkout, name='checkout'),




    # path('admin/',admin.site.urls)
    # Otras URL de la aplicación
]
# Agrega esto para servir archivos de medios durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
