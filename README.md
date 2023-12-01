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

## Übungen

- [Übung 1](https://classroom.github.com/a/qO6T_1gF)
- [Übung 2](https://classroom.github.com/a/AWq59C0c)
- [Übung 3](https://classroom.github.com/a/2ulNqvSd)
- [Übung 4](https://classroom.github.com/a/3Irdd_CR)
- [Übung 5](https://classroom.github.com/a/XUQGUgHV)

## Prüfungen

- [Prüfung 1](https://classroom.github.com/a/cneGWKdD)
- [Nachprüfung 1](https://classroom.github.com/a/LR60u2IA)

## Lernziele

- [Lernziele zur Programmierprüfung I](Lernziele_Programmieren_I.pdf)

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
