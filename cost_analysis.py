import pulp as lp

#DECLARATION VARIABLES

#Stakeholder
I = 2 # Pemanufaktur
J = 2 # Distributor
K = 4 # Konsumen
L = 2 # Pengumpulan
M = 2 # Pembuangan

## DATA COLLECTION
# Kuantitas dan Kapasitas
Dk =  [100000, 110000, 120000, 130000]  # --> Demand Produk 
Cppi = [135000, 140000, 145000, 150000] # --> Kapasitas Maksimal Produksi Manufaktur
Cri = [88000, 90000, 91000, 92000]      #--> Kapasitas Maksimal Remanufaktur
CPdj = [50000, 53000, 56000, 60000]     #--> Kapasitas Maksimal Distributor
Cccl = [70000, 85000, 90000, 95000]     #--> Kapasitas Maksimal Pusat Pengumpulan
Cccdm = [80000, 90000, 95000, 100000]   #--> Kapasitas Maksimal Pusat Pembuangan

# Fixed Cost
fcl = [400000, 440000, 480000, 500000]  #--> Biaya Pendirian Fasilitas Pengumpulan
fbm = [300000, 320000, 340000, 350000]  #--> Biaya Pendirian Fasilitas Pembuangan

# Variable Cost
Coj = [5, 6, 7, 8]          #--> Biaya Penanganan Produk di Distributor 
Ccl = [13, 14, 15, 17]      #--> Biaya Pemilahan Produk di Pengumpulan
Crei = [8, 9, 10, 13]       #--> Biaya Remanufaktur di Pemanufaktur
Cdl = [10, 11, 12, 14]      #--> Biaya Pemusnahan di Pembuangan

PCi = [12.5, 15.0, 17.5, 19.5]

# Delivery Cost (Vehicle Based)
Cdv = {
    "Truck (Hybrid Motor)": [13,14],
    "Truck with Petrol" : [9,10],
    "Trailer (Hybrid Motor)": [6,7],
    "Trailer with Petrol" : [4,5]
}

Cdv_keys = Cdv.keys()

# Distance
dij = [150, 200, 300, 500]  #--> Distance Pemanufaktur (i) ke Distributor (j)
djk = [100, 150, 200, 350]  #--> Distance Distributor (j) ke Konsumen (k)
dkl = [90, 95, 97, 100]     #--> Distance Konsumen (k) ke Pengumpulan (l)
dli = [200, 300, 400, 650]  #--> Distance Pengumpulan (l) ke Pemanufaktur (i)
dlm = [250, 500, 600, 750]  #--> Distance Pengumpulan (l) ke Pembuangan (m)

# Faktor-Faktor Biner
GLti = [0, 1, 0, 1]         #--> Produksi Green Produk atau Tidak (1,0)

# Faktor-Faktor Pendukung Lain
B = [0.1, 0.2, 0.25, 0.3]   #--> Faktor Biaya Produksi Green
Pngi = [50, 52, 54, 55]     #--> Harga Produk Non-Green
Png = 55                    #--> Maksimum Harga Produk Non-Green
Fd = 0.5                    #--> Proporsi Produk Bekas Pakai Yang Dibuang
q = [0.3, 0.4, 0.45 ,0.5]   #--> Tingkat Penerimaan Kualitas Produk Bekas Pakai (Menghitung Yk)

# BIAYA PEMANUFAKTUR (1)

## PRODUCTION COST
# 1. Biaya Produksi (Cpi)
Cpi = [PCi[item] + B[item] * GLti[item] for item in range(4)] #--> Cpi = PCi x Faktor Green

# 2. Jumlah yang diproduksi dan dikirimkan (QPij)
QPij = [Dk[item] * 0.8 for item in range(4)] #QPij = Dk x Proporsi

# print(QPij)

### PERHITUNGAN PRODUCTION COST
production_cost = [Cpi[i]*QPij[i] for i in range(4)]
print(production_cost)

## DELIVERY COST MANUFACTURE -> DISTRIBUTOR
# 1. Biaya per Kendaraan (cdv)

# 2. Jarak (dij)

### PERHITUNGAN DELIVERY COST
delivery_cost = [Cdv[i]*dij[i] for i in range(4)]

# 3. Jumlah Produk Yang Dikirimkan Dari Pemanufaktur ke Distributor 
# Pakai Jumlah yang diproduksi

### PERHITUNGAN DELIVERY COST
perhitungan_delivery_cost = [dij[i]*production_delivery_quantity[i] for i in range(4)]

## REMANUFACTURE COST (Crei x Qrli)
# 1. Biaya Remanufaktur (Crei)

# 2. Jumlah yang diremanufaktur (Qrli)

### PERHITUNGAN REMANUFACTURE COST
perhitungan_remanufacture_cost = [Crei[i]*Qrli[i] for i in range(4)]

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
Dk = lp.LpVariable("Demand", 0, None)
QPij = lp.LpVariable("Jumlah Produksi", 0, None, lp.LpInteger)


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
problem += QPij >= Dk


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
1. Rumus be^-φq serta masing-masing variable itu apa?
2. Proporsi Untuk Masing-Masing Perpindahan itu Berapa?
3. Jumlah Tempat Manufaktur, Distributor, Konsumen dst itu kan berbagai macam.
   Sedangkan Datanya berbentuk Distribusi, Contohnya Jarak. Nah itu nanti untuk Jumlah Tempatnya
   akan Berpengaruh ke perhitungan atau mengikuti distribusi saja?
4. GLti perhitungan faktor binernya seperti apa? Apakah 1 objek diasumsikan memiliki satu faktor biner
   (A : 1, B : 0 dst) atau satu faktor disimulasikan 2 kali? (A:0, A:1, B:0, B:2)
'''