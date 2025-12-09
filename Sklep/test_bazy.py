# -*- coding: utf-8 -*-
# Test tworzenia bazy danych z rozszerzonymi danymi

# Importowanie biblioteki sys do konfiguracji kodowania konsoli
import sys
# Importowanie biblioteki io do rekonfiguracji strumieni wyjściowych
import io

# Konfiguracja kodowania UTF-8 dla konsoli Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Import klasy głównej
from system_automatyzacji_sqlserver import ReportAutomationSystem

# Komunikat startowy
print("=" * 60)
print("TEST INICJALIZACJI BAZY DANYCH Z ROZSZERZONYMI DANYMI")
print("=" * 60)
print()

# Tworzenie instancji systemu (uruchomi initialize_database)
print("Tworzenie instancji systemu...")
system = ReportAutomationSystem()

print()
print("=" * 60)
print("INICJALIZACJA ZAKOŃCZONA")
print("=" * 60)
print()

# Zamknięcie (bez GUI)
print("Test zakończony pomyślnie!")
