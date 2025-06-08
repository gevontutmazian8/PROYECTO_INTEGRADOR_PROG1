import time
import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor          # Valor almacenado en el nodo
        self.izquierda = None       # Referencia al subárbol izquierdo
        self.derecha = None         # Referencia al subárbol derecho

class ABB:
    def __init__(self):
        self.raiz = None            # Inicialmente, el árbol está vacío

    def insertar(self, nodo, valor):
        """
        Inserta un valor en el árbol recursivamente.
        Si el nodo es None, crea uno nuevo.
        Si el valor es menor que el nodo actual, va al subárbol izquierdo.
        Si es mayor o igual, va al subárbol derecho.
        """
        if nodo is None:
            return Nodo(valor)      # Nuevo nodo hoja
        if valor < nodo.valor:
            nodo.izquierda = self.insertar(nodo.izquierda, valor)
        else:
            nodo.derecha = self.insertar(nodo.derecha, valor)
        return nodo

    def insertar_valor(self, valor):
        """
        Método público para insertar un valor,
        comienza desde la raíz.
        """
        self.raiz = self.insertar(self.raiz, valor)

    def buscar(self, nodo, valor):
        """
        Busca un valor en el árbol recursivamente.
        Retorna el nodo si se encuentra, o None si no.
        """
        if nodo is None:
            return None
        if valor == nodo.valor:
            return nodo
        elif valor < nodo.valor:
            return self.buscar(nodo.izquierda, valor)
        else:
            return self.buscar(nodo.derecha, valor)

    def recorrido_enorden(self, nodo, resultado=None):
        """
        Recorrido en orden que devuelve una lista ordenada de valores.
        Visita: subárbol izquierdo, nodo actual, subárbol derecho.
        """
        if resultado is None:
            resultado = []
        if nodo:
            self.recorrido_enorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self.recorrido_enorden(nodo.derecha, resultado)
        return resultado

    def buscar_en_rango(self, nodo, minimo, maximo, resultados=None):
        """
        Busca todos los valores dentro del rango [minimo, maximo].
        """
        if resultados is None:
            resultados = []
        if nodo is None:
            return resultados
        if minimo < nodo.valor:
            self.buscar_en_rango(nodo.izquierda, minimo, maximo, resultados)
        if minimo <= nodo.valor <= maximo:
            resultados.append(nodo.valor)
        if nodo.valor < maximo:
            self.buscar_en_rango(nodo.derecha, minimo, maximo, resultados)
        return resultados

    def imprimir_con_indentacion(self, nodo=None, nivel=0):
        """
        Imprime el árbol en consola con indentación para mostrar niveles.
        Imprime primero el subárbol derecho, luego el nodo, luego el subárbol izquierdo.
        Esto ayuda a visualizar el árbol con la raíz hacia la izquierda.
        """
        if nodo is None:
            nodo = self.raiz
        if nodo.derecha:
            self.imprimir_con_indentacion(nodo.derecha, nivel + 1)
        print("    " * nivel + str(nodo.valor))
        if nodo.izquierda:
            self.imprimir_con_indentacion(nodo.izquierda, nivel + 1)

    def contar_hojas(self, nodo):
        """
        Cuenta la cantidad de hojas del árbol.
        Una hoja es un nodo que no tiene hijos (izquierda y derecha son None).
        """
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self.contar_hojas(nodo.izquierda) + self.contar_hojas(nodo.derecha)

    def altura(self, nodo):
        """
        Calcula la altura del árbol.
        La altura es el número máximo de niveles desde la raíz hasta una hoja.
        Un árbol vacío tiene altura 0.
        """
        if nodo is None:
            return 0
        altura_izquierda = self.altura(nodo.izquierda)
        altura_derecha = self.altura(nodo.derecha)
        return 1 + max(altura_izquierda, altura_derecha)


def main():
    abb = ABB()

    print("Insertando valores ordenados:")
    for i in range(1, 21):
        abb.insertar_valor(i)

    print("\nImpresión sencilla con indentación:")
    abb.imprimir_con_indentacion()

    print("\nRecorrido en orden (debe ser lista ordenada):")
    print(abb.recorrido_enorden(abb.raiz))

    print("\nCantidad de hojas en el árbol:", abb.contar_hojas(abb.raiz))
    print("Altura del árbol:", abb.altura(abb.raiz))
    print("Raíz del árbol:", abb.raiz.valor if abb.raiz else None)

    valor_buscado = 15
    nodo = abb.buscar(abb.raiz, valor_buscado)
    print(f"\nBuscar valor {valor_buscado}: ", "Encontrado" if nodo else "No encontrado")

    rango_min, rango_max = 5, 15
    print(f"\nValores en rango [{rango_min}, {rango_max}]:")
    print(abb.buscar_en_rango(abb.raiz, rango_min, rango_max))

    """ Prueba de inserción de valores aleatorios"""
    abb2 = ABB()
    datos = [10, 5, 20, 3, 7, 15, 30, 25, 1, 6]
    for v in datos:
        abb2.insertar_valor(v)

    print("\nImpresión sencilla con indentación:")
    abb2.imprimir_con_indentacion()

    print("\nRecorrido en orden:")
    print(abb2.recorrido_enorden(abb2.raiz))

    print("\nCantidad de hojas en el árbol:", abb2.contar_hojas(abb2.raiz))
    print("Altura del árbol:", abb2.altura(abb2.raiz))
    print("Raíz del árbol:", abb2.raiz.valor if abb2.raiz else None)


if __name__ == "__main__":
    main()
