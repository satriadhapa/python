class Ideal:
    def orang(self, nama, tinggi, berat):
        self.nama = str(input("Masukkan nama Anda : "))
        self.nama = nama
            # fungsi dibawah ini merupakan fungsi yang menambahkan value dari user
            #self.tinggi = int(input("Berapa Tinggi Badan Anda: "))
        self.tinggi = tinggi
            # fungsi dibawah ini merupakan fungsi yang menambahkan value dari user
            #self.berat = int(input("Berapa berat badan Anda: "))
        self.berat = berat
        ideal = tinggi - 110
        
        if berat == ideal:
            print("Berat badan Anda sudah ideal. Pertahankan!!!")    
        elif berat > ideal:
            print("Anda perlu diet")
        elif berat < ideal:
            print("Anda kekurangan berat badan")
        else:
            print("Berat badan Anda tidak diketahui.")     
        print("tinggi badan : ",tinggi)
        print("Berat badan : ",berat)
        print("berat badan ideal : ",ideal)    
