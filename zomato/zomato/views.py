from django.shortcuts import render

from zomato.entity import Restaurant

restaurant1 = Restaurant(1, "Restaurante do Gordo", 'Comida boa é aquela comida feita com amor',
                         'rua ali do lado da esquina',
                         'https://guianobairro.com.br/wp-content/uploads/WhatsApp-Image-2019-03-04-at-10.43.46.jpeg',
                         '0:00 - 23:59')
restaurant2 = Restaurant(2, "Restaurante dos Marombas",
                         "Nosso restaurante tem tudo fresco e orgânico para você ter o melhor no seu prato. ",
                         'rua do lado da academia',
                         'https://encrypted-tbn0.gstatic.com/images?q=tbn'
                         ':ANd9GcTUBTffYh5wNfZd1rR7cQDs2GwK6IibwZOXrgIoBurVFx4vEcjwXMweNp84JPpx5exKgY0&usqp=CAU',
                         "09:00 - 18:00")
restaurant3 = Restaurant(3, "Restaurante", 'O caminho da felicidade tem o endereço do nosso restaurante ',
                         'bota qualquer coisa cara',
                         'https://www.casamagalhaes.com.br/blog/wp-content/uploads/2019/01/7-passos-eficazes-para'
                         '-fidelizar-os-clientes-do-seu-restaurante.jpg',
                         '10:00 - 21:00')

restaurants = [restaurant1, restaurant2, restaurant3]


def index(request):
    return render(request, "index.html", {"restaurants": restaurants})


def seeRestaurant(request, id: int):
    for restaurant in restaurants:
        if restaurant.getId() == id:
            return render(request, "restaurant.html", {"restaurant": restaurant})
