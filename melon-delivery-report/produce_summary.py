def report_logger(report):
    the_file = open(report)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()


print("Day 1")
report_logger("um-deliveries-20140519.txt")

print("Day 2")
report_logger("um-deliveries-20140520.txt")

print("Day 3")
report_logger("um-deliveries-20140521.txt")

