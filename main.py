
import json

def cargar_datos(ruta):

    #Opening JSON File
    with open(ruta) as contenido:
        #returns JSON as a dictionary
        valores = json.load(contenido)
        return valores
        
def count_comments(valores):

        numbers = []
        #loop to access each dictionary in the list
        for elem in valores:
             #To add an item to the end of the list
             numbers.append(elem['userId'])

        #Counting all items with count()
        result = [[x,numbers.count(x)] for x in set(numbers)]
        print(result)

def last_two(valores):
    comments = []
    n=0
    for elem in valores:
        if ((elem['id']-n) % 9 == 0 or elem['id'] % 10 == 0):
             #To add an item to the end of the list
             comments.append(elem['body'])
             n+=0.5
             
    result = [[comments[i], comments[i+1]] for i in range(0, 10, 2)]       
    print(result)

if __name__ == '__main__':
    ruta = 'descarga.json'
    print("Comentarios que tiene cada usuario: ")
    valores = cargar_datos(ruta)

    count_comments(valores)
    last_two(valores)