from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Producto, Categoria

# Create your views here.
from django.db.models import Q

def index(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda de los parámetros GET
    lista_categorias = Categoria.objects.all()
    
    if query:
        # Filtrar los productos que coincidan con el término de búsqueda en nombre o descripción
        lista_productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query)).order_by('nombre')
    else:
        lista_productos = Producto.objects.order_by('nombre')[:6]
    
    context = {
        'productos': lista_productos,
        'categorias': lista_categorias,
    }
    return render(request, 'index.html', context)


def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html',{'producto': producto})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    lista_productos = categoria.producto_set.all()
    lista_categorias = Categoria.objects.all()
    
    context = {
        'productos':lista_productos,
        'categorias':lista_categorias,
        'categoria':categoria
    }
    
    return render(request,'index.html',context)
def calcular_total(request):
    # Lógica para calcular la sumatoria de precios de los elementos seleccionados
    total = 0
    # Obten los elementos seleccionados y calcula la sumatoria de precios
    # ...

    # Redirige a una página donde se mostrará el resultado
    return HttpResponseRedirect('/total/?total={}'.format(total))