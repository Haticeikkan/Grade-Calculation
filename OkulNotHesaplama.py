while True:
    vize = input("Vize Notunuzu Giriniz: ")
    try:
        vize = float(vize)
        assert 0 <= vize <= 100
    except:
        print("Lütfen 0-100 Arasında Bir Sayı Giriniz!")
        continue
    break

while True:
    ödev = input("Ödev Notunuzu Giriniz: ")
    try:
        ödev = float(ödev)
        assert 0 <= ödev <= 100

    except:
        print("Lütfen 0-100 Arasında Bir Sayı Giriniz!")
        continue
    break

while True:
    final = input("Final Notunuzu Giriniz: ")
    try:
        final = float(final)
        assert 0 <= final <= 100
    except:
        print("Lütfen 0-100 Arasında Bir Sayı Giriniz!")
        continue
    break

ortalama = float((vize * 0.3) + (ödev * 0.2) + (final * 0.5))

print("Ortalamanız: ", ortalama)

if ortalama >= 90:
    print("Harf Notunuz: AA")
elif ortalama >= 85:
    print("Harf Notunuz: BA")
elif ortalama >= 80:
    print("Harf Notunuz: BB")
elif ortalama >= 75:
    print("Harf Notunuz: CB")
elif ortalama >= 70:
    print("Harf Notunuz: CC")
elif ortalama >= 60:
    print("Harf Notunuz: DC")
elif ortalama >= 50:
    print("Harf Notunuz: DD")
else:
    print("Harf Notunuz: FF")

# print("Hatice İkkan...")