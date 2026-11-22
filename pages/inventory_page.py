
class InventoryPage:

    def __init__(self, page):
        self.page = page

        # Elementos del catálogo
        self.titulo = page.locator(".title")
        self.productos = page.locator(".inventory_item")
        
        self.nombres = page.locator(
        ".inventory_item_name"
        )

        self.precios = page.locator(
        ".inventory_item_price"
        )
 
        # Carrito
        self.contador_carrito = page.locator(
            "[data-test='shopping-cart-badge']"
        )

        self.boton_agregar_mochila = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )

        self.boton_eliminar_mochila = page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        )

    # Verificar título del catálogo
    def obtener_titulo(self):
        return self.titulo.inner_text()

    # Contar productos
    def contar_productos(self):
        return self.productos.count()

    # Obtener nombres
    def obtener_nombres(self):
        return self.nombres.all_text_contents()

    # Obtener precios
    def obtener_precios(self):
        return self.precios.all_inner_texts()

    
    
    def agregar_mochila(self):

        self.boton_agregar_mochila.click()

        self.boton_eliminar_mochila.wait_for(
        state="visible"
    )

        self.contador_carrito.wait_for(
        state="visible"
    )

        assert self.obtener_contador_carrito() == "1"
    

    # Eliminar mochila
    def eliminar_mochila(self):
        self.boton_eliminar_mochila.click()

    # Obtener cantidad del carrito
    def obtener_contador_carrito(self):
        return self.contador_carrito.inner_text()
