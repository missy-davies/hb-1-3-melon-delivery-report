def print_daily_report(day, the_file):
    """Given a day number and a path to a file generate a report
    
    Generate a report for the number of melons and the total cost delivered for a particular day"""

    log = open(the_file)
    print(f"Day {day}")

    for line in log:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

    log.close()

print_daily_report(1, "um-deliveries-20140519.txt")
print_daily_report(2, "um-deliveries-20140520.txt")
print_daily_report(3, "um-deliveries-20140521.txt")