[the function can be invoke]

initial []  => Only Owner of the smart contract can be invoke this function, the initialize will create the data {'name','bcs_test'} and {'owner_address',1000}
regis ["address"]  => This Function is for user to register in the system , this will create the data {'user_address',100}
value ["address"]  => This Function is to Show the data value of the user who has been registered, only the user can see their own data value
add ["address",value]  => This Function for the Owner of the Contract to add some value for the user

