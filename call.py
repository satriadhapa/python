from polymophism import Kucing
from polymophism import Toke

print(25 * "=" + str("Kucing"), 25 * "=")
kucing = Kucing(nama= True, nama_hewan=True, 
                ekor= True)
kucing.suara()
print(25 * "=" + str("Toke"), 25 * "=")
toke = Toke(nama= True, nama_hewan=True, 
            ekor= True)
toke.suara()

