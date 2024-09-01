import pulp as lp

#DECLARATION VARIABLES

Manufaktur = ["M1", "M2"]
Distributor = ["D1", "D2"]
Konsumen = ["K1", "K2", "K3", "K4"]
Pengumpulan = ["P1", "P2"]
Pembuangan = ["PB1", "PB2"]

## DATA COLLECTION
# Kuantitas dan Kapasitas
Dk =  [100000, 110000, 120000, 130000]  # --> Demand Produk 
Cppi = [135000, 140000, 145000, 150000] # --> Kapasitas Maksimal Produksi Manufaktur
Cri = [88000, 90000, 91000, 92000]      #--> Kapasitas Maksimal Remanufaktur
CPdj = [50000, 53000, 56000, 60000]     #--> Kapasitas Maksimal Distributor
Cccl = [70000, 85000, 90000, 95000]     #--> Kapasitas Maksimal Pusat Pengumpulan
Ccdm = [80000, 90000, 95000, 100000]   #--> Kapasitas Maksimal Pusat Pembuangan

# Fixed Cost
fcl = [400000, 440000, 480000, 500000]  #--> Biaya Pendirian Fasilitas Pengumpulan
fbm = [300000, 320000, 340000, 350000]  #--> Biaya Pendirian Fasilitas Pembuangan

# Variable Cost
Coj = [5, 6, 7, 8]              #--> Biaya Penanganan Produk di Distributor 
Ccl = [13, 14, 15, 17]          #--> Biaya Pemilahan Produk di Pengumpulan
Crei = [8, 9, 10, 13]           #--> Biaya Remanufaktur di Pemanufaktur
Cdl = [10, 11, 12, 14]          #--> Biaya Pemusnahan di Pembuangan

PCi = [12.5, 15.0, 17.5, 19.5]  #--> Biaya Produksi Non Hijau

# Delivery Cost (Vehicle Based)
Cdv = {
    "Truck (Hybrid Motor)": [13,14],
    "Truck with Petrol" : [9,10],
    "Trailer (Hybrid Motor)": [6,7],
    "Trailer with Petrol" : [4,5]
}

Cdv_Temporary = [13, 9, 6, 4]

Cdv_keys = Cdv.keys()
Cdv_dicts = lp.LpVariable.dicts("Vehicles",Cdv_keys,lowBound=0,upBound=None,cat=lp.LpContinuous)

print(Cdv_dicts)
# Distance
dij = [150, 200, 300, 500]  #--> Distance Pemanufaktur (i) ke Distributor (j)
djk = [100, 150, 200, 350]  #--> Distance Distributor (j) ke Konsumen (k)
dkl = [90, 95, 97, 100]     #--> Distance Konsumen (k) ke Pengumpulan (l)
dli = [200, 300, 400, 650]  #--> Distance Pengumpulan (l) ke Pemanufaktur (i)
dlm = [250, 500, 600, 750]  #--> Distance Pengumpulan (l) ke Pembuangan (m)

# Faktor-Faktor Biner
GLti = [0, 1, 0, 1]         #--> Produksi Green Produk atau Tidak (1,0)
ul = [0, 1, 0, 1]           #--> Fasilitas Pengumpulan Dibangun atau Tidak (1,0)
vm = [0, 1, 0, 1]           #--> Fasilitas Pembuangan Dibangun atau Tidak (1,0)

# Faktor-Faktor Pendukung Lain
B = [0.1, 0.2, 0.25, 0.3]   #--> Faktor Biaya Produksi Green
Pngi = [50, 52, 54, 55]     #--> Harga Produk Non-Green
Png = [55, 55, 55, 55]      #--> Maksimum Harga Produk Non-Green
Pd = [0, 20, 40, 55]        #--> Maksimum Penawaran Diskon
Fd = [0.5, 0.5, 0.5, 0.5]   #--> Proporsi Produk Bekas Pakai Yang Dibuang
q = [0.3, 0.4, 0.45 ,0.5]   #--> Tingkat Penerimaan Kualitas Produk Bekas Pakai (Menghitung Yk)
a = [0, 1, 2, 3]            #--> Tingkat Kesadaran Lingkungan Konsumen Berdasarkan Zona

### PEMANUFAKTUR
## PRODUCTION COST (Cpi x QPij)
Cpi = [PCi[item] + B[item] * GLti[item] for item in range(4)]   #--> Cpi = PCi x Faktor Green
QPij = [Dk[item] * 0.8 for item in range(4)]                    #QPij = Dk x Proporsi
production_cost = [Cpi[i]*QPij[i] for i in range(4)]
print(production_cost)

## DELIVERY COST MANUFACTURE -> DISTRIBUTOR (Cdv x dij x QPij) --> Cdv Belom
# delivery_cost_ij = [Cdv_dicts[item] *dij[i]*QPij[i] for item in Cdv for i in range(4)]
delivery_cost_ij = [Cdv_Temporary[i] *dij[i]*QPij[i] for i in range(4)]

### DISTRIBUTOR
## HANDLING COST (BIAYA PENANGANAN) (Coj x QPij)
handling_cost = [Coj[i]*QPij[i] for i in range(4)]

## DELIVERY COST DISTRIBUTOR -> KONSUMEN (Cdv x djk x QDjk)
QDjk = [QPij[item] * 0.8 for item in range(4)]
delivery_cost_jk = [Cdv_Temporary[i]* djk[i]*QDjk[i] for i in range(4)]

### PENGUMPULAN
## BUILD FACILITY COST L (fcl x ul)
facility_cost_l = [fcl[i] * ul[i] for i in range(4)]

## SORTING COST (Cccl x Rkl)
Yk = [Pd[i]/Png[i] * a[i]/3 for i in range(4)]                  #--> Tingkat Pengembalian Produk Bekas Pakai
# Rkl = [QDjk[item] * 0.8 for item in range(4)]                 #--> Ada Rumusnya Rkl <= Yk x QDjk x GLti
Rkl = [QDjk[item] * Yk[item] * GLti[item] for item in range(4)] #--> Jumlah Produk Bekas Pakai yang Dikembalikan Konsumen      
sorting_cost = [Cccl[i] * Rkl[i] for i in range(4)]

## DELIVERY COST PENGUMPULAN -> PEMANUFAKTUR (Cdv x dli x QRli)
QRli = [Rkl[item] * 0.5 for item in range(4)]
delivery_cost_li = [Cdv_Temporary[i]*dli[i]*QRli[i] for i in range(4)]

## DELIVERY COST PENGUMPULAN -> PEMBUANGAN (Cdv x dlm x QSlm)
QSlm = [Rkl[item] * 0.5 for item in range(4)]
delivery_cost_lm = [Cdv_Temporary[i]*dlm[i]*QSlm[i] for i in range(4)]

### PEMANUFAKTUR (2)
## REMANUFACTURE COST (Crei x QRli)
remanufacture_cost = [Crei[i]*QRli[i] for i in range(4)]

## DISCOUNT COST (QRli x Pd x Dd)
Dd = [0.5, 0.6, 0.7, 0.8] # Asumsi 
### PERHITUNGAN DISCOUNT COST
discount_cost = [Pd[i]*QRli[i]*Dd[i] for i in range(4)]

### PEMBUANGAN
## BUILD FACILITY COST (2) (fbm x vm)
facility_cost_m = [fbm[i] * vm[i] for i in range(4)]

## DISPOSAL COST (Cdl x QSlm)
disposal_cost = [Cdl[i] * QSlm[i] for i in range (4)]

#MODEL
problem = lp.LpProblem("Cost_Minimization", lp.LpMinimize)

print(problem)
#DECISION VARIABLES
Dk = lp.LpVariable("Demand", 0, None, lp.LpContinuous)
QPij = lp.LpVariable("Jumlah Produksi", 0, None, lp.LpContinuous)

# PRODUCTION COST
biaya_produksi = lp.LpVariable.dicts("Biaya_Produksi", production_cost, 0, None, lp.LpContinuous)

print(biaya_produksi)
# DELIVERY COST MANUFACTURE -> DISTRIBUTOR
biaya_pengiriman_ij = lp.LpVariable.dicts("Biaya_Pengiriman_ij", delivery_cost_ij, 0, None, lp.LpContinuous)

# HANDLING COST
biaya_penanganan = lp.LpVariable.dicts("Biaya_Penanganan", handling_cost, 0, None, lp.LpContinuous)

# DELIVERY COST DISTRIBUTOR -> KONSUMEN
biaya_pengiriman_jk = lp.LpVariable.dicts("Biaya_Pengiriman_jk", delivery_cost_jk, 0, None, lp.LpContinuous)

# BUILD FACILITY COST L
biaya_pembangunan_fasilitas_l = lp.LpVariable.dicts("Biaya_Pembangunan_Fasilitas_L", facility_cost_l, 0, None, lp.LpContinuous)

# SORTING COST
biaya_pemilahan = lp.LpVariable.dicts("Biaya_Pemilahan", sorting_cost, 0, None, lp.LpContinuous)

# DELIVERY COST PENGUMPULAN -> PEMANUFAKTUR
biaya_pengiriman_li = lp.LpVariable.dicts("Biaya_Pengiriman_li", delivery_cost_li, 0, None, lp.LpContinuous)

# DELIVERY COST PENGUMPULAN -> PEMBUANGAN
biaya_pengiriman_lm = lp.LpVariable.dicts("Biaya_Pengiriman_lm", delivery_cost_lm, 0, None, lp.LpContinuous)

# REMANUFACTURE COST
biaya_remanufacture = lp.LpVariable.dicts("Biaya_Remanufacture", remanufacture_cost, 0, None, lp.LpContinuous)

# DISCOUNT COST
biaya_diskon = lp.LpVariable.dicts("Biaya_Diskon", discount_cost, 0, None, lp.LpContinuous)

# BUILD FACILITY COST M
biaya_pembangunan_fasilitas_m = lp.LpVariable.dicts("Biaya_Pembangunan_Fasilitas_M", facility_cost_m, 0, None, lp.LpContinuous)

# DISPOSAL COST
biaya_pembuangan = lp.LpVariable.dicts("Biaya_Pembuangan", disposal_cost, 0, None, lp.LpContinuous)

#OBJECTIVE FUNCTION TOTAL COST
problem += (
    lp.lpSum(biaya_produksi[i] for i in biaya_produksi) +
    lp.lpSum(biaya_pengiriman_ij[i] for i in biaya_pengiriman_ij) +
    lp.lpSum(biaya_penanganan[i] for i in biaya_penanganan)+
    lp.lpSum(biaya_pengiriman_jk[i] for i in biaya_pengiriman_jk)+
    lp.lpSum(biaya_pembangunan_fasilitas_l[i] for i in biaya_pembangunan_fasilitas_l)+
    lp.lpSum(biaya_pemilahan[i] for i in biaya_pemilahan)+
    lp.lpSum(biaya_pengiriman_li[i] for i in biaya_pengiriman_li)+
    lp.lpSum(biaya_pengiriman_lm[i] for i in biaya_pengiriman_lm)+
    lp.lpSum(biaya_remanufacture[i] for i in biaya_remanufacture) +
    lp.lpSum(biaya_diskon[i] for i in biaya_diskon) +
    lp.lpSum(biaya_pembangunan_fasilitas_m[i] for i in biaya_pembangunan_fasilitas_m) +
    lp.lpSum(biaya_pembuangan[i] for i in biaya_pembuangan) 
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
# Jumlah Produk yang Diproduksi Pemanufaktur (Dikirim ke Distributor) >= Demand Produk
problem += [QPij[i] for i in range(4)] >= [Dk[i] for i in range(4)]

# 2. QDjk <= QPij
# Jumlah Produk yang Dikirim ke Distributor <= Jumlah Jumlah Produk yang Diproduksi Pemanufaktur
problem += [QDjk[i] for i in range(4)] <= [QPij[i] for i in range(4)]


# 3. QRli <= (1 - Fd) (Rkl + ... + n)
# Jumlah Produk Penampungan ke Pemanufaktur <= Rumus x Jumlah Produk Konsumen ke Penampungan
problem += [QRli[i] for i in range(4)] <= [(1-Fd[i]) * Rkl[i] for i in range(4)]

# 4. QSlm == Fd (Rkl + ... + n)
# Jumlah Produk Pengumpulan ke Pembuangan == Rumus x Jumlah Produk Konsumen ke Penampungan
problem += [QSlm[i] for i in range(4)] == [Fd[i] * Rkl[i] for i in range(4)]

# 5. Rkl <= yk (QDjk x GLti + ... + n)
# Jumlah Produk Konsumen ke Penampungan <= yk x Jumlah (Produk Dikirim ke Distributor x Biner 0,1 -> nongreen/green)
problem += [Rkl[i] for i in range(4)] <= [QDjk[item] * Yk[item] * GLti[item] for item in range(4)]

# 6. QRli <= M (QPij + ... + n)
# Jumlah Penampungan ke Pemanufaktur <= M (?) x (Jumlah Pemanufaktur ke Distributor)
problem += [QRli[i] for i in range(4)] <= [QPij[i] for i in range(4)]

# 7. QMi atau QPij <= Cppi
# Jumlah Produk yang Diproduksi Pemanufaktur <= Kapasitas Produksi
problem += [QPij[i] for i in range(4)] <= [Cppi[i] for i in range(4)]

# 8. QDjk <= Cpdj
# Jumlah Produk Dikirim Distributor ke Konsumen <= Kapasitas Distributor
problem += [QDjk[i] for i in range(4)] <= [CPdj[i] for i in range(4)]

# 9. Rkl <= ul Cccl
# Jumlah Produk Dari Konsumen ke Distributor <= ul (?) x Kapasitas Pengumpulan
problem += [Rkl[i] for i in range(4)] <= [ul[i] * Cccl[i] for i in range(4)]

# 10. QRli <= Cri
# Jumlah Produk Pengumpulan ke Pemanufaktur <= Kapasitas Remanufaktur
problem += [QRli[i] for i in range(4)] <= [Cri[i] for i in range(4)]

# 11. QSlm <= vm Ccdm
# Jumlah Produk Dibuang <= vm (?) x Kapasitas Pembuangan
problem += [QSlm[i] for i in range(4)] <= [vm[i] * Ccdm[i] for i in range(4)]

# 12. yk = (Pd/Png x δk/δ* be^-φq) --> Sudah Di Rumus Perhitungan Yk

# 13. Cpi = PCi + βi (t GLti + ... + n) --> Sudah Di Perhitungan Biaya Produksi

# 14. Pd <= Pngi 
problem += [Pd[i] for i in range(4)] <= [Pngi[i] for i in range(4)]

# 15. QMi, Qrli, QSlm, Qpij, Qdjk, Rkl Pd, Cpi >= 0 --> Otomatis Dari Perhitungan Dan Variabel

# 16. ul, vm, GLti ∈ {0,1} --> Otomatis Dari Perhitungan Dan Variabel

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
5. Dd (Penawaran Diskon) datanya didapat darimana?
'''