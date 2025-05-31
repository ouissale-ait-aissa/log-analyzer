def analyze_log(input_file, output_file):
    stats = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    with open(input_file, 'r') as file:
        for line in file:
            if "ERROR" in line:
                stats["ERROR"] += 1
            elif "WARNING" in line:
                stats["WARNING"] += 1
            elif "INFO" in line:
                stats["INFO"] += 1

    with open(output_file, 'w') as report:
        for level, count in stats.items():
            report.write(f"{level}: {count}\n")

if __name__ == "__main__":
    analyze_log("log.txt", "rapport.txt")
