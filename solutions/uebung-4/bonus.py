#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Schreiben Sie ein Programm, welches eine gegebene Datei in englischer Sprache einliest
und daraus die Wörterbucher letter_frequency und word_frequency erstellt, in welchen 
zu jedem Buchstaben bzw. Wort die Anzahl Vorkommen dieses Buchstabens/Worts in der Datei 
assoziiert wird.

Implementieren Sie danach eine Verschülsselung, in welcher Buchstaben nach einem festen
Schema permutiert werden (z.B. a->e, b->h, c->a, d->z, e->r, ....)
und lassen Sie Ihr Programm aufgrund einer Häufigkeitsanalyse in einem langen Text
die Verschlüsselung knacken

Resourcen:
- https://www.w3schools.com/python/python_file_open.asp
- https://libguides.middlesex.mass.edu/c.php?g=278796&p=1857707  
  (Plain Text UTF-8 herunterladen, Inhaltsverzeichnis entfernen)
- https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
"""

import numpy as np


def letter_and_word_frequency(content, alphabet):
    # Ersetze Satzzeichen durch Leerzeichen
    signs = [",", ".", "!", ";", "(", ")", '"', ":", "-", "?"]
    content_without_signs = content.lower()
    for sign in signs:
        content_without_signs = content_without_signs.replace(sign, " ")

    # Generiere Wörter und Buchstaben (jeweils mit Wiederholungen)
    words = content_without_signs.split()
    letters = [l for word in words for l in word]

    # Generiere Liste der absoluten Häufigkeiten der Buchstaben
    letter_frequency = {a: letters.count(a) for a in alphabet}
    letter_frequency = dict(sorted(letter_frequency.items(), key=lambda x: -x[1]))

    # Generie Liste der absoluten Häufigkeiten der Wörter
    word_list = set(words)
    word_frequency = {word: words.count(word) for word in word_list}
    word_frequency = dict(sorted(word_frequency.items(), key=lambda x: -x[1]))

    return letter_frequency, word_frequency


def permute_letters(content, alphabet, permutation):
    # Permutiere die Buchstaben gemäss der Permutation
    permutation_upper = [letter.upper() for letter in permutation]

    # Im kleingeschriebenen Text, ersetze alle Buchstaben durch die permutierten Grossbuchstaben
    content_permuted = content.lower()
    for i, letter in enumerate(alphabet):
        content_permuted = content_permuted.replace(letter, permutation_upper[i])

    # Buchstaben, die original gross geschrieben waren, sollen gross sein; alle anderen klein
    temp = list(
        content_permuted.lower()
    )  # Listeintrag zu ändern ist einfacher als Zeichenketteneintrag
    for i in range(len(content_permuted)):
        if content[i].isupper():
            temp[i] = content_permuted[i].upper()
    content_permuted = "".join(temp)  # Mache aus der Liste wieder eine Zeichenkette
    return content_permuted


def restore_content(content, text_letters_sorted):
    # Sortierte Buchstabenhäufigkeiten in Projekt Gutenberg
    stats_letters_sorted = "etaoinshrdlcumwfgypbvkjxqz"
    return permute_letters(content, text_letters_sorted, stats_letters_sorted)


if __name__ == "__main__":
    # Aus der folgenden Datei wird der Text gelesen, der nach einer Permutation
    # der Buchstaben entschlüsselt werden soll.
    # Dieser ist durch den Namen einer auf dem eigenen Rechner vorhandenen Datei zu ersetzen
    FILENAME = "sample2.txt"

    file = open(FILENAME, "r")
    content_raw = file.read()

    alphabet = [chr(n) for n in range(97, 97 + 26)]  # Liste [a, b, ... , z]
    permutation = np.random.permutation(alphabet)  # Zufällige Permutation davon

    # Erzeuge Text, in welchem Buchstaben gemäss `permutation` vertauscht sind
    content_permuted = permute_letters(content_raw, alphabet, permutation)
    letter_frequency, word_frequency = letter_and_word_frequency(
        content_permuted, alphabet
    )

    # Versuche Wiederherstellung des originalen Textes mittels Häufigkeitsanalyse
    content_restored = restore_content(content_permuted, letter_frequency.keys())

    print(f"Wiederhergestellter Text: {content_restored}")

    # Der wiederhergestellte Text wird nur ungefähr mit dem originalen Text übereinstimmen,
    # wenn der Text nicht genügend lange ist. Versuche daher durch sukzessives Vertauschen
    # zweier Buchstaben den Text ganz zu entschlüsseln.
    while True:
        inp = input("Buchstaben vertauschen (z.B. 'as' vertauscht 'a' mit 's')? ")
        if len(inp) != 2:
            break
        content_restored = permute_letters(content_restored, inp, inp[1] + inp[0])
        print(f"Verbesserter Text: {content_restored}")
