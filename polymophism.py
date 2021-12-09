import time

class Kucing:
    def __init__(self, nama, nama_hewan, ekor):
        super()
        self.nama = nama
        self.nama_hewan = nama_hewan
        self.ekor = ekor
        nama = str(input("Masukkan nama pemilik : "))
        nama_hewan = str(input("Nama kucing : "))
        ekor = int(input("Masukkan banyak ekor : "))
        if ekor >= 5:
            print("super waw")
        else:
            print("lumayan")
    
    def suara(self):
        print("Meong...meong...meong")
        
class Toke:
    def __init__(self, nama, nama_hewan, ekor):
        super()
        self.nama = nama
        self.nama_hewan = nama_hewan
        self.ekor = ekor
        nama = str(input("Masukkan nama pemilik : "))
        nama_hewan = str(input("Nama Toke : "))
        ekor = int(input("Masukkan banyak ekor : "))
        if ekor >= 5:
            print("super waw")
        else:
            print("lumayan")
    def suara(self):
        print(6 * " Toke")
        time.sleep(4)