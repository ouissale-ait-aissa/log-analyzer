from colorama import init, Fore
init(autoreset=True)

stats = {"ERROR": 0, "WARNING": 0, "INFO": 0}

with open("log.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            stats["ERROR"] += 1
        elif "WARNING" in line:
            stats["WARNING"] += 1
        elif "INFO" in line:
            stats["INFO"] += 1

with open("rapport.txt", "w") as report:
    report.write(f"ERROR: {stats['ERROR']}\n")
    report.write(f"WARNING: {stats['WARNING']}\n")
    report.write(f"INFO: {stats['INFO']}\n")

print(f"{Fore.RED}ERROR: {stats['ERROR']}")
print(f"{Fore.YELLOW}WARNING: {stats['WARNING']}")
print(f"{Fore.GREEN}INFO: {stats['INFO']}")

import sys

error_count = 0
with open('log.txt', 'r') as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1

if error_count > 5:
    print(f"Erreur critique : {error_count} erreurs détectées. Build échoue.")
    sys.exit(1)  # Jenkins détectera l’échec
else:
    print(f"Nombre d’erreurs OK : {error_count}")
    sys.exit(0)  # Build réussi

