'''
    MIT License

    Copyright (c) 2024 José Luis Alvarez Gago

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''


# Diccionario con solo números:
solnu = {12: '1 segundo', 13: '5 segundos', 14: '52 minutos', 15: '9 minutos',
16: '1 hora', 17: '14 horas', 18: '6 días'}
# Diccionario con solo letras mayúsculas O minúsculas:
letiy = {9: '3 segundos', 10: '1 minuto', 11: '32 minutos', 12: '14 horas',
13: '2 semanas', 14: '1 año', 15: '27 años', 16: '713 años', 17: '18.000 años',
18: '481.000 años'}
# Diccionario con letras minúsculas Y mayúsculas:
lmimy = {7: '1 segundo', 8: '28 segundos', 9: '24 minutos', 10: '21 horas',
11: '1 mes', 12: '6 años', 13: '332 años', 14: '17.000 años', 15: '898.000 años',
16: '46 millones de años', 17: '2 billones de años', 18: '126 billones de años'}
# Diccionario con letras minúsculas, mayúsculas y números:
numyi = {7: '2 segundos', 8: '2 minutos', 9: '2 horas', 10: '5 días',
11: '10 meses', 12: '53 años', 13: '3000 años', 14: '202.000 años',
15: '12 millones de años', 16: '779 millones de años',
17: '48 billones de años', 18: '2 trillones de años'}
# Diccionario con letras minúsculas, mayúsculas, números y simbolos:
niysi = {7: '4 segundos', 8: '5 minutos', 9: '6 horas', 10: '2 semanas',
11: '3 años', 12: '226 años', 13: '15.000 años', 14: '1 millón de años',
15: '77 millones de años', 16: '5 billones de años', 17: '380 billones de años',
18: '26 trillones de años'}

def numPwd():
    global uso
    global tie
    uso = "números:"
    if 0 <= lo <= 11:
        tie = "un instante..."
    else:
        tie = (solnu.get(lo))

def alfPwd():
    global uso
    global tie
    if (pas.islower() == True):
        uso = "letras minúsculas."
        if 0 <= lo <= 8:
            tie = "un instante..."
        else:
            tie = (letiy.get(lo))
    elif (pas.isupper() == True):
        uso = "letras mayúsculas."
        if 0 <= lo <= 8:
            tie = "un instante..."
        else:
            tie = (letiy.get(lo))
    else:
        uso = "letras minúsculas y mayúsculas."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (lmimy.get(lo))

def varPwd():
    igno = ["ª", "º", "#", "$", "¿", "?", "^", "¨", "*", "¡", "!", "'", "%", "€", "%", "~", "&", "/", "(", ")", "=", ".", ",", ":", ";", "{", "}", "ç", "<",">", "|", " ", "+", "-", "_", "[", "]"]
    mayu = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minu = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    mume = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    global uso
    global tie
    ctr1 = False
    ctr2 = False
    ctr3 = False
    ctr4 = False
    for i in pas:
        if i in igno:
            ctr1 = True
        else:
            for i in pas:
                if i in mayu:
                    ctr2 = True
                else:
                    for i in pas:
                        if i in minu:
                            ctr3 = True
                        else:
                            for i in pas:
                                if i in mume:
                                    ctr4 = True
                                else:
                                    pass
    if ctr1 == True and ctr2 == True and ctr3 == True and ctr4 == True:
        uso = "letras minúsculas, mayúsculas, números y símbolos."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (niysi.get(lo))
    elif ctr2 == True and ctr3 == True and ctr4 == True:
        uso = "letras minúsculas, mayúsculas y números."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (numyi.get(lo))
    elif ctr2 == True and ctr4 == True:
        uso = "letras mayúsculas y números."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (numyi.get(lo))
    elif ctr3 == True and ctr4 == True:
        uso = "letras minúsculas y números."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (numyi.get(lo))
    elif ctr2 == True and ctr3 == True and ctr1 == True:
        uso = "letras minúsculas, mayúsculas y símbolos."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (numyi.get(lo))
    elif ctr3 == True and ctr1 == True:
        uso = "letras minúsculas y símbolos."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (numyi.get(lo))
    elif ctr2 == True and ctr1 == True:
        uso = "letras mayúsculas y símbolos."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (numyi.get(lo))
    elif ctr4 == True and ctr1 == True:
        uso = "números y símbolos."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (numyi.get(lo))
    elif ctr1 == True:
        uso = "símbolos."
        if 0 <= lo <= 6:
            tie = "un instante..."
        else:
            tie = (solnu.get(lo))
    else:
        pass

def ejePwd():
    global uso
    global tie
    if (pas.isdigit()) == True:
        numPwd()
    elif (pas.isalpha()) == True:
        alfPwd()
    else:
        varPwd()
    if uso is not None:
        print("La contraseña introducida está formada por " + uso)
    else:
        print("Ha ocurrido un error: No está contemplada la constitución de su contraseña, revise las instrucciones.")
    if tie is not None:
        print("Podría ser crackeada en " + tie)
    else:
        print("Ha ocurrido un error: No está contemplada el tiempo de crackeo de su contraseña, revise las instrucciones.")


def main():
    global pas
    global lo
    pas = input("Introduzca la contraseña a estudiar (máximo 18 caracteres): ")
    lo = len(pas)
    if lo > 18:
        lo = str(lo)
        print("Ha habido un error. La contraseña debe tener entre 1 y 18 caracteres. La introducida tiene " + lo + ".")
    else:
        ejePwd()

if __name__ == '__main__':
    main()

