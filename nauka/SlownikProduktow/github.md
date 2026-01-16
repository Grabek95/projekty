text
# Kompletny przewodnik po Git i GitHub – od podstaw

## Spis treści
- [Tworzenie repozytorium na GitHub](#tworzenie-repozytorium-na-github)
- [Podstawowy workflow: add, commit, push](#podstawowy-workflow)
- [Rozwiązywanie typowych błędów](#rozwiązywanie-błędów)
- [VS Code – Git w GUI](#vs-code-git)
- [Zaawansowane: konflikty i rebase](#zaawansowane)
- [Organizacja projektów](#organizacja)

## Tworzenie repozytorium na GitHub

1. Zaloguj się na GitHub.
2. Kliknij zielony przycisk **+** → **New repository**.
3. Nadaj nazwę (np. `projekty`), opis, wybierz **Public/Private**.
4. Zaznacz **Add a README file** (opcjonalnie).
5. Kliknij **Create repository**.

**Połączenie z lokalnym folderem:**
git clone https://github.com/Grabek95/projekty.git
cd projekty

text

## Podstawowy workflow

### W terminalu
git status # co się zmieniło
git add . # dodaj zmiany do stagingu
git commit -m "Opis zmian" # utwórz commit
git push # wyślij na GitHub

text

### W VS Code (Source Control)
1. **Stage Changes** (+ przy „Changes”).
2. Wpisz opis commita.
3. **Commit** (✓).
4. **Push/Sync** (strzałki na dole).

## Rozwiązywanie typowych błędów

### "Can't push refs remote – fetch first"
git pull --rebase origin main # dociągnij i połącz zmiany
git push

text

### "fatal: couldn't find remote ref main/master"
Sprawdź nazwę gałęzi:
git branch # lokalna gałąź
git remote -v # zdalne repo

text
Potem użyj właściwej nazwy: `git pull --rebase origin main` lub `master`.

### "Author identity unknown"
git config --global user.name "Twoje Imię"
git config --global user.email "twoj@email.com"

text

### Problem z plikiem `nul` (Windows)
git rm --cached "Sklep/nul" # usuń z indeksu
echo Sklep/nul >> .gitignore # zignoruj na zawsze

text

## VS Code – Git w GUI

1. Otwórz folder projektu.
2. Panel **Source Control** (ikona gałązki).
3. **Stage** → wiadomość → **Commit** → **Push**.
4. Przy pierwszym push: potwierdź repo `origin`.

## Zaawansowane: konflikty i rebase

Jeśli `git pull --rebase` pokaże konflikty:
1. Git wskaże pliki w konflikcie.
2. Edytuj pliki, usuń markery `<<<<<<<`, `=======`, `>>>>>>>`.
3. `git add .`
4. `git rebase --continue`
5. `git push`

## Organizacja projektów

C:\projekty
├── nauka/
│ ├── lista_zakupow.py
│ └── README.md
├── Sklep/
│ ├── main.py
│ └── config.ini
└── .gitignore

text

**Schemat pracy prywatna/ służbowa:**
- Prywatny PC: pełne repo + GitHub + push.
- Służbowy: tylko pliki tymczasowo (zip/mail → prywatny PC).

## Przydatne komendy

git log --oneline -5 # ostatnie 5 commitów
git status # stan repo
git branch # gałęzie
git remote -v # zdalne repo
git push -u origin main # pierwszy push z trackingiem

text

---

**Autor:** Asystent AI (Perplexity/Claude)  
**Data:** Styczeń 2026  
**Uwagi:** Dokument zawiera wszystkie kluczowe kroki z rozmowy. Screenshots nie zostały wklejone, ale linki do komend są uniwersalne.