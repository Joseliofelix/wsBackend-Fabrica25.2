from rest_framework import viewsets
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer
from .services import importar_produtos

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# Endpoint extra para importar da API externa
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def importar(request):
    count = importar_produtos()
    return Response({"mensagem": f"{count} produtos importados da Fake Store API"})
