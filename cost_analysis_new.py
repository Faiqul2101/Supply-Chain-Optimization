import pulp as lp

# PARAMETER

Cdv = { # Asumsi Trailer Petrol dan Truck Petrol
    "ij" : {
        "i1 ke j1" : 4,
        "i1 ke j2" : 5,
        "i2 ke j1" : 4,
        "i2 ke j2" : 5,
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

d = {
    "ij" : {
        "i1 ke j1" : 150,
        "i1 ke j2" : 500,
        "i2 ke j1" : 150,
        "i2 ke j2" : 500,
    },
    
    "jk" : {
        "j1 ke K1" : 100,
        "j1 ke K2" : 350,
        "j1 ke K3" : 100,
        "j1 ke K4" : 350,
        "j2 ke K1" : 100,
        "j2 ke K2" : 350,
        "j2 ke K3" : 100,
        "j2 ke K4" : 350,
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
        "l1 ke i1" : 200,
        "l1 ke i2" : 650,
        "l2 ke i1" : 200,
        "l2 ke i2" : 650,
    },

    "lm" : {
        "l1 ke m1" : 250,
        "l1 ke m2" : 750,
        "l2 ke m1" : 250,
        "l2 ke m2" : 750,
    }
}

# MANUFACTURE COST

PCi = {
    "Manufaktur 1" : 12.5,
    "Manufaktur 2" : 19.5
}

Cre = {
    "Manufaktur 1" : 8,
    "Manufaktur 2" : 13
}

Beta = {
    "Manufaktur 1" : 0.1,
    "Manufaktur 2" : 0.3
}

Png = {
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
    "Collector 1" : 20*20000,
    "Collector 2" : 20*25000
}

# DISPOSER COST

Cdm = {
    "Disposer 1" : 10,
    "Disposer 2" : 13
}

Fbm = {
    "Disposer 1" : 10*30000,
    "Disposer 2" : 10*35000
}

# CAPACITY 
Cppi ={
    "Manufaktur 1" : 135000,
    "Manufaktur 2" : 150000
}

Cri = {
    "Manufaktur 1" : 88000,
    "Manufaktur 2" : 92000
}

Cpdj = {
    "Distributor 1" : 50000,
    "Distributor 2" : 60000   
}

Cccl = {
    "Collector 1" : 70000,
    "Collector 2" : 95000
}

Ccdm = {
    "Disposer 1" : 80000,
    "Disposer 2" : 100000
}


# DEMAND
Dk = {
    "Konsumen 1" : 100000,
    "Konsumen 2" : 110000,
    "Konsumen 3" : 120000,
    "Konsumen 4" : 130000
}

# Kumpulan Keys
manuf_keys = PCi.keys()
distributor_keys = Coj.keys()
konsumen_keys = Dk.keys()
collector_keys = Cccl.keys()
disposer_keys = Ccdm.keys()
Cdv_ij = Cdv["ij"].keys()
Cdv_jk = Cdv["jk"].keys()
Cdv_li = Cdv["li"].keys()
Cdv_lm = Cdv["lm"].keys()
d_ij = d["ij"].keys()
d_jk = d["jk"].keys()
d_kl = d["kl"].keys()
d_li = d["li"].keys()
d_lm = d["lm"].keys()

# Model Problem
problem = lp.LpProblem("Supply_Chain_Optimization", lp.LpMinimize)

# Variabel Manufaktur
QMi = lp.LpVariable.dicts("jumlah_produksi_manuf", manuf_keys, 0,None,cat=lp.LpInteger)
Qrli = lp.LpVariable.dicts("jumlah_produk_remanufaktur", manuf_keys, 0,None,cat=lp.LpInteger)
QPij = lp.LpVariable.dicts("jumlah_produk_dikirim_ke_distributor", distributor_keys, 0,None,cat=lp.LpInteger)
Pd = lp.LpVariable.dicts("penawaran_diskon", manuf_keys, 0,None,cat=lp.LpInteger)
GLti = lp.LpVariable.dicts("parameter_ramah", manuf_keys, 0, 1,cat=lp.LpInteger)

# Variabel Distributor
Qdjk = lp.LpVariable.dicts("produk_to_konsum",konsumen_keys,lowBound=0,upBound=None,cat=lp.LpInteger)
    
# Variabel Konsumen
Rkl =  lp.LpVariable.dicts("konsumen_to_collector",collector_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# Variabel Collector
Ul = lp.LpVariable.dicts("parameter_bangun_collector", collector_keys, 0,1,cat=lp.LpBinary)

# Variabel Disposer
Vm = lp.LpVariable.dicts("parameter_bangun_disposer", disposer_keys, 0,1,cat=lp.LpBinary)
Qslm =  lp.LpVariable.dicts("produk_dibuang",disposer_keys,lowBound=0,upBound=None,cat=lp.LpInteger)

# KALKULASI BIAYA

# Kalkulasi Biaya Manufaktur Cpi = PCi + Beta * GLti
for item1 in manuf_keys :
    for item2 in manuf_keys:
        for item3 in manuf_keys: 
            if GLti[item1] != 0 : 
                biaya_produksi = lp.lpSum((PCi[item1] + Beta[item2]) * QMi[item3]) 
            if GLti[item1] == 0 : 
                biaya_produksi = lp.lpSum(PCi[item1] * QMi[item3]) 

# Kalkulasi Biaya Remanufaktur, Cre * QRli --> Ngga Pengaruh Ke Total Biaya
for item1 in manuf_keys:
    for item2 in manuf_keys: 
        biaya_remanufaktur = lp.lpSum(Cre[item1] * Qrli[item2])

# Kalkulasi Biaya Pengiriman I ke J --> Belum Dibagi Kapasitas Cvr atau Cvt --> Pengaruh ke Total Biaya
for item in Cdv_ij :
    for item2 in distributor_keys :
        for item3 in d_ij :
            biaya_pengiriman_i_j = Cdv["ij"][item] * QPij[item2] * d["ij"][item3]

# Kalkulasi Biaya Diskon Qrli * Pd * Dd --> Ini gabisa di eksekusi karena Qrli dan Pd merupakan variable tidak konstan
# for item1 in manuf_keys :
#     for item2 in manuf_keys :
#         for item3 in manuf_keys :
#             biaya_diskon = lp.lpSum(Qrli[item1]*dd[item3]*Pd[item2])

# Kalkulasi Biaya Penanganan di Distributor Coj * Qdjk --> Ngga Pengaruh Ke Total Biaya
# for item in distributor_keys :
#     for item2 in konsumen_keys :
#         biaya_penanganan = lp.lpSum(Coj[item] * Qdjk[item2])

# Kalkulasi Biaya Pengiriman J ke K --> Belum Dibagi Kapasitas Cvr atau Cvt --> Ngga Pengaruh Ke Total Biaya
# for item in Cdv_jk :
#     for item2 in konsumen_keys :
#         for item3 in d_jk :
#             biaya_pengiriman_j_k = Cdv["jk"][item] * Qdjk[item2] * d["jk"][item3]

# Kalkulasi Fixed Cost Capacity Collector Fcl Ul --> Ngga Pengaruh Ke Total Biaya
# for item in collector_keys :
#     for item2 in collector_keys :
#         if Ul[item2] != 0 :
#             fixed_cost_collector = lp.lpSum(Fcl[item]) * 1
#         if Ul[item2] == 0 :
#             fixed_cost_collector = 0

# Kalkulasi Biaya Pemilahan Ccl Rkl --> Ngga Pengaruh Ke Total Biaya
for item in collector_keys :
    for item2 in collector_keys :
        biaya_pemilahan = lp.lpSum(Ccl[item] * Rkl[item2])

# Fungsi Tujuan
problem += lp.lpSum(biaya_produksi + biaya_remanufaktur + biaya_pengiriman_i_j)

# Constraint
#QPij >= Dk --> Aman
for item1 in distributor_keys :
    for item2 in konsumen_keys :
        problem += lp.lpSum(QPij[item1]) >= lp.lpSum(Dk[item2])

#QMi + QRli == QPij --> Yang Terpilih QRli = 0
for item1 in manuf_keys :
    for item2 in manuf_keys : 
        for item3 in distributor_keys:
            problem += lp.lpSum(QMi[item1]) + lp.lpSum(Qrli[item2]) == lp.lpSum(QPij[item3])

#Qdjk <= QPij
for item in konsumen_keys:
    for item2 in distributor_keys:
        problem += lp.lpSum(Qdjk[item]) <= lp.lpSum(QPij[item2])

#QRli <= (1-Fd) Rkl
for item in manuf_keys :
    for item2 in collector_keys:
        problem += lp.lpSum(Qrli[item]) <= (1-0.5) * lp.lpSum(Rkl[item2])

#QSlm == Fd Rkl
for item in disposer_keys :
    for item2 in collector_keys :
        problem += lp.lpSum(Qslm[item]) == 0.5 * lp.lpSum(Rkl[item2])

#Rkl <= Yk QDjk GLti --> Yk belum terkonversi
for item in collector_keys:
    for item2 in konsumen_keys:
        for item3 in manuf_keys :
            if GLti[item3] != 0 :
                problem += 0.9 * lp.lpSum(Rkl[item]) <= lp.lpSum(Qdjk[item2])
            if GLti[item3] == 0 :
                problem += lp.lpSum(Rkl[item]) == 0
                
#QRli <= Qpij
for item in manuf_keys:
    for item2 in distributor_keys:
        problem += lp.lpSum(Qrli[item]) <= lp.lpSum(QPij[item2])

#QMi <= Cppi
for item in manuf_keys :
    for item2 in manuf_keys:
        problem += lp.lpSum(QMi[item]) <= lp.lpSum(Cppi[item2])

#Qdjk <= Cpdj
for item in konsumen_keys:
    for item2 in distributor_keys :
        problem += lp.lpSum(Qdjk[item]) <= lp.lpSum(Cpdj[item2])

#Rkl <= ul Cccl
for item in collector_keys : 
    for item2 in collector_keys :
        if Ul[item2] != 0 :
            problem += lp.lpSum(Rkl[item]) <= lp.lpSum(Cccl[item2])
        if Ul[item2] == 0 :
            problem += lp.lpSum(Rkl[item]) == 0

#Qrli <= Cri
for item in manuf_keys :
    for item2 in manuf_keys:
        problem += lp.lpSum(Qrli[item]) <= lp.lpSum(Cri[item2])

#Qslm <= vm Ccdm
for item in disposer_keys :
    for item2 in disposer_keys :
        if Vm[item2] != 0 :
            problem += lp.lpSum(Qslm[item]) <= lp.lpSum(Ccdm[item2])
        if Vm[item2] == 0 :
            problem += lp.lpSum(Qslm[item]) == 0

#Pd <= Pngi
for item in manuf_keys :
    for item2 in manuf_keys:
        problem += lp.lpSum(Pd[item]) <= lp.lpSum(Png[item2])

# #Dummy QRli
# for item in manuf_keys:
#     problem += lp.lpSum(Qrli[item]) >= 100

print("=================================")
print("Biaya Produksi : ", biaya_produksi)
# print("Biaya Remanufaktur : ", biaya_remanufaktur)
print("Biaya Pengiriman I ke J : ", biaya_pengiriman_i_j)
# print("Biaya Diskon : ", biaya_diskon)
# print("Biaya Penanganan : ", biaya_penanganan)
# print("Biaya Pengiriman J ke K : ", biaya_pengiriman_j_k)
# print("Biaya Fixed Cost Collector : ", fixed_cost_collector)
# print("Biaya Pemilahan: ", biaya_pemilahan)
print("=================================")

problem.writeLP("Cost_Minimization")
problem.solve()
print("Status:", lp.LpStatus[problem.status])

status = problem.solve()
print(lp.LpStatus[status])

for v in problem.variables():
    print(v.name, "=", v.varValue)

print("Total Biaya =", lp.value(problem.objective))