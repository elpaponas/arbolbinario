class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierdo)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecho)
        else:
            print("El valor ya existe en el árbol")

    def buscar(self, valor):
        return self._buscar(valor, self.raiz) is not None

    def _buscar(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar(valor, nodo_actual.izquierdo)
        else:
            return self._buscar(valor, nodo_actual.derecho)

    def eliminar(self, valor):
        self.raiz = self._eliminar(valor, self.raiz)

    def _eliminar(self, valor, nodo):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar(valor, nodo.izquierdo)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar(valor, nodo.derecho)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            nodo_min = self._minimo(nodo.derecho)
            nodo.valor = nodo_min.valor
            nodo.derecho = self._eliminar(nodo_min.valor, nodo.derecho)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def mostrar(self, nodo=None, nivel=0, prefijo="R: "):
        if nodo is None:
            nodo = self.raiz

        if nodo.derecho is not None:
            self.mostrar(nodo.derecho, nivel + 1, prefijo="D--> ")

        espacio = "    " * nivel
        print(f"{espacio}{prefijo}{nodo.valor}")

        if nodo.izquierdo is not None:
            self.mostrar(nodo.izquierdo, nivel + 1, prefijo="I--> ")

    def recorrer_inorden(self):
        elementos = []
        self._inorden(self.raiz, elementos)
        return elementos

    def _inorden(self, nodo, elementos):
        if nodo:
            self._inorden(nodo.izquierdo, elementos)
            elementos.append(nodo.valor)
            self._inorden(nodo.derecho, elementos)

    def recorrer_preorden(self):
        elementos = []
        self._preorden(self.raiz, elementos)
        return elementos

    def _preorden(self, nodo, elementos):
        if nodo:
            elementos.append(nodo.valor)
            self._preorden(nodo.izquierdo, elementos)
            self._preorden(nodo.derecho, elementos)

    def recorrer_postorden(self):
        elementos = []
        self._postorden(self.raiz, elementos)
        return elementos

    def _postorden(self, nodo, elementos):
        if nodo:
            self._postorden(nodo.izquierdo, elementos)
            self._postorden(nodo.derecho, elementos)
            elementos.append(nodo.valor)

# Código interactivo para manipular el árbol
def main():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\nOperaciones con Árbol Binario de Búsqueda:")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Mostrar Árbol")
        print("5. Recorrer Inorden")
        print("6. Recorrer Preorden")
        print("7. Recorrer Postorden")
        print("8. Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == "1":
            elemento = int(input("Ingresa el valor a insertar: "))
            arbol.insertar(elemento)
        elif eleccion == "2":
            elemento = int(input("Ingresa el valor a buscar: "))
            if arbol.buscar(elemento):
                print(f"El valor {elemento} se encuentra en el árbol.")
            else:
                print(f"El valor {elemento} no se encuentra en el árbol.")
        elif eleccion == "3":
            elemento = int(input("Ingresa el valor a eliminar: "))
            arbol.eliminar(elemento)
            print(f"El valor {elemento} ha sido eliminado del árbol.")
        elif eleccion == "4":
            arbol.mostrar()
        elif eleccion == "5":
            print("Recorrido Inorden:", arbol.recorrer_inorden())
        elif eleccion == "6":
            print("Recorrido Preorden:", arbol.recorrer_preorden())
        elif eleccion == "7":
            print("Recorrido Postorden:", arbol.recorrer_postorden())
        elif eleccion == "8":
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
