from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def verificar_cliente():
    ci = request.json.get('ci')

    codRes, menRes, accion = inicializarcliente(ci)

    salida = {
        'accion': accion,
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci
    }
    return jsonify(salida)

def inicializarcliente(ci):
    cliente = "6213141"
    codRes = "SIN_ERROR"
    menRes = "OK"

    try:
        print("Verificar cliente")
        if ci == cliente:
            print("Cliente encontrado")
            accion = "Success"
            codRes = "SIN_ERROR"
            menRes = "OK"
            ci= ci

        else:
            print("Cliente no encontrado")
            accion = "Cliente no está en el sistema"
            codRes = "ERROR"
            menRes = "Error cliente"
            ci = ci
    except Exception as e:
        print("ERROR:", str(e))
        codRes = "ERROR"
        menRes = "Msg: " + str(e)
        accion = "Error interno"
    
    return codRes, menRes, accion

