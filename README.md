# Python úkoly heading
## Lokální nastavení
Instalace potřebných balíčků:
```
pip install -r requirements.txt
```

## Práce s python heading
**Zpracování data a práce s pythonem** -> Python-testing/Work_with_python/(evaluator.py)
  - Cíl: Máme XLSX soubor, který obsahuje dump MongoDB (tzn v rámci buněk jsou JSON objekty). Je potřeba si tuto strukturu rozložit na jednotlivé elementy. Výsledek očekávám kvantitativní analýzu jednotlivých dílčích hodnot.
    - Pro sloupce I-R z přiloženého souborů spočítat, kolik je jaká hodnota zadána (včetně „prázdné“), + kolikrát je zadaná nějaká hodnota
    - Sloupec „A“ je ID uživatele – zjistit kolik má jaký uživatel zapnuto/vypnuto (sloupec H)
    - Výstup – buď v pythonu prezentovatelnou formou, nebo XLSX tabulka
  - možnost vložení Python-testing/data_python.xlsx i jako argument 
    ```
    python3 path/to/evaluator.py path/to/source/file
    
    ```  
## Automatické testy heading
  **Selenium a Python/Javascript** -> Python-testing/Automatic_testing
  - Cíl:
    - Jednoduchý test pomocí Selenium za pomocí Python/Javascript na libovolné minimálně od  2 krocích – najít element, kliknout
    - načte stránku google.com -> přijme cookies -> v prohlížeči vyhledá Selenium -> získá popisek z Wikipedia -> vypíše ho do terminálu
