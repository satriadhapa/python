class Ideal:
    def orang(self, nama, tinggi, berat):
        self.nama = str(input("Masukkan nama Anda : "))
        self.nama = nama
        self.tinggi = int(input("Berapa Tinggi Badan Anda: "))
        self.tinggi = tinggi
        self.berat = int(input("Berapa berat badan Anda: "))
        self.berat = berat
        ideal = tinggi - 110
        
        if berat == ideal:
            print(ideal)
            print("Berat badan Anda sudah ideal. Pertahankan!!!")
        elif berat > ideal:
            print("Anda perlu diet")
        elif berat < ideal:
            print("Anda kekurangan berat badan")
        else:
            print("Berat badan Anda tidak diketahui.")     