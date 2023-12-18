from kps_factory import KPSPeli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input().strip().lower()
        peli = KPSPeli.luo_peli(vastaus)
        if peli is not None:
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
