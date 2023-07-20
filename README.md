# Ahorcado
El juego de el ahorcado con municipios de Jalisco

![image](https://github.com/LuisRosado/Ahorcado/assets/140114139/323477fa-fbca-4076-8a5d-49fa125772e2)

Este código en Python implementa el juego del ahorcado con algunas palabras predefinidas. A continuación, te explico cada parte del código:

 -palabras: Es una lista que contiene varias palabras para el juego del ahorcado. Una de estas palabras se seleccionará al azar para que el jugador adivine.

 -palabra: Es una lista que se inicializa con una palabra al azar seleccionada de la lista palabras.

 -horca: Es una lista de cadenas que representan la imagen de la horca en diferentes estados.

 -ahorcado: Es una lista de cadenas que representan la imagen del ahorcado en diferentes estados.

 -letras_todas: Es una lista que almacenará todas las letras que el usuario ingrese, para que no repita letras.

 -fallos: Es un contador que representa la cantidad de intentos fallidos que ha tenido el jugador al adivinar la palabra.

 -resultado: Es una lista que se inicializa con "_", que luego se irá llenando con las letras adivinadas correctamente.

Luego del setup inicial, el código entra en un bucle principal (while True) donde se ejecutará el juego hasta que se gane o se llegue a un límite de intentos fallidos (3 en este caso).

En cada iteración del bucle, se muestra la imagen de la horca y el estado actual de las letras adivinadas (las letras correctas y las letras que aún faltan por adivinar).

El usuario ingresa una letra, y se realizan comprobaciones para asegurarse de que la entrada sea válida: una sola letra, no repetida y una letra del alfabeto.

Si la letra ingresada por el usuario está en la palabra a adivinar, se actualiza la lista resultado para mostrar la letra en la posición correcta.

Si la letra ingresada no está en la palabra, se incrementa el contador fallos.

Si el jugador adivina todas las letras de la palabra (resultado es igual a palabra), se muestra un mensaje de felicitaciones y se termina el juego.

Si el jugador alcanza el límite de intentos fallidos (3 en este caso), se muestra la palabra completa y un mensaje de que ha perdido.

Después de cada iteración del bucle, se borra la pantalla y se repite el proceso para la siguiente ronda del juego.

En resumen, este código implementa un juego del ahorcado donde el jugador debe adivinar una palabra seleccionada al azar de una lista predefinida. El juego muestra la horca y el estado de las letras adivinadas, y el jugador tiene un límite de 3 intentos fallidos antes de perder.
