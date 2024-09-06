Cdv = { # Asumsi Trailer Petrol dan Truck Petrol
    "ij" : {
        "i1 ke j1" : 4,
        "i1 ke j2" : 5,
        "i2 ke j1" : 4,
        "i2 ke j2" : 4,
    },

    "jk" : {
        "j1 ke K1" : 9,
        "j1 ke K2" : 10,
        "j1 ke K3" : 9,
        "j1 ke K4" : 10,
        "j2 ke K1" : 9,
        "j2 ke K2" : 10,
        "j2 ke K3" : 9,
        "j2 ke K4" : 10,
    },

    "li" : {
        "l1 ke i1" : 9,
        "l1 ke i2" : 10,
        "l2 ke i1" : 9,
        "l2 ke i2" : 10,
    },

    "lm" : {
        "l1 ke m1" : 9,
        "l1 ke m2" : 10,
        "l2 ke m1" : 9,
        "l2 ke m2" : 10,
    }
}

abc = Cdv["ij"].keys()

print(abc)