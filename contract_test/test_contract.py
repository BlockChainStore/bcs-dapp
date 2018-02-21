from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete

from boa.code.builtins import concat, list, range, take, substr

OWNER = b'\xd3h\x8c\x06{,\xc2\xf4\r\xe6\xb1\x19nA\xdb\xf64u\xf4\xc3'
dApp_name = 'bcs_test'
VERSION = 1

def Main(operation, args):

    trigger = GetTrigger()

    if trigger == Verification():
        is_owner = CheckWitness(OWNER)

        if is_owner:
            return True

        return False

    elif trigger == Application():
        # Check the version for compatability
        if operation == 'initial':
            res = False
            if (len(args) == 0):
                print('checking if its the owner')
                isowner = CheckWitness(OWNER)
                if isowner:
                     print('it is the owner')
                     context = GetContext()
                     owner_value = Get(context, OWNER)
                     if (owner_value == 0) :
                         Put(context, 'name',dApp_name)
                         Put(context, OWNER,1000)
                         res = True
                     else :
                         print('You are Already Initialize')

            else:
                Log('INVALID_ARGUMENTS')

            return res

        elif operation == 'regis':
            res = False
            if (len(args) == 1):
                addr = args[0]
                Log('Registration')
                context = GetContext()
                addr_regis = Get(context, addr)
                if (addr_regis == 0) :
                      Put(context, addr,100)
                      res = True
                else :
                      print('You are Already Register')
            else:
                Log('INVALID_ARGUMENTS')
                return False

            return res
                
        elif operation == 'value':
            res = 0
            if (len(args) == 1):
                addr = args[0]
                isowner = CheckWitness(addr)
                if isowner:
                     context = GetContext()
                     value = Get(context, addr)
                     if not (value == 0) :
                         res = value
                     else :
                         print('You are not Registration')
                
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False

            return False
        
        elif operation == 'add':
            if (len(args) == 2):
                addr = args[0]
                value_added = args[1]
                isowner = CheckWitness(OWNER)
                if isowner:
                     context = GetContext()
                     value = Get(context, addr)
                     if not (value == 0) :
                         data = value_added+value
                         Put(context, addr, data)
                         print('value added')
                         return True
                     else :
                         print('The Addresss no Register yet')
                else :
                     print('You are not Owner')
                return False
            else:
                Log('INVALID_ARGUMENTS')
                return False

            return False 
    
        Log('INVALID_FUNCTION')
        return False

    Log('FORBIDDEN')
    return False

