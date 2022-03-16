def get_cafe_name(cafe):
    return cafe["name"]

def get_cafe_till(cafe):
    return cafe["till"]

def get_cafe_menu(cafe):
    cakes = []
    for cake in cafe["cake_menu"]:
        cakes.append(cake["name"])
    return cakes

def list_gluten_free_cakes(cafe):
    gluten_free_cakes = []
    for cake in cafe["cake_menu"]:
        if cake["gluten_free"]:
            gluten_free_cakes.append(cake)
    return gluten_free_cakes


def increase_till(cafe, amount):
    cafe["till"] += amount

def find_cake_by_name(cafe, cake_name):
    for cake in cafe["cake_menu"]:
        if cake["name"] == cake_name:
            return cake

def sell_cake(cafe, cake_name):
    cake = find_cake_by_name(cafe, cake_name)
    increase_till(cafe, cake["price"])
    cafe["cakes_sold"] += 1
