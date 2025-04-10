def verificar_acl():
    
    numero_acl = input("Introduce el número de ACL IPv4 dentro el rango 1-199: ")
    try:
        numero_acl = int(numero_acl)
    except ValueError:
        print("El número ingresado no es válido. Debe ser un número entero.")
        return
    if 1 <= numero_acl <= 99:
        print(f"El número {numero_acl} corresponde a una ACL Estándar.")
    
    elif 100 <= numero_acl <= 199:
        print(f"El número {numero_acl} corresponde a una ACL Extendida.")
    
    else:
        print(f"El número {numero_acl} no corresponde a una lista de acceso válida.")

verificar_acl()
