from kps_pelaa import KiviPaperiSaksetPeli

class KPSPelaajaVsPelaaja(KiviPaperiSaksetPeli):
    def __init__(self, tuomari) -> None:
        super().__init__(tuomari)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto