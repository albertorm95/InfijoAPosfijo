abcd=list('ABCDEFGHIJKLMNOPQRSTUVXYZ')
udt=list('0123456789')
N=50
pila=[]
EP=[]
tope=-1

def llena():
    if(tope==(N-1)):
        print 'STACKOVERFLOW'
        return True
    return False

def vacia():
    if(tope==-1):
        'STACKUNDERFLOW'
        return True
    return False

def push(dato):
    if(llena()!=True):
        global tope
        tope=tope+1
        pila.insert(tope,dato)

def pop():
    if(vacia()!=True):
        global tope
        aux=pila[tope]
        del pila[tope]
        tope=tope-1
        return aux
    else:
        return -9999

def infijo(i, EI):
    if(EI[i]=='^'):
        prioridadop=4
        return prioridadop
    elif(EI[i]=='*'):
        prioridadop=2
        return prioridadop
    elif(EI[i]=='/'):
        prioridadop=2
        return prioridadop
    elif(EI[i]=='+'):
        prioridadop=1
        return prioridadop
    elif(EI[i]=='-'):
        prioridadop=1
        return prioridadop
    elif(EI[i]=='('):
        prioridadop=5
        return prioridadop

def pripila(pila):
    if(pila[tope]=='^'):
        prioridadpi=3
        return prioridadpi
    elif(pila[tope]=='*'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='/'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='+'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='-'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='('):
        prioridadpi=0
        return prioridadpi


eistring=raw_input('Ingrese Operacion sin espacios: ')
EI=list(eistring.upper())

for i in range(len(EI)):
    if(EI[i] in abcd or EI[i] in udt):      #EI es operando
        EP.append(EI[i])
    elif(EI[i]!=')'):                       #EI es diferente a ')'
        if (tope==-1):                      #Pila no esta vacia
            push(EI[i])
        else:
            if(infijo(i,EI)<=pripila(pila)):#operador de EI es <= a operador de pila
                EP.append(pop())                
                push(EI[i])
            elif(infijo(i,EI)>pripila(pila)):#operador de EI es > a operador de pila
                push(EI[i])
    elif(EI[i]==')'):                       #EI es igual a ')'
        while (pila[tope]!='('):            #Pila es diferente a '('
            EP.append(pop())
        if(pila[tope]=='('):                #Pila es igual a '('
            pop()
        elif(tope!=-1):                     #Pila no esta vacia
            EP.append(pop())

while (tope>-1):                
    EP.append(pop())
print ''.join(EP)        














