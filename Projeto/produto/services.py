import requests
from .models import Categoria, Produto

def importar_produtos():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    if response.status_code != 200:
        return 0

    produtos = response.json()
    count = 0

    for item in produtos:
        categoria_nome = item.get("category", "Sem Categoria")
        categoria, _ = Categoria.objects.get_or_create(nome=categoria_nome)

        Produto.objects.update_or_create(
            titulo=item["title"],
            defaults={
                "preco": item["price"],
                "descricao": item["description"],
                "categoria": categoria
            }
        )
        count += 1
    return count
