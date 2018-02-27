from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete

from boa.code.builtins import concat, list, range, take, substr

BCSCHAIN = b'\x0b\xf5\xe0J\xffj\x97\x03\\\xdeH\x98i\x86\xf4\xe3\xfa`\x9fy'
VERSION = 1

def Main(operation, args):
    """
    This is the main entry point for the dApp
    :param operation: the operation to be performed
    :type operation: str
    :param args: an optional list of arguments
    :type args: list
    :return: indicating the successful execution of the dApp
    :rtype: string
    """
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
                width = args[3]
                length = args[4]
                height = args[5]

                Log('Owning_Area')
                res = own_area(addr,lat,lon,width,length,height)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False

        elif operation == 'regisProduct':
            if (len(args) == 3):
                seller_addr = args[0]
                product_hash = args[1]

                Log('Registering_Product')
                res = create_product(seller_addr,product_hash)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False
                
        elif operation == 'activateProduct':
            if (len(args) == 2):
                seller_addr = args[0]
                product_hash = args[1]

                Log('Activating_Product')
                res = activate_product(seller_addr ,product_hash)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False
        
        elif operation == 'setPrice':
            if (len(args) == 3):
                seller_addr = args[0]
                product_hash = args[1]
                price = args[2]

                Log('Setting_Price')
                res = set_price(seller_addr,product_hash,price)
                return res
            else:
                Log('INVALID_ARGUMENTS')
                return False


        elif operation == 'buyProduct':
            if (len(args) == 2):
                buyer_addr = args[0]
                product_hash = args[1]

                Log('Buying_Product')
                res = buy_product(buyer_addr,product_hash)
                return res

            else:
                Log('INVALID_ARGUMENTS')
                return False

        elif operation == 'deactivateProduct':
            if (len(args) == 2):
                seller_addr = args[0]
                product_hash = args[1]

                Log('Deactivating_Product')
                res = deactivate_product(seller_addr,product_hash)
                return res

            else:
                Log('INVALID_ARGUMENTS')
            return False

        Log('INVALID_FUNCTION')
        return False

    Log('FORBIDDEN')
    return False

def own_area(owner_address , lat,lon,width,length,height) :
    if not CheckWitness(owner_address):
        Log('FORBIDDEN')
        return False
    
    context = GetContext()
    address = Get(context, owner_address)
    obj = [lat,lon,width,length,height]
    location = _data_packing(obj)
    
    if (address == 0):
        Put(context, owner_address, location)
        Log('OWNED_SUCCESS')
        return True
    else :
        Log('AlREADY_OWNED')

    return False

def create_product(seller_address , p_hash) :
    if not CheckWitness(seller_address):
        Log('FORBIDDEN')
        return False
    
    if is_owned_area(seller_address):
        context = GetContext()
        price = 0
        status = 'inactive'
        obj = [seller_address,price,status]
        product_data = _data_packing(obj)
        Put(context, p_hash, product_data)
        Log('Product_Registered')
        return True
    
    return False

def set_price(seller_address , p_hash, price) :
    if not CheckWitness(seller_address):
        Log('FORBIDDEN')
        return False
    
    if is_owned_product(p_hash,seller_address) :
        context = GetContext()
        status = 'active'
        obj = [seller_address,price,status]
        product_data = _data_packing(obj)
        Put(context, p_hash, product_data)
        Log('SUCCESS')
        
        return True
    
    return False

def activate_product(seller_address , p_hash) :
    if _set_product_status(seller_address,p_hash,'active') :
        Log('ACTIVE_SUCCESS')
        return True
    
    return False

def deactivate_product(seller_address ,p_hash):
    if _set_product_status(seller_address,p_hash,'inactive') :
        Log('DEACTIVE_SUCCESS')
        return True

    return False

def buy_product(buyer_address , p_hash):
    if not CheckWitness(buyer_address):
        Log('FORBIDDEN')
        return False

    Log('CAN_NOT_BUY_THE_PRODECT')
    return False

##################################################
# helper function for handling
##################################################

def _set_product_status(seller_address,p_hash,status):
    if not CheckWitness(seller_address):
        Log('FORBIDDEN')
        return False
    
    if is_owned_product(p_hash,seller_address) :
        context = GetContext()
        product_data_get = Get(context, p_hash)
        price = _get_price(product_data_get)
        obj = [seller_address,price,status]
        product_data = _data_packing(obj)
        Put(context, p_hash, product_data)
        
        return True

    return False

def is_owned_area(owner_address):
    
    return True

def is_owned_product(p_hash,seller_address):
    
    return True

def _get_owner(product_data) :
    obj = _data_unpacking(product_data)
    owner = obj[0]

    return owner

def _get_price(product_data) :
    obj = _data_unpacking(product_data)
    price = obj[1]

    return price

def _get_status(product_data) :
    obj = _data_unpacking(product_data)
    status = obj[2]

    return status

def _change_owner(p_hash,new_owner_address) :
    context = GetContext()
    product_data_get = Get(context, p_hash)
    if not len(product_data_get) == 0:
        obj = _data_unpacking(product_data_get)
        obj = [new_owner_address,obj[1],obj[2]]
    
        product_data = _data_packing(obj)
        Put(context, p_hash, product_data)
        
        return True

    return False


# helper function for data handling
def _data_unpacking(data_str):
    output = list()
    str_tmp=''
    for c in data_str :
        if (c == ';'):
            output.append(str_tmp)
            str_tmp = ''
        else :
            str_tmp = str_tmp+c
            
    return output

def _data_packing(items):
    output_str = ''
    for item in items:
        output_str = concat(output_str,item)
        output_str = concat(output_str,';')
    
    return output_str

