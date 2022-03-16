def get_cafe_name(cafe):
    return cafe["name"]

def get_cafe_till(cafe):
    return cafe["till"]

def get_cafe_menu(cafe):
    cakes = []
    for cake in cafe["cake_menu"]:
        cakes.append(cake["name"])
    return cakes

def increase_till(cafe, amount):
    cafe["till"] += amount

def list_gluten_free_cakes(cafe):
    gluten_free_cakes = []
    for cake in cafe["cake_menu"]:
        if cake["gluten_free"]:
            gluten_free_cakes.append(cake)
    return gluten_free_cakes

def find_cake_by_name(cake_name):
    pass

def sell_cake(cake_name):
    pass
