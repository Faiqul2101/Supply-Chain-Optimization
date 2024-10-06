import pulp as lp

# PARAMETER
Cvl = {             #Trailer Capacity
    # "i1 ke j1" : 23,
    # "i1 ke j2" : 25,
    # "i2 ke j1" : 23,
    # "i2 ke j2" : 25,
    "M1 ke D1" : 23,
    "M1 ke D2" : 25,
    "M2 ke D1" : 23,
    "M2 ke D2" : 25,
        }

Cvt = {             #Truck Capacity
    "jk" : {
        'Konsumen 1' : 10,
        'Konsumen 2' : 12,
        'Konsumen 3' : 10,
        'Konsumen 4' : 12,
        # "j1 ke K1" : 10,
        # "j1 ke K2" : 12,
        # "j1 ke K3" : 10,
        # "j1 ke K4" : 12,
        # "j2 ke K1" : 10,
        # "j2 ke K2" : 12,
        # "j2 ke K3" : 10,
        # "j2 ke K4" : 12,
    },

    "li" : {
        "Manufaktur 1" : 10,
        "Manufaktur 2" : 12
    },

    "lm" : {
        "Disposer 1" : 10,
        "Disposer 2" : 12
    },

    "is" : {
        "i1 ke s1" : 10,
        "i1 ke s2" : 12,
        "i1 ke s3" : 10,
        "i1 ke s4" : 12,
        "i2 ke s1" : 10,
        "i2 ke s2" : 12,
        "i2 ke s3" : 10,
        "i2 ke s4" : 12,
    },
    
    "sl" : {
        "s1 ke l1" : 10,
        "s2 ke l1" : 12,
        "s3 ke l1" : 10,
        "s4 ke l1" : 12,
        "s1 ke l2" : 10,
        "s2 ke l2" : 12,
        "s3 ke l2" : 10,
        "s4 ke l2" : 12,
    }
}

Cdv = { # Asumsi Trailer Petrol dan Truck Petrol
    "ij" : {
        "M1 ke D1" : 4,
        "M1 ke D2" : 5,
        "M2 ke D1" : 4,
        "M2 ke D2" : 5,
        # "i1 ke j1" : 4,
        # "i1 ke j2" : 5,
        # "i2 ke j1" : 4,
        # "i2 ke j2" : 5,
    },

    "jk" : {
        'Konsumen 1' : 9,
        'Konsumen 2' : 10,
        'Konsumen 3' : 9,
        'Konsumen 4' : 10,
        # "j1 ke K1" : 9,
        # "j1 ke K2" : 10,
        # "j1 ke K3" : 9,
        # "j1 ke K4" : 10,
        # "j2 ke K1" : 9,
        # "j2 ke K2" : 10,
        # "j2 ke K3" : 9,
        # "j2 ke K4" : 10,
    },

    "li" : {
        "Manufaktur 1" : 9,
        "Manufaktur 2" : 10
    },

    "lm" : {
        "Disposer 1" : 9,
        "Disposer 2" : 10
    },

    "is" : {
        "i1 ke s1" : 9,
        "i1 ke s2" : 10,
        "i1 ke s3" : 9,
        "i1 ke s4" : 10,
        "i2 ke s1" : 9,
        "i2 ke s2" : 10,
        "i2 ke s3" : 9,
        "i2 ke s4" : 10,
    },
    
    "sl" : {
        "s1 ke l1" : 9,
        "s2 ke l1" : 10,
        "s3 ke l1" : 9,
        "s4 ke l1" : 10,
        "s1 ke l2" : 9,
        "s2 ke l2" : 10,
        "s3 ke l2" : 9,
        "s4 ke l2" : 10,
    }
}

d = {
    "ij" : {
        "M1 ke D1" : 150,
        "M1 ke D2" : 500,
        "M2 ke D1" : 150,
        "M2 ke D2" : 500,
    },
    
    "jk" : {
        'Konsumen 1' : 100,
        'Konsumen 2' : 350,
        'Konsumen 3' : 100,
        'Konsumen 4' : 350,
        # "j1 ke K1" : 100,
        # "j1 ke K2" : 350,
        # "j1 ke K3" : 100,
        # "j1 ke K4" : 350,
        # "j2 ke K1" : 100,
        # "j2 ke K2" : 350,
        # "j2 ke K3" : 100,
        # "j2 ke K4" : 350,
    },

    "kl" : {
        "k1 ke l1" : 90,
        "k1 ke l2" : 100,
        "k2 ke l1" : 90,
        "k2 ke l2" : 100,
        "k3 ke l1" : 90,
        "k3 ke l2" : 100,
        "k4 ke l1" : 90,
        "k4 ke l2" : 100,
    },

    "li" : {
        "Manufaktur 1" : 200,
        "Manufaktur 2" : 650,
    },

    "lm" : {
        "Disposer 1" : 250,
        "Disposer 2" : 750
    },

    "is" : {
        "i1 ke s1" : 110,
        "i1 ke s2" : 125,
        "i1 ke s3" : 110,
        "i1 ke s4" : 125,
        "i2 ke s1" : 110,
        "i2 ke s2" : 125,
        "i2 ke s3" : 110,
        "i2 ke s4" : 125,
    },

    "sl" : {
        "s1 ke l1" : 150,
        "s2 ke l1" : 200,
        "s3 ke l1" : 150,
        "s4 ke l1" : 200,
        "s1 ke l2" : 150,
        "s2 ke l2" : 200,
        "s3 ke l2" : 150,
        "s4 ke l2" : 200,
    }
}

# MANUFACTURE COST

PCi = {
    "Manufaktur 1" : 12.5,
    "Manufaktur 2" : 12.5
}

Cre = {
    "Manufaktur 1" : 8,
    "Manufaktur 2" : 13
}

Beta = {
    "Manufaktur 1" : 0.1,
    "Manufaktur 2" : 0.3
}

Pngi = {
    "Manufaktur 1" : 50,
    "Manufaktur 2" : 55
}

q = {
    "Manufaktur 1" : 0.3,
    "Manufaktur 2" : 0.5
}

b = {
    "Manufaktur 1" : 0.1,
    "Manufaktur 2" : 0.3
}

dd = {
    "Manufaktur 1" : 0.3,
    "Manufaktur 2" : 0.5
}

# SECONDARY MARKET
Csr = {
    "Sekunder 1" : 30,
    "Sekunder 2" : 35,
    "Sekunder 3" : 45,
    "Sekunder 4" : 50,
}


# DISTRIBUTOR COST

Coj = {
    "Distributor 1" : 5,
    "Distributor 2" : 8
}

# COLLECTOR COST

Ccl = {
    "Collector 1" : 13,
    "Collector 2" : 17
}

Fcl = {
    "Collector 1" : 20*20,
    "Collector 2" : 20*25
}

# DISPOSER COST

Cdl = {
    "Disposer 1" : 10,
    "Disposer 2" : 13
}

Fbm = {
    "Disposer 1" : 10*30,
    "Disposer 2" : 10*35
}

# CAPACITY 
Cppi ={
    "Manufaktur 1" : 235,
    "Manufaktur 2" : 250
}

Cri = {
    "Manufaktur 1" : 88,
    "Manufaktur 2" : 92
}

Cpdj = {
    "Distributor 1" : 350,
    "Distributor 2" : 275   
}

Cccl = {
    "Collector 1" : 70,
    "Collector 2" : 95
}

Ccdm = {
    "Disposer 1" : 80,
    "Disposer 2" : 100
}

# DEMAND
Dk = {
    "Konsumen 1" : 100,
    "Konsumen 2" : 110,
    "Konsumen 3" : 120,
    "Konsumen 4" : 130
}

Ds = {
    "Sekunder 1" : 25,
    "Sekunder 2" : 35,
    "Sekunder 3" : 45,
    "Sekunder 4" : 50,
}

# KONSUMEN
Pd = {
    "Konsumen 1" : 50,
    "Konsumen 2" : 52,
    "Konsumen 3" : 54,
    "Konsumen 4" : 55,
}

kesadaran_lingkungan = {
    "Konsumen 1" : 0,
    "Konsumen 2" : 1,
    "Konsumen 3" : 2,
    "Konsumen 4" : 3,
}
# PARAMETER TAMBAHAN
# epsilon = 1e-6

dummy = ["M1 ke D1", "M1 ke D2"]
dummy2 = ["M2 ke D1", "M2 ke D2"]
dummy3 = ["D1 ke K1", "D1 ke K2", "D1 ke K3", "D1 ke K4"]
dummy4 = ["D2 ke K1", "D2 ke K2", "D2 ke K3", "D2 ke K4"]
dummy5 = ["K1 ke C1", "K2 ke C1", "K3 ke C1", "K4 ke C1"]
dummy6 = ["K1 ke C2", "K2 ke C2", "K3 ke C2", "K4 ke C2"]
dummy7 = ["Konversi_C1 ke M1", "Konversi_C1 ke M2"]
dummy8 = ["Konversi_C2 ke M1", "Konversi_C2 ke M2"]

# Kumpulan Keys
manuf_keys = PCi.keys()
distributor_keys = Coj.keys()
konsumen_keys = Dk.keys()
sekunder_keys = Ds.keys()
collector_keys = Cccl.keys()
disposer_keys = Ccdm.keys()
Cdv_ij = Cdv["ij"].keys()
Cdv_jk = Cdv["jk"].keys()
Cdv_li = Cdv["li"].keys()
Cdv_lm = Cdv["lm"].keys()
Cdv_is = Cdv["is"].keys()
Cdv_sl = Cdv["sl"].keys()
d_ij = d["ij"].keys()
d_jk = d["jk"].keys()
d_kl = d["kl"].keys()
d_li = d["li"].keys()
d_lm = d["lm"].keys()
d_is = d["is"].keys()
d_sl = d["sl"].keys()
Cvl_keys = Cvl.keys()
Cvt_keys_jk = Cvt["jk"].keys()
Cvt_keys_li = Cvt["li"].keys()
Cvt_keys_lm = Cvt["lm"].keys()
Cvt_keys_is = Cvt["is"].keys()
Cvt_keys_sl = Cvt["sl"].keys()

# PENENTUAN YK
yk = []
for item in konsumen_keys :
    a = Pd[item]/55*kesadaran_lingkungan[item]/3*((2.71**(-5*0.1)*0.9))
    # a = int(a)
    yk.append(a)

proporsi_pengembalian = dict(zip(konsumen_keys, yk))

print("proporsi", proporsi_pengembalian)
print("proporsi", proporsi_pengembalian.values())
# Model Problem
problem = lp.LpProblem("Supply_Chain_Optimization", lp.LpMinimize)

# Variabel Manufaktur
PMi = lp.LpVariable.dicts("PMi", manuf_keys, 0,None,cat=lp.LpInteger)
# Pd = lp.LpVariable.dicts("Pd", manuf_keys, 0,None,cat=lp.LpInteger)
Pre = lp.LpVariable.dicts("Pre", manuf_keys, 0,None,cat=lp.LpInteger)
QPij = lp.LpVariable.dicts("Qpij", manuf_keys, 0,None,cat=lp.LpInteger)
QPij1 = lp.LpVariable.dicts("Qpij Manuf 1", dummy, 0,None,cat=lp.LpInteger)
QPij2 = lp.LpVariable.dicts("Qpij Manuf 2", dummy2, 0,None,cat=lp.LpInteger)
GLti = lp.LpVariable.dicts("GLti", manuf_keys, 0, 1,cat=lp.LpInteger)

Qrli = lp.LpVariable.dicts("Qrli", manuf_keys, 0,None,cat=lp.LpInteger)
Qrli1 = lp.LpVariable.dict("Qrli Collector 1", dummy7,0, None, cat=lp.LpInteger)
Qrli2 = lp.LpVariable.dict("Qrli Collector 2", dummy8,0, None, cat=lp.LpInteger)

# Variabel Distributor
# Qdjk = lp.LpVariable.dicts("Qdjk",konsumen_keys,lowBound=0,upBound=None,cat=lp.LpInteger)
Qdjk = lp.LpVariable.dicts("Qdjk",distributor_keys,lowBound=0,upBound=None,cat=lp.LpInteger)
Qdjk1 = lp.LpVariable.dicts("Qdjk Distributor 1",dummy3,lowBound=0,upBound=None,cat=lp.LpInteger)
Qdjk2 = lp.LpVariable.dicts("Qdjk Distributor 2",dummy4,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Konsumen
Rkl =  lp.LpVariable.dicts("Rkl",collector_keys,lowBound=0,upBound=None,cat=lp.LpInteger)
Rkl1 =  lp.LpVariable.dicts("Rkl",dummy5,lowBound=0,upBound=None,cat=lp.LpInteger)
Rkl2 =  lp.LpVariable.dicts("Rkl",dummy6,lowBound=0,upBound=None,cat=lp.LpInteger)
Rkl_Konsumen =  lp.LpVariable.dicts("Rkl",konsumen_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Sekunder
Qmis =  lp.LpVariable.dicts("Qmis",sekunder_keys,lowBound=0,upBound=None,cat=lp.LpInteger)
Qmis1 =  lp.LpVariable.dicts("Qmis",manuf_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Collector
Ul = lp.LpVariable.dicts("Ul", collector_keys, 0,1,cat=lp.LpBinary)
Qwsl =  lp.LpVariable.dicts("Qwsl",collector_keys,lowBound=0,upBound=None,cat=lp.LpInteger)
Qwsl1 =  lp.LpVariable.dicts("Qwsl",sekunder_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Disposer
Vm = lp.LpVariable.dicts("vm", disposer_keys, 0,1,cat=lp.LpBinary)
Qslm =  lp.LpVariable.dicts("Qslm",disposer_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# KALKULASI BIAYA
# ...

# FUNGSI TUJUAN
problem += lp.lpSum((PCi[item]+Beta[item]) * QPij[item] for item in manuf_keys ) 
rumus3 = lp.lpSum(Cdv['ij'][item]*QPij1[item]*(1/Cvl[item])*d["ij"][item] for item in dummy) + lp.lpSum(Cdv['ij'][item]*QPij2[item]*(1/Cvl[item])*d["ij"][item] for item in dummy2)

print("Tes rumus",rumus3)

# Constraint
#1. QPij
#QPij >= Dk --> Aman
problem += lp.lpSum(QPij[item1] for item1 in manuf_keys) >= lp.lpSum(Dk[item2] for item2 in konsumen_keys)

#QPij1 = QPij[Manufaktur1] --> Aman
problem += lp.lpSum(QPij1[item] for item in dummy) == QPij["Manufaktur 1"]

#QPij2 = QPij[Manufaktur2] --> Aman
problem += lp.lpSum(QPij2[item] for item in dummy2) == QPij["Manufaktur 2"]

#Qpij <= Cppi --> Aman
for item in manuf_keys :
    problem += QPij[item] <= Cppi[item]

#2. Qdjk
#QPij1 + QPij2 == Qdjk --> Aman
#Konversi QPij1 dan QPij2 ke Qdjk1 Distributor 1 dan Distributor 2 --> Aman
problem += QPij1["M1 ke D1"] + QPij2["M2 ke D1"] == Qdjk["Distributor 1"]
problem += QPij1["M1 ke D2"] + QPij2["M2 ke D2"] == Qdjk["Distributor 2"]

#Qdjk <= Cpdj --> Aman
for item in distributor_keys :
    problem += Qdjk[item] <= Cpdj[item]
    
#Memastikan jumlah yang dikirim ke Konsumen 1,2,3,4 == Jumlah barang yg ada di Distributor 1 atau 2 --> Aman
problem += lp.lpSum(Qdjk1[item] for item in dummy3) <= Qdjk["Distributor 1"]
problem += lp.lpSum(Qdjk2[item] for item in dummy4) <= Qdjk["Distributor 2"]
    
# #Memastikan Barang yang dikirim D1 dan D2 tidak melebihi permintaan konsumen 1, 2, 3, 4 --> Aman
problem += Qdjk1["D1 ke K1"] + Qdjk2["D2 ke K1"] == Dk["Konsumen 1"]
problem += Qdjk1["D1 ke K2"] + Qdjk2["D2 ke K2"] == Dk["Konsumen 2"]
problem += Qdjk1["D1 ke K3"] + Qdjk2["D2 ke K3"] == Dk["Konsumen 3"]
problem += Qdjk1["D1 ke K4"] + Qdjk2["D2 ke K4"] == Dk["Konsumen 4"]

#3. Rkl
#Rkl <= Yk QDjk GLti --> Aman
#Konversi dari Qdjk Konsumen 1 ke Rkl Konsumen 1, Qdjk Konsumen 2 ke Rkl Konsumen 2, dst --> Aman
problem += proporsi_pengembalian["Konsumen 1"] * (Qdjk1["D1 ke K1"] + Qdjk2["D2 ke K1"]) <= Rkl_Konsumen["Konsumen 1"]
problem += proporsi_pengembalian["Konsumen 2"] * (Qdjk1["D1 ke K2"] + Qdjk2["D2 ke K2"]) <= Rkl_Konsumen["Konsumen 2"]
problem += proporsi_pengembalian["Konsumen 3"] * (Qdjk1["D1 ke K3"] + Qdjk2["D2 ke K3"]) <= Rkl_Konsumen["Konsumen 3"]
problem += proporsi_pengembalian["Konsumen 4"] * (Qdjk1["D1 ke K4"] + Qdjk2["D2 ke K4"]) <= Rkl_Konsumen["Konsumen 4"]

#Konversi Rkl Konsumen ke Rkl1 dan Rkl2 (Untuk Pengiriman) --> Aman
problem += Rkl1["K1 ke C1"] + Rkl2["K1 ke C2"] == Rkl_Konsumen["Konsumen 1"]
problem += Rkl1["K2 ke C1"] + Rkl2["K2 ke C2"] == Rkl_Konsumen["Konsumen 2"]
problem += Rkl1["K3 ke C1"] + Rkl2["K3 ke C2"] == Rkl_Konsumen["Konsumen 3"]
problem += Rkl1["K4 ke C1"] + Rkl2["K4 ke C2"] == Rkl_Konsumen["Konsumen 4"]

#Konversi Rkl1 ke Rkl Collector 1 dan Rkl2 ke Rkl Collector 2 --> Aman
problem += lp.lpSum(Rkl1[item] for item in dummy5) == Rkl["Collector 1"]
problem += lp.lpSum(Rkl2[item] for item in dummy6) == Rkl["Collector 2"]

#Rkl <= ul Cccl --> Problem : Rkl Konsumen 4 menyesuaikan Kebutuhan Maksimasi Kapasitas Pengumpulan --> Aman
#Memastikan jumlah yang diterima dari konsumen 1,2,3,4 memenuhi kapasitas Collector 1,2 --> Aman
problem += lp.lpSum(Rkl1[item] for item in dummy5) <= Cccl["Collector 1"]
problem += lp.lpSum(Rkl2[item] for item in dummy6) <= Cccl["Collector 2"]

#Memastikan Total Jumlah yang dikirimkan oleh Konsumen = Total Jumlah yang diterima oleh Collector --> Aman
problem += lp.lpSum(Rkl1[item] for item in dummy5) + lp.lpSum(Rkl2[item] for item in dummy6) <= Cccl["Collector 1"] + Cccl["Collector 2"]

#4. Qrli
#Memastikan Qrli yang dikirim ke M1 dan M2 == Rkl yang ada di C1 atau C2
problem += Rkl["Collector 1"] == 0.5 * (Qrli1["Konversi_C1 ke M1"] + Qrli1["Konversi_C1 ke M2"])
problem += Rkl["Collector 2"] == 0.5 * (Qrli2["Konversi_C2 ke M1"] + Qrli2["Konversi_C2 ke M2"])

#QRli <= (1-Fd) Rkl
#Memastikan Qrli merupakan proporsi dari Rkl
problem += Qrli["Manufaktur 1"] == (1-0.5) * (Qrli1["Konversi_C1 ke M1"] + Qrli2["Konversi_C2 ke M1"])
problem += Qrli["Manufaktur 2"] == (1-0.5) * (Qrli1["Konversi_C1 ke M2"] + Qrli2["Konversi_C2 ke M2"])

#QRli <= Qpij
problem += lp.lpSum(Qrli[item1] for item1 in manuf_keys) <= lp.lpSum(QPij[item2] for item2 in manuf_keys)

#Qrli <= Cri
for item in manuf_keys :
    problem += Qrli[item] <= Cri[item]

#5. Qmis
#Qmis <= Qrli
#problem += lp.lpSum(Qmis1[item1] for item1 in manuf_keys) <= lp.lpSum(Qrli[item2] for item2 in manuf_keys)

#Qmis >= Ds --> Aman
problem += lp.lpSum(Qmis1[item1] for item1 in manuf_keys) >= lp.lpSum(Ds[item2] for item2 in sekunder_keys)

#6. Qwsl
#Qwsl <= ul Csrl 
problem += lp.lpSum(Qwsl1[item]for item in sekunder_keys) <= lp.lpSum(Csr[item1]for item1 in sekunder_keys)

#7. Qslm
#QSlm == Fd Rkl + Qwsl
# problem += lp.lpSum(Qslm[item1] for item1 in disposer_keys) == 0.5 * lp.lpSum(Rkl1[item2] for item2 in konsumen_keys) + lp.lpSum(Qwsl1[item3] for item3 in sekunder_keys )

#Qslm <= vm Ccdm
problem += lp.lpSum(Qslm[item] for item in disposer_keys) <= lp.lpSum(Ccdm[item1] for item1 in disposer_keys)

problem.writeLP("Cost_Minimization")
problem.solve()
print("Status:", lp.LpStatus[problem.status])

status = problem.solve(lp.PULP_CBC_CMD(msg=0))
print(lp.LpStatus[status])
print(problem)

for v in problem.variables():
    print(v.name, "=", v.varValue)
print("Total Biaya =", lp.value(problem.objective))