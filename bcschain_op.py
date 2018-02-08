from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete


BCSCHAIN = b''
VERSION = 1

def Main(operation, args):

    trigger = GetTrigger()

    if trigger == Verification():
        is_owner = CheckWitness(BCSCHAIN)

        if is_owner:
            return True

        return False

    elif trigger == Application():
        # Check the version for compatability
        if operation == 'ownArea':
            if (len(args) == 3):
                addr = args[0]
                lat = args[1]
                lon = args[2]

                Log('Owning_Area')
                res = own_area(addr,lat,lon)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False

        elif operation == 'createProduct':
            if (len(args) == 3):
                addr = args[0]
                uuid = args[1]
                p_name = args[2]

                Log('Creating_Product')
                res = create_product(addr,uuid,p_name)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False
                
        elif operation == 'activateProduct':
            if (len(args) == 2):
                addr = args[0]
                uuid = args[1]

                Log('Activating_Product')
                res = activate_product(addr ,uuid)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False
        
        elif operation == 'setPrice':
            if (len(args) == 3):
                addr = args[0]
                uuid = args[1]
                price = args[2]

                Log('Setting_Price')
                res = set_price(addr,uuid,price)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False


        elif operation == 'buyProduct':
            if (len(args) == 2):
                addr = args[0]
                uuid = args[1]

                Log('Buying_Product')
                res = buy_product(addr,uuid)
                return res

            else:
                Log('INVALID_ARGUMENTS')
                return False

        elif operation == 'deactivateProduct':
            if (len(args) == 2):
                addr = args[0]
                uuid = args[1]

                Log('Deactivating_Product')
                res = deactivate_product(addr,uuid)
                return res

            else:
                Log('INVALID_ARGUMENTS')
            return False

        Log('INVALID_FUNCTION')
        return False

    Log('FORBIDDEN')
    return False

def own_area(owner_address , lat, lon) :
    if not CheckWitness(owner_address):
        Log('FORBIDDEN')
        return False
    
    address = Get(context, owner_address)
    location = [lat,lon]

    if (address == 0):
        Put(context, owner_address, location)
        Log('owned_success')
        return True

    return False

def create_product(address , uuid, product_name) :
    return False

def set_price(address , uuid, price) :
    return False

def activate_product(address , uuid) :
    return False

def buy_product(address , uuid):
    return False

def deactivate_product(address ,uuid):
    return False
