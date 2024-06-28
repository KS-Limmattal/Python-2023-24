<!-- -*- coding: utf-8 -*- -->

# Python-Programmierung 2023-24

## Installation

### Windows

Empfohlen wird die portable Python-Installation [WinPython](https://github.com/winpython/winpython), Version 3.11.4. vom 15. Juli 2023 ([Download-Link](https://github.com/winpython/winpython/releases/download/6.4.20230625final/Winpython64-3.11.4.0.exe)). Diese enthält alle Module (inklusive math, cmath, numpy, pygame), die wir in diesem Semester benötigen werden. WinPython enthält die Python-Programmierumgebung Spyder, mit der wir arbeiten werden.

Für eine leistungsfähige Konsole und Arbeit mit `Git`-Repositories wird [PortableGit](https://github.com/git-for-windows/git) empfohlen, Version 2.42.0 vom 13. Juli 2023 ([Download-Link](https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.1/Git-2.42.0-64-bit.exe)). Für die Arbeit mit Git siehe [Seite zu Git](GIT.md)

PortableGit soll in einen Ordner `PortableGit` im Ordner installiert werden, in welchem bereits WinPython installiert ist (z.B. im Wurzel-Verzeichnis `D:` oder `E:` für ein USB-Stick, oder im Dokumenten-Ordner auf Laufwerk `C:`). Git wird mittels der
Kommandozeile `git-bash` verwendet. Um `git-bash` direkt aus dem Ordner auszuführen, welches `WinPython` und `PortableGit` enthält, wird am besten von `git-bash.exe` mittels Rechtsklick "Verknüpfung erstellen" eine Verknüpfung erstellt. Die Verknpüfung wird nun ins Verzeichnis mit `WinPython` und `PortableGit` verschoben. Ausserdem erstellen wir in diesem Verzeichnis einen Ordner `MyCode`, in welcher der eigene Python Code platziert wird.

Die Ordner-Struktur könnte nun wie folgt aussehen:
![grafik](https://user-images.githubusercontent.com/40485433/131446510-0f393315-001b-4161-b1a6-75ff74f86606.png)

Durch Rechtklick auf die Verknüpfung auf `git-bash.exe` können wir das Verzeichnis, in welchem das Terminal gestartet wird, auf unser eigenes Code-Verzeichnis setzen:
![grafik](https://user-images.githubusercontent.com/40485433/131446801-2b9c42b5-4374-43c9-8c7e-01e20851b617.png)

### MacOS

Python3 und pip3 sind üblicherweise vorinstalliert. Die Programmierumgebung `spyder` erhält man auf [der Spyder Installationsseite](https://docs.spyder-ide.org/current/installation.html)

Ein Terminal gibt es unter MacOS vorintalliert. Um `Git` zu installieren, kann man im Terminal `git` eingeben und wird durch die Installation geführt.

### Linux

Sowohl `python3`, der Paket-Installer `pip3` wie auch die Programmierumgebung `spyder` sowie `git` lassen sich über die Kommandozeile installieren (unter Ubuntu `sudo apt install python3 pip3 spyder git`)

### Online Editoren

Anstatt einer lokalen Python-Installation lassen sich für einfache Zwecke auch ein Online-Editor einsetzen wie z.B.

- [Python Tutor](https://pythontutor.com/)
- [Online Python](https://www.online-python.com/)

## Programmierprojekt

[Projekt](https://classroom.github.com/a/3UwXo-P_)

## Übungen

- [Übung 1](https://classroom.github.com/a/qO6T_1gF)
- [Übung 2](https://classroom.github.com/a/AWq59C0c)
- [Übung 3](https://classroom.github.com/a/2ulNqvSd)
- [Übung 4](https://classroom.github.com/a/3Irdd_CR)
- [Übung 5](https://classroom.github.com/a/XUQGUgHV)
- [Übung 6](https://classroom.github.com/a/THIM3nIV)
- [Übung 7](https://classroom.github.com/a/8Eaas1g6)
- [Übung zur Vererbung](https://classroom.github.com/a/6sZP9s0H)
- [Super Mario Level 1](https://classroom.github.com/a/BkZ_FTv6)

### Online-Ressourcen mit Übungen und Musterlösungen

- [w3resource](https://www.w3resource.com/python-exercises/)
  Diese Seite enthält zum Teil ziemlich gute Aufgaben, von einfach zu mittelschwer.
  Es gibt auch Musterlösungen dazu. Leider sind die Anforderungen in der Aufgabenstellung
  manchmal unklar formuliert oder (vermutlich in Einzelfällen) fehlerhaft und die Lösungen
  sind oftmals etwas umständlich und manchmal etwas verwirrend.
- [pynative](https://pynative.com/python-exercises-with-solutions/)
  Diese Seiten enthält kleine Aufgaben, die mit ca. 3 Zeilen Code gelöst werden können. 
  Bei den Musterlösungen werden zum Teil Alternativen gegeben. 
- [w3schools](https://www.w3schools.com/python/exercise.asp)
  Hier geht es um blosse Syntax-Einübung. Es müssen Lücken in kleinen Programmtexten
  eingefüllt werden.

## Prüfungen

- [Prüfung 1](https://classroom.github.com/a/cneGWKdD)
- [Nachprüfung 1](https://classroom.github.com/a/LR60u2IA)
- [Prüfung 2](https://classroom.github.com/a/y7E-OhqQ)
- [Nachprüfung 2](https://classroom.github.com/a/1pRzc13E)

## Lernziele

- [Lernziele zur Programmierprüfung I](Lernziele_Programmieren_I.pdf)
- [Lernziele zur Programmierprüfung II](Lernziele_Programmieren_II.pdf)

## Themen

### 1. Teil

- Eingabe und Ausgabe
- Textformattierung (f-String Formattierung)
- if-Abfrage
- Schleifen (while, for)

### 2. Teil

- Berechnungen mit Ganzzahlen, Fliesskommazahlen und komplexen Zahlen
- Iterative Verfahren zur Berechnung von Näherungswerten
- Das numpy Modul und Berechnungen mit Vektoren und Matrizen
- Fraktale

### 3. Teil

- Listen
- Wörterbücher

### 4. Teil

- Funktionen

### 5. Teil

- Klassen
- Überladung von Operatoren

## 6. Teil

- Zusammenarbeit in Teams
- Vererbung
- Spiele mit pygame
