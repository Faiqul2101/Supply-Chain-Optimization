import pulp as lp

#DECLARATION VARIABLES

#Stakeholder
I = 2 # Pemanufaktur
J = 2 # Distributor
K = 4 # Konsumen
L = 2 # Pengumpulan
M = 2 # Pembuangan

# BIAYA PEMANUFAKTUR

## PRODUCTION COST
# 1. Biaya
# production cost = Cpi/PCi
Cpi = [12.5, 15.0, 17.5, 19.5] # -> Asumsi Cpi = PCi

# 2. Jumlah yang diproduksi dan dikirimkan
production_delivery_quantity = [100000, 110000, 120000, 130000] #Qpij = Dk -> Jumlah yang diproduksi = yang Dikirim = Permintaan 

### PERHITUNGAN PRODUCTION COST
perhitungan_production_cost = [Cpi[i]*production_delivery_quantity[i] for i in range(4)]
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
distance_k_l = [90, 95, 97, 100]
distance_l_m = [200, 300, 400, 650]
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

'''
I = PEMANUFAKTUR (i)
J = DISTRIBUTOR (j)
K = KONSUMEN (k)
L = PENGUMPULAN (l)
M = PEMBUANGAN (m)
'''


#CONSTRAINT MODEL
# 1. QPij >= Dk  
# Jumlah Produk yang Diproduksi Pemanufaktur >= Demand Produk



# 2. QDjk <= QPij
# Jumlah Produk yang Dikirim ke Distributor <= Jumlah Jumlah Produk yang Diproduksi Pemanufaktur



# 3. QRli <= (1 - Fd) (Rkl + ... + n)
# Jumlah Produk Penampungan ke Pemanufaktur <= Rumus x Jumlah Produk Konsumen ke Penampungan



# 4. QSlm == Fd (Rkl + ... + n)
# Jumlah Produk Pengumpulan ke Pembuangan == Rumus x Jumlah Produk Konsumen ke Penampungan



# 5. Rkl <= yk (QDjk x GLti + ... + n)
# Jumlah Produk Konsumen ke Penampungan <= yk x Jumlah (Produk Dikirim ke Distributor x Biner 0,1 -> nongreen/green)



# 6. QRli <= M (QPij + ... + n)
# Jumlah Penampungan ke Pemanufaktur <= M (?) x (Jumlah Pemanufaktur ke Distributor)



# 7. QMi <= Cppi
# Jumlah Produk yang Diproduksi Pemanufaktur <= Kapasitas Produksi



# 8. QDjk <= Cpdj
# Jumlah Produk Dikirim Distributor ke Konsumen <= Kapasitas Distributor



# 9. Rkl <= ul Cccl
# Jumlah Produk Dari Konsumen ke Distributor <= ul (?) x Kapasitas Pengumpulan



# 10. QRli <= Cri
# Jumlah Produk Pengumpulan ke Pemanufaktur <= Kapasitas Remanufaktur



# 11. QSlm <= vm Ccdm
# Jumlah Produk Dibuang <= vm (?) x Kapasitas Pembuangan



# 12. yk = (Pd/Png x δk/δ* be^-φq)
# yk (?) = (?)



# 13. Cpi = PCi + βi (t GLti + ... + n)
# Biaya Produksi = Biaya Produksi Produk non Green x Green Factor 



# 14. Pd <= Pngi 
# (?)



# 15. QMi, Qrli, QSlm, Qpij, Qdjk, Rkl Pd, Cpi >= 0
# Semua Jenis Kuantitas dan Kapasitas Produk >= 0


# 16. ul, vm, GLti ∈ {0,1}
# Faktor merupakan Elemen Bilangan Biner (0 atau 1)

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
1. APAKAH Cpi = PCi? -> Ada Rumusnya Di Constraint
2. APAKAH KUANTITAS YANG DIPRODUKSI = KAPASITAS PRODUKSI?
3.
'''