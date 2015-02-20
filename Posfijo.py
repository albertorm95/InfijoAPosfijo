N=100
#pila=[0 for i in range(N)]
pila=[]

global tope
tope=0

def llena():
    if(tope==(N-1)):
        return True
    return False

def vacia():
    if(tope==-1):
        return True
    return False

def push(dato):
    if(llena()!=True):
        global tope
        tope=tope+1
        #pila[tope]=dato
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

def operando(i, EI):
    abcd='abcdefghijklmnopqrstuvxyz'
    abcd=list(abcd)
    for j in range(len(abcd)):
        if(EI[i]==abcd[j]):
            return True
    return False

def operador(i, EI):
    if(EI[i]!=')'):
        return True

#eistring=raw_input('Ingrese Operacion sin espacios: ')
#EI=list(eistring.lower())
EI=['a','+']
EP=[]
for i in range(2):
    if(operando(i, EI)==True):
        EP.append(EI[i])
    elif(operador(i, EI)==True):
        if (tope==-1):
            push(EI[i])
        #else:
            
            
           

print pila
print EI
print EP


       

