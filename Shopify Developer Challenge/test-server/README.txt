This server side web api was implemented in GraphQL and Javascript and uses graphql-yoga to host a local basic GraphQL server. All the requirements to run the GraphQL server and interact with the api have already been installed. Simply in command prompt enter the test-server directory and enter the command: 

$ npm start

Incase you cannot run the server follow the steps. To install graphql-yoga, run the following in terminal command in the directory ./test-server

$ npm install graphql-yoga

# or, using Yarn:
$ yarn add graphql-yoga

There is a built-in script that restarts the server whenever changes are made using nodemon. To install nodemon run this in a terminal:

$ npm install nodemon --save-dev

# or, using Yarn:
$ yarn add nodemon --dev 


Now to run the GraphQL server on a local computer, type the following in a terminal while in the ./test-server directory:

$ npm start

open a browser(preferably Google Chrome) and go to:

http://localhost:4000/

OR

http://localhost:4000/graphql

I have heard GraphQL is used by shopify, but just in case i will explain how GraphQl works. You input queries or mutations to send to a server, according to the syntax in the schema and list data that you would like the server to change and/or data that you would like the server to tell you.

Below i have provided input data to test the majority of cases that were asked in the document.

UNIT TESTS:
Case 1) Query for all products, regardless of inventory availability:
query{
  allProducts(OnlyStock:false){
    price
    title
    id
    inventory_count
  }
}

Case 2) Query for all products, but only products with available inventory:
query{
  allProducts(OnlyStock:true){
    price	
    title
    id
    inventory_count
  }
}

Case 3) Query for a single product, based on an id of the product
query{
  product(id:"1"){
    price
    id
    title
    inventory_count
  }
}

Case 4) Trying to purchase products in shopping cart without creating a shopping cart:
mutation{
  Checkout{
    cartValue
    cartCreated
    cartProducts{
      price
      inventory_count
      title
      id
    }
  }
}

Case 5) Creating a cart, and checking out with no products inside it:
mutation{
  createCart{
    cartValue
    cartCreated
  }
  Checkout{
    cartValue
    cartCreated
  }
}

RESULT => ERROR: "cart is empty"

Case 6) Creating a cart, adding a product in stock to it, then checking out:
mutation{
  createCart{
    cartValue
    cartCreated
  }
  AddToCart(itemId:"0"){
    cartValue
    cartCreated
    cartProducts{
      price
      id
      inventory_count
      title
    }
  }
  Checkout{
    cartValue
    cartCreated
  }
}

Case 7) Creating a cart, then adding an out of stock product to the cart, and attempting to checkout:
mutation{
  createCart{
    cartValue
    cartCreated
  }
  AddToCart(itemId:"1"){
    cartValue
    cartCreated
    cartProducts{
      price
      id
      inventory_count
      title
    }
  }
  Checkout{
    cartValue
    cartCreated
  }
}

RESULT => Error: "no product match or out of stock"

Case 8) Product inventory shouldn't reduce until after a cart has been completed:
STEP 1) Check inventory count on all products:
query{
  allProducts(OnlyStock:false){
    id
    title
    inventory_count
  	price
}
}
STEP 2) Create a cart and add an in-stock product
mutation{
  createCart{
    cartValue
    cartCreated
  }
  AddToCart(itemId:"0"){
    cartValue
    cartCreated
    cartProducts{
      price
      id
      inventory_count
      title
    }
  }
}
STEP 3) Check for any change to inventory count of product that was added to the cart:
query{
  allProducts(OnlyStock:false){
    id
    title
    inventory_count
  	price
}
}

RESULT => inventory count of product is not changed
