# BCS Dapp

[![N|Solid](https://bcschain.io/wp-content/uploads/2018/01/bsc-logo-main-70px-1.png)](https://bcschain.io)

BlochChainStore is an decentralized app that aims to offer Augmented Reality services to its users.
## Abstract
Blockchain Store(BCS) is a virtual reality platform powered by 
the Neo blockchain. Users can create, experience,
and monetize content and application. Shop or area in BCS is permanently
owned by the community. giving them control over their creation.
Users claim ownership of virtual shop or area on a blockchain-base ledger.
Shop or area owners contral what content is published to their portion,
which is identified by a set of cartesion coordinates(x,y). Contents can be
range from static, dynamic 3D scenes, charactor to interactitve system. 

##  The Function in Smart Contract
- **ownArea [seller_address, lat, lon, width, length, height]** => This Function is using for Seller to owning the area in VR World
- **regisProduct [seller_address, p_hash]** => This Function is for registering the product by using the hash to represent the product object, the status of new registered product is 'inactive' 
- **setPrice [seller_address, p_hash, price]** => This Function is for set price of the product. When invoked, the status of product change to 'active', only owner of the product can set the price
- **activateProduct [seller_address, p_hash]** => Using for Activate the Product , only owner of the product can activate
- **deactivateProduct [seller_address, p_hash]** =>  Using for Deactivate the Product , only owner of the product can deactivate
- **buyProduct [buyer_address, p_hash]** => This Function is for buyer to buy the product ,When the Process success ,owner of product will changed to buyer


License
----

[MIT](https://opensource.org/licenses/MIT)