jumla = input("Jumla kiriting: ")
sozlar = jumla.split()

print(f"\nJumlada {len(sozlar)} ta so'z bor:\n")

for i, soz in enumerate(sozlar, 1):
    print(f"  {i}. '{soz}' — uzunligi: {len(soz)} ta harf")
eng_uzun = max(sozlar, key=len)
print(f"\nEng uzun so'z: '{eng_uzun}' ({len(eng_uzun)} harf)")
