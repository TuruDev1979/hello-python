### Traductor ###

aurebesh = {" ":" ","a":"aurek","b":"besh","c":"cresh","ch":"cherek","d":"dorn","e":"esk",
            "eo":"onith","f":"forn","g":"grek","h":"herf","i":"isk","j":"jenth","k":"krill",
            "kh":"krenth","l":"leth","m":"mern","n":"nern","ng":"nen","o":"osk","oo":"orenth",
            "p":"peth","q":"qek","r":"resh","s":"senth","sh":"sen","t":"trill","th":"thesh",
            "u":"usk","v":"vev","w":"wesk","x":"xesh","y":"yirt","z":"zerek",}

palabra = input("¿Qué palabra quieres traducir?")
palabra = palabra.lower()
traduccion = ""

for letra in palabra:
    traduccion += aurebesh[letra]

print(traduccion.capitalize())