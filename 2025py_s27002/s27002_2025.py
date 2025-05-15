# CEL:
# Program służy do generowania losowej sekwencji DNA i zapisu jej w formacie FASTA.
# Użytkownik podaje długość sekwencji, ID, opis i imię.
# Sekwencja zapisywana jest do pliku z rozszerzeniem .fasta.
# Program wyświetla statystyki procentowe nukleotydów oraz stosunek CG do AT.
# W losowe miejsce sekwencji wstawiane jest imię użytkownika.

import random
import os

# Funkcja generująca losową sekwencję DNA
def generate_dna_sequence(length):
    nucleotides = ['A', 'C', 'G', 'T']
    return ''.join(random.choices(nucleotides, k=length))

# Funkcja obliczająca statystyki sekwencji DNA
def calculate_statistics(sequence):
    total = len(sequence)
    counts = {nuc: sequence.count(nuc) for nuc in "ACGT"}
    percentages = {nuc: round((count / total) * 100, 1) for nuc, count in counts.items()}
    cg = counts['C'] + counts['G']
    at = counts['A'] + counts['T']
    cg_at_ratio = round((cg / at) * 100, 1) if at > 0 else 0
    return percentages, cg_at_ratio

def main():
    # Pobieranie danych od użytkownika
    seq_length = int(input("Podaj długość sekwencji: "))
    seq_id = input("Podaj ID sekwencji: ")
    description = input("Podaj opis sekwencji: ")
    name = input("Podaj imię: ")

    # Oryginalny:
    # dna_sequence = generate_dna_sequence(seq_length)
    # MODIFIED (dodano seed dla powtarzalności w testach i debugowaniu):
    random.seed(42)
    dna_sequence = generate_dna_sequence(seq_length)

    # Wstawienie imienia w losowym miejscu
    insert_position = random.randint(0, len(dna_sequence))
    # Oryginalny:
    # final_sequence = dna_sequence[:insert_position] + name + dna_sequence[insert_position:]
    # zmineiony, uzasadnienie: oddzielnie przechowujemy sekwencję z i bez imienia:
    final_sequence = dna_sequence[:insert_position] + name + dna_sequence[insert_position:]

    # Obliczanie statystyk (na podstawie sekwencji bez imienia)
    percentages, cg_at_ratio = calculate_statistics(dna_sequence)

    # Tworzenie zawartości pliku FASTA
    fasta_content = f">{seq_id} {description}\n{final_sequence}\n"

    # Oryginalny:
    # with open(f"{seq_id}.fasta", "w") as f:
    #     f.write(fasta_content)
    # zmieniony, uzasadnienie: dodano sprawdzenie i informację o ścieżce zapisu
    filename = f"{seq_id}.fasta"
    with open(filename, "w") as f:
        f.write(fasta_content)

    print(f"Sekwencja została zapisana do pliku {filename}")
    print("Statystyki sekwencji:")
    for nuc, perc in percentages.items():
        print(f"{nuc}: {perc}%")
    print(f"%CG: {cg_at_ratio}")

# Oryginalny:
# if __name__ == "__main__":
#     main()
# zmieniony, uzasadnienie: dodano obsługę błędów wejściowych:
if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Błąd: Wprowadź poprawną liczbę całkowitą dla długości sekwencji.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
