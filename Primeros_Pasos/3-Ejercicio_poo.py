class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self._vida = vida
        self.ataque = ataque

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre}")
        objetivo.recibir_danio(self.ataque)

    def recibir_danio(self, cantidad):
        self._vida -= cantidad

        if self._vida < 0:
            self._vida = 0

        print(f"{self.nombre} recibió {cantidad} de daño.")
        print(f"Vida restante: {self._vida}")

    def esta_vivo(self):
        return self._vida > 0

    def mostrar_info(self):
        print(f"\n--- {self.nombre} ---")
        print(f"Vida: {self._vida}")
        print(f"Ataque: {self.ataque}")


class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, armadura):
        super().__init__(nombre, vida, ataque)
        self.armadura = armadura

    def recibir_danio(self, cantidad):
        # La armadura reduce el daño recibido
        danio_real = cantidad - self.armadura

        if danio_real < 0:
            danio_real = 0

        print(f"{self.nombre} bloqueó {self.armadura} de daño.")

        super().recibir_danio(danio_real)


class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, mana):
        super().__init__(nombre, vida, ataque)
        self.mana = mana

    def atacar(self, objetivo):
        if self.mana >= 10:
            danio = self.ataque * 2
            self.mana -= 10

            print(f"{self.nombre} lanzó una bola de fuego.")
            objetivo.recibir_danio(danio)
        else:
            print(f"{self.nombre} no tiene suficiente mana.")


# ==========================================
# CREACIÓN DE OBJETOS
# ==========================================

guerrero = Guerrero(
    nombre="Arthas",
    vida=150,
    ataque=20,
    armadura=5
)

mago = Mago(
    nombre="Merlín",
    vida=100,
    ataque=25,
    mana=50
)


# ==========================================
# MOSTRAR INFORMACIÓN
# ==========================================

guerrero.mostrar_info()
mago.mostrar_info()


# ==========================================
# COMBATE
# ==========================================

print("\n===== COMIENZA EL COMBATE =====")

guerrero.atacar(mago)

print()

mago.atacar(guerrero)

print()

guerrero.atacar(mago)


# ==========================================
# ESTADO FINAL
# ==========================================

print("\n===== ESTADO FINAL =====")

guerrero.mostrar_info()
mago.mostrar_info()

print("\n¿Guerrero vivo?", guerrero.esta_vivo())
print("¿Mago vivo?", mago.esta_vivo())