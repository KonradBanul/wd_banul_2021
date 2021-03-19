def numer_dnia(a):
    if a == 1:
        return "poniedziałek"
    elif a == 2:
        return "wtorek"
    elif a == 3:
        return "środa"
    elif a == 4:
        return "czwartek"
    elif a == 5:
        return "piątek"
    elif a == 6:
        return "sobota"
    elif a == 7:
        return "niedziela"
    else:
        return "nie ma takiego dnia"
def skrot(dzien):
    if dzien == "poniedziałek":
        return "pon"
    elif dzien == "wtorek":
        return "wt"
    elif dzien == "środa":
        return "śr"
    elif dzien == "czwartek":
        return "czw"
    elif dzien == "piątek":
        return "pt"
    elif dzien == "sobota":
        return "sob"
    elif dzien == "niedziela":
        return "ndz"
    else:
        return "nie ma takiego dnia"

    

    