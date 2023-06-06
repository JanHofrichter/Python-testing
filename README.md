# Python úkoly heading
## Lokální nastavení
Instalace potřebných balíčků:
```
pip install -r requirements.txt
```
Nastavení webdriveru:
  - Chrome
    1. Zkontrolovat verzi prohlížeče: chrome://settings/help    
      - pokud máte verzi: Google Chrome Version 114.0.5735.90 a používáte Linux, nic nenastavujete
    2. Stáhnout driver podle verze prohlížeče a OS: https://sites.google.com/a/chromium.org/chromedriver/downloads
    3. Ze Zip extrahovat chromedriver
    4. Nový chromedriver nahradit za automatic_testing/chromedriver
  - Firefox
    1. Stáhnout nejnovější verzi GeckoDriveru pro OS: https://github.com/mozilla/geckodriver/releases  
    2. Ze Zip extrahovat soubor geckodriver
    3. Geckodriver nahradit za automatic_testing/chromedriver
    4. Nastavit GeckoDriver do automatic_testing/web_scraper.py:
    ```
    PATH = "automatic_testing/geckodriver"
    driver = webdriver.Firefox(PATH)
    ``` 

## Práce s python heading
**Zpracování data a práce s pythonem** -> Python-testing/work_with_python/(evaluator.py)
  - Cíl: Máme XLSX soubor, který obsahuje dump MongoDB (tzn v rámci buněk jsou JSON objekty). Je potřeba si tuto strukturu rozložit na jednotlivé elementy. Výsledek očekávám kvantitativní analýzu jednotlivých dílčích hodnot.
    - Pro sloupce I-R z přiloženého souborů spočítat, kolik je jaká hodnota zadána (včetně „prázdné“), + kolikrát je zadaná nějaká hodnota
    - Sloupec „A“ je ID uživatele – zjistit kolik má jaký uživatel zapnuto/vypnuto (sloupec H)
    - Výstup – buď v pythonu prezentovatelnou formou, nebo XLSX tabulka
  - Možnost vložení work_with_python/data_python.xlsx i jako argument 
    ```
    python3 work_with_python/evaluator.py work_with_python/data_python.xlsx
    ```  
## Automatické testy heading
  **Selenium a Python/Javascript** -> Python-testing/automatic_testing
  - Cíl:
    - Jednoduchý test pomocí Selenium za pomocí Python/Javascript na libovolné minimálně od  2 krocích – najít element, kliknout
    - Načte stránku google.com -> přijme cookies -> v prohlížeči vyhledá Selenium -> získá popisek z Wikipedia -> vypíše ho do terminálu
  - Spuštění programu:
    ```
    python3 automatic_testing/web_scraper.py
    ```  
