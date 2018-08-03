# unit_test_list
list_lib.py:
	Egy python library ami jelenleg 4 "üres" függvényt +1 konstanst tartalmaz.
	Ha lefuttatod (le lehet) ki is írja, hogy ő csak egy library és nem is
	csinál úgy amúgy semmit önmagában.
	Ezeket az implementációkat be kell fejezeni, de ne ess neki mert trükkös!
	A függvényeket kb 10 perc megcsinálni és nem ez a feladat lényege!!!

unit_test_list_lib.py:
	Ez egy unit test case class-t implementáló python file.
	Le lehet futtatni amivel is kiértékel 20 unit tesztet.
	Az eredmény többnyire FAIL, mivel a hiányos "list_lib" funkcionalitását
	igyekszik kiértékelni és ügye az majdnem teljesen üres.
	Ezen felül van egy pár "üres" szimplán csak direktbe fail-elő test case
	e.g.: "test_max_list_multiple"

A feladat az lenne, hogy az összes unit test OK eredmény legyen.
Ez egy három részből álló feladat:

1.: Át kéne futni ezt legalább felületesen:
https://docs.python.org/2/library/unittest.html
Az első pár bekezdés elég fontos/hasznos (pl.: Basic example és a 
Command-Line Interface)

2.: Át kéne nézni a list_lib.py-t és unit_test_list_lib.py-t és a meglévő kód
illetve a meglévő tesztek alapján be kéne fejezni a list_lib.py implementálását

3.: Át kéne nézni a list_lib.py-t és unit_test_list_lib.py-t és a meglévő kód
illetve a meglévő tesztek alapján be kéne fejezni a hiányzó unit test-eket



Itt egy command-line parancs amivel talán könnyebb átlátni az eredményt meg a
hibákat is (a mappán belül kell futtatni):
python -m unittest discover . -v -p "unit_test*.py"
