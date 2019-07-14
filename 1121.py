class Node:
    def __init__(self, pasien=None):
        self.pasien = pasien
        self.nextpasien = None

class LinkedList:
    def __init__(self):
        self.pasien1 = None

    def printpasien(self):
        data = self.pasien1
        while data is not None:
            print (data.pasien)
            data = data.nextpasien
            
    def antrian(self, new_pasien):
        pasien_baru = Node(new_pasien)
        pasien_akhir = self.pasien1
        while pasien_akhir.nextpasien is not None:
            pasien_akhir= pasien_akhir.nextpasien
            
        pasien_akhir.next_pasien = pasien_baru
            
    def selesaiperiksa(self):
        Node = self.pasien1
        self.pasien1 = Node.nextpasien
        del Node

antri=LinkedList()
antri.pasien1 = Node("1.Imam")
n2 =Node("2.Fikri")
n3 =Node("3.Adi")
n4 =Node("4.Saroji")
n5 =Node("5.Jordan")

antri.antrian (10)

antri.pasien1.nextpasien = n2
n2.nextpasien = n3
n3.nextpasien = n4
n4.nextpasien = n5

print("    Daftar Pasien")

antri.printpasien()
print("  ")
print("    Pasien Selanjutnya")
antri.selesaiperiksa()
antri.printpasien()


