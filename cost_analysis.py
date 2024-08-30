import pulp as lp

#DECLARATION VARIABLES

#Stakeholder
I = 2 # Pemanufaktur
J = 2 # Distributor
K = 4 # Konsumen
M = 2 # Pengumpulan
N = 2 # Pembuangan

# BIAYA PEMANUFAKTUR

## PRODUCTION COST
# 1. Biaya
production_cost = [12.5, 15.0, 17.5, 19.5] # -> Asumsi Cpi = PCi

# 2. Jumlah yang diproduksi dan dikirimkan
production_delivery_quantity = [100000, 110000, 120000, 130000] #Qpij = Dk -> Jumlah yang diproduksi = yang Dikirim = Permintaan 

### PERHITUNGAN PRODUCTION COST
perhitungan_production_cost = [production_cost[i]*production_delivery_quantity[i] for i in range(4)]
print(perhitungan_production_cost)

## REMANUFACTURE COST
# 1. Biaya 
remanufacture_cost = [8, 10, 12, 13]

# 2. Jumlah yang diremanufaktur
# -> Harus tau Qjk dan Qkl. Qli = (1-Fd) * Qkl

### PERHITUNGAN REMANUFACTURE COST
perhitungan_remanufacture_cost = []


## DELIVERY COST MANUFACTURE -> DISTRIBUTOR
# 1. Biaya per Kendaraan
cost_vehicle_per_distance = {
    "Truck (Hybrid Motor)": [13,14],
    "Truck with Petrol" : [9,10],
    "Trailer (Hybrid Motor)": [6,7],
    "Trailer with Petrol" : [4,5]
}


# 2. Jarak 
distance_i_j = [150, 200, 300, 500]
distance_j_k = [100, 150, 200, 350]
distance_k_m = [90, 95, 97, 100]
distance_m_i = [200, 300, 400, 650]
distance_m_n = [250, 500, 600, 750]

# 3. Jumlah Produk Yang Dikirimkan Dari Pemanufaktur ke Distributor 
# Pakai Jumlah yang diproduksi

### PERHITUNGAN DELIVERY COST
perhitungan_delivery_cost = [distance_i_j[i]*production_delivery_quantity[i] for i in range(4)]


## DISCOUNT COST
# 1. Biaya
discount_cost = []

# 2. Jumlah Produk Kembali
return_product_quantity = []

# 3. Pengaruh Diskon Terhadap Demand
dd = [0.5, 0.6, 0.7, 0.8] # Asumsi 

### PERHITUNGAN DISCOUNT COST
perhitungan_discount_cost = [discount_cost[i]*return_product_quantity[i]*dd[i] for i in range(4)]


#MODEL
problem = lp.LpProblem("Cost_Minimization", lp.LpMinimize)

#DECISION VARIABLES
# Biaya Produksi
biaya_produksi = lp.LpVariable.dicts("Biaya_Produksi", perhitungan_production_cost, 0, None, lp.LpContinuous)

# Biaya Remanufaktur
biaya_remanufacture = lp.LpVariable.dicts("Biaya_Remanufacture", perhitungan_remanufacture_cost, 0, None, lp.LpContinuous)

# Biaya Pengiriman ke Distributor
biaya_pengiriman_i_j = lp.LpVariable.dicts("Biaya_Pengiriman_i_j", perhitungan_delivery_cost, 0, None, lp.LpContinuous)

# Biaya Pemberian Diskon
biaya_diskon = lp.LpVariable.dicts("Biaya_Diskon", perhitungan_discount_cost, 0, None, lp.LpContinuous)

#OBJECTIVE FUNCTION TOTAL COST -> MASIH BIAYA MANUFAKTUR
problem += (
    lp.lpSum(biaya_produksi[a] for a in biaya_produksi) +
    lp.lpSum(biaya_remanufacture[b] for b in biaya_produksi) +
    lp.lpSum(biaya_pengiriman_i_j[c] for c in biaya_produksi) +
    lp.lpSum(biaya_diskon[d] for d in biaya_produksi) 
)

#Fungsi Batasan
# ... Menyesuaikan

#Penyelesaian
problem.writeLP("Cost_Minimization")
problem.solve()
print("Status:", lp.LpStatus[problem.status])

print(problem)
status = problem.solve()
print(lp.LpStatus[status])

for v in problem.variables():
    print(v.name, "=", v.varValue)

print("Total Biaya =", lp.value(problem.objective))


# NOTES
'''
1. KAPASITAS DIGUNAKAN SEBAGAI FUNGSI BATASAN
2.
'''

#LIST PERTANYAAN
'''
1. APAKAH Cpi = PCi?
2. APAKAH KUANTITAS YANG DIPRODUKSI = KAPASITAS PRODUKSI?
3.
'''