/**
 * Allows the use of graphql yoga content
 */
const {
    GraphQLServer
} = require('graphql-yoga');

/**
 * List of product to keep track of all product in store
 * docs for 'product' discussed later
 */
var products = [{
        id: '0',
        title: 'Fidget Spinner',
        price: 5.99,
        inventory_count: 1000,
    },
    {
        id: '1',
        title: 'Unicorn Backpack',
        price: 19.99,
        inventory_count: 0,
    }
];
/**
 * Default cart to keep track of attributes
 */
var cart;
cart = {
    cartProducts: null,
    cartValue: 0,
    cartCreated: false,
}

/**
 * All types indicating their relationships between each other, attributes,
 * return types and argument types
 *
 * type product: an individual item that has a unique id to other product,
 * and data specific to itself
 *
 * type shoppingCart: an individual container of multiple product and stores
 * cartValue representing the value of all product
 *
 *
 * allproducts: Returns a list of all products and only available
 * products if OnlyStock is true.
 *
 * product: Returns a product with a matching id
 *
 * Checkout: Purchases all product(s) in cart and empties cart
 *
 * createCart: Creates a shopping cart
 *
 * AddToCart: Adds a product with matching itemid to an existing cart
 */
const typeDefs = `
  type product {
    id: ID!
    title: String!
    price: Float!
    inventory_count: Int!
  }
  type shoppingCart{
    cartProducts: [product!]!
    cartValue: Float!
    cartCreated: Boolean!
  }
  type Query {
    allProducts(OnlyStock: Boolean!): [product!]!
    product(id: ID!): product!

  }
  type Mutation {
    Checkout: shoppingCart!
    createCart: shoppingCart!
    AddToCart(itemId: ID!): shoppingCart!
  }
`;

const resolvers = {
    Query: {
      /**
       * Returns a list of all products and only available products if OnlyStock
       */
        allProducts: (_, {
            OnlyStock
        }) => {
            if (OnlyStock) {
                let find_products = products.filter(x => (x.inventory_count > 0));
                if (!find_products) {
                    throw new Error('Cannot find your products!');
                }
                return find_products;
            } else {
                return products;
            }
        },
        /**
         * Returns a product with a matching id
         */
        product: (_, {
            id
        }) => {
            const product = products.find(x => x.id === id);
            if (!product) {
                throw new Error('Cannot find your product!');
            }
            return product;
        }
    },
    Mutation: {
      /**
       * Purchases all product(s) in cart and empties cart
       */
        Checkout: (_, ) => {

            if (!cart.cartCreated) {
                throw new Error('please create cart first')
            }
            if (!cart.cartProducts) {
                throw new Error('cart is empty')
            }


            var i;
            for (i = 0; i < cart.cartProducts.length; i++) {
                const product = products.find(x => x.id === cart.cartProducts[i].id);
                product.inventory_count -= 1;

            }

            cart = {
                cartProducts: undefined,
                cartValue: 0,
                cartCreated: false,
            }

            return cart

        },
        /**
         * Adds a product with matching itemid to an existing cart
         */
        AddToCart: (_, {
            itemId
        }) => {
            if (cart.cartCreated) {
                var productMatch;
                productMatch = products.find(x => x.id === itemId)
                if (!productMatch || productMatch.inventory_count <= 0) {
                    throw new Error('no product match or out of stock')
                } else {

                    cart.cartValue += productMatch.price

                }

                var addOne = {
                    id: itemId,
                    title: productMatch.title,
                    price: productMatch.price,
                    inventory_count: productMatch.inventory_count,
                }
                if (!cart.cartProducts) {
                    cart.cartProducts = [addOne];
                } else {
                    cart.cartProducts = [...cart.cartProducts, addOne];
                }
                //throw new Error(cart);
            } else {
                throw new Error('please create a shoppingCart first')
            }
            cart.cartCreated = true
            return cart
        },
        /**
         * Creates a shopping cart
         */
        createCart: (_, ) => {
            cart.cartCreated = true;
            return cart
        },
    }
}

/**
 * specifies which port and URL extension to use for the server
 */
const opts = {
    port: 4000,
    endpoint: '/graphql'
}

/**
 * Create the server which we will send our GraphQL queries and mutations to.
 */
const server = new GraphQLServer({
    typeDefs,
    resolvers,
    opts
});

/**
 * Turn the server on by listening to a port.
 * http://localhost:4000
 */
server.start(() => {
    console.log(
        `😄 Server running at http://localhost:${opts.port}${opts.endpoint}`
    );
});
