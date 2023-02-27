# FITNES-MODULIN TESTIT
#======================

# KIRJASTOJEN JA MODULIEN LATAUKSET
import fitnes

def test_laske_bmi():
    assert fitnes.laske_bmi(64.7, 170) == 22.4
    assert fitnes.laske_bmi(40, 170) == 13.8
    assert fitnes.laske_bmi(100, 170) == 34.6

def test_aikuisen_rasvaprosentti():
    # Testejä aikuisia miehiä
    assert fitnes.aikuisen_rasvaprosentti(22.4, 20, 1) == 15.3
    assert fitnes.aikuisen_rasvaprosentti(13.8, 40, 1) == 9.6
    assert fitnes.aikuisen_rasvaprosentti(34.6, 70, 1) == 41.4

    # Aikuisia naisia
    assert fitnes.aikuisen_rasvaprosentti(20.8, 20, 0) == 24.2
    assert fitnes.aikuisen_rasvaprosentti(13.8, 40, 0) == 20.4
    assert fitnes.aikuisen_rasvaprosentti(34.6, 60, 0) == 49.9

def test_naisen_usa_rasvaprosentti():
    assert round(fitnes.usarasvaprosentti_nainen(170, 70, 90, 37)) == 18
    assert round(fitnes.usarasvaprosentti_nainen(170, 90, 90, 42)) == 26

def test_miehen_usa_rasvaprosentti():
    assert round(fitnes.usarasvaprosenttimies(171, 91, 38)) == 22
    assert round(fitnes.usarasvaprosenttimies(170, 120, 42)) == 37
    






