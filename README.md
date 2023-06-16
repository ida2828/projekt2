# projekt2
INSTRUKCJA do korzystania z wtyczki "Wtyczka PyQGIS"

1. Zastosowanie wtyczki

1.1 Obliczanie róznicy wysokości dwóch zaznaczonych punktów

1.2 Obliczenie pola powierzchni między zaznaczonymi punktami

2. Warunki działania wtyczki

-system operacyjny Windows

-zainstalowany na danym urządzeniu Python w wersji 3.9 oraz Spyder, QGIS 3.28.7

-biblioteka NumPy oraz SciPy

-pobranie warstwy z wysokościami oraz współrzędnymi np. z Rejestrów z Geoportalu z usługi EGiB - WFS

3. Praca z programem

Aby użyć wtyczki "Wtyczka PyQGIS" należy dysponować warstwą ze współrzędnymi w układzie 2000 oraz wysokościami. Aby pozyskać taką warste można skorzystać z zasobów EGiB na
stronie https://integracja.gugik.gov.pl/eziudp/ , wybrać typ jednoski (np. powiat) a następnie skopiować link, za pomocą którego utworzymy nowe połączenie metodą WFS w programie QGIS.
Z nowego połączenia WFS przeciągamy warstwę "Osnowa wysokościowa". Kontrolujemy czy na pewno zawiera ona dane, których potrzebuje nasza wtyczka tj. otwieramy tabelę atybutów, 
a następnie szukamy nagłówków tabeli: "x2000", "y2000", "h_plevrf2007nh". 
Przed każdym użyciem wtyczki należy przeładować wtyczkę za pomocą "Plugin Reloader". 

3.1 Aby obliczyć różnicę wysokości należy zaznaczyć na aktywnej warstwie dwa punkty, po czym włączyć wtyczkę, a następnie kliknąć "Policz" pod napisem "Oblicz różnicę wysokosći"
Jeżeli użytkownik zaznaczy 1 punkt albo więcej niż 2 punkty w komunikatach ukaże się ostrzeżenie "WARNING" mówiące o tym ile punktów powinien poprawnie wybrać.
Gdy użytkownik prawidłowo wybierze ilość punktów i naciśnie klawisz policz, wynik działania pojawi się pod klawiszem policz oraz w Komunikatach w zakładce "Różnica wysokości" jako "SUCCESS"
Wartość podawana jest to wartość bezwzględna różnicy dwóch punktów, w metrach.

3.2 Aby obliczyć  pole powierzchni należy zaznaczyć na aktywnej warstwie conajmniej trzy punkty, po czym włączyć wtyczkę, a następnie kliknąć "Policz" 
pod napisem "Oblicz pole powierzchni".
Jeżeli użytkownik zaznaczy mniej niż 3 punkty w komunikatach ukaże się ostrzeżenie "WARNING" mówiące o tym ile punktów powinien poprawnie wybrać.
Gdy użytkownik prawidłowo wybierze ilość punktów i naciśnie klawisz policz, wynik działania pojawi się pod klawiszem policz oraz w Komunikatach w zakładce "Pole powierzchni" jako "SUCCESS"
Wartość podawana jest w hektarach w układzie 2000.
