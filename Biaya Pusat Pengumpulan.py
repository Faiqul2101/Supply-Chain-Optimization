#Stakeholder
I = 1 # Pemanufaktur
J = 2 # Distributor
K = 4 # Konsumen
M = 2 # Pengumpulan
N = 2 # Pembuangan

''' 
# Biaya Pendirian Fasilitas Pengumpulan
    fcl = Biaya tetap untuk mendirikan pusat pengumpulan (l) ($)
    ul = variabel biner bernilai 1 jika pusat pengumpulan (l) didirikan dan bernilai 0 jika sebaliknya. 

# Biaya Pemilahan
    Ccl   = Biaya Pemilahan per Produk (l) ($/unit)
    Jumlah Produk Yang Dikembalikan == gatau dapet darimana

# Biaya Pengiriman ke Pemanufaktur
    Cdv =  Biaya transportasi untuk pengiriman satu unit produk atau produk bekas pakai atau komponen dari produk bekas pakai dengan menggunakan 
            kendaraan (v) ($/unit)Cdv	Biaya transportasi untuk pengiriman satu unit produk atau produk bekas pakai atau komponen dari produk bekas 
            pakai dengan menggunakan kendaraan (v) ($/unit)
    dli = Jarak dari Penampungan ke Pemanufaktur
    Cri  = Kapasitas remanufaktur (unit) == jumlah yg dikirim ke remanufaktur (?)

# Biaya Pengiriman ke Pembuangan
    Cdv =  Biaya transportasi untuk pengiriman satu unit produk atau produk bekas pakai atau komponen dari produk bekas pakai dengan menggunakan 
            kendaraan (v) ($/unit)Cdv	Biaya transportasi untuk pengiriman satu unit produk atau produk bekas pakai atau komponen dari produk bekas 
            pakai dengan menggunakan kendaraan (v) ($/unit)
    dlm = Jarak dari Penampungan ke Pembuangan
    Ccdm  = Kapasitas pusat pembuangan (unit) == ini lebih dari cri, jadi kayanya gamungkin disesuaikan dengan kapasitas, sementara angkanya pake random dulu
'''

''' Biaya Pendirian Fasilitas Pengumpulan'''
list_fcl = [20*20000 , 20*25000]

'''Biaya Pemilahan'''
ccl = [13, 17]

'''Biaya Pengiriman ke Pemanufaktur'''
# 1. Biaya per Kendaraan
cost_vehicle_per_distance = {
    "Truck (Hybrid Motor)": [13,14],
    "Truck with Petrol" : [9,10],
    "Trailer (Hybrid Motor)": [6,7],
    "Trailer with Petrol" : [4,5]
}

# 2. Jarak 
distance_m_i = [200, 300, 400, 650]

# 3. Jumlah yang diremanufaktur (asumsi n == Cri)
n_remanufaktur = [88000, 92000]

# Biaya M --> I
cost_delivery_remanufaktur = distance_m_i*n_remanufaktur


