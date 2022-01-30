import csv
import sys

# Map different rows indexes in ft-70d/ft-3d format
# The rest of the columns match the order
ft70d = {
    "ams": 8,
    "dig_analog": 9,
    "tx_power": 16,
    "tag": 20,
    "skip": 17,
    "auto_step": 18,
    "step": 19,
}

csv_output = []
in_file = sys.argv[1]

def digital_analog_convert(ams, da):
    """Converts mode format"""
    if ams == "ON" and da == "DN":
        return "AMS"
    elif ams == "ON" and da == "ANALOG":
        return "FM"
    elif ams == "OFF":
        if da == "ANALOG":
            return "FM"
        return "DN"
    else:
        return ""


def power_convert(power):
    """Converts power"""
    if power == "HIGH":
        return "High (5W)"
    elif power == "MID":
        return "L3 (2.5W)"
    elif power == "LOW":
        return "L1 (0.3W)"
    else:
        return ""


with open(in_file, newline="") as csv_in:
    data = csv.reader(csv_in, delimiter=",")
    for row in data:
        ams = row[ft70d["ams"]]
        dig_analog = row[ft70d["dig_analog"]]

        row_out = row[0:8]
        row_out.extend([digital_analog_convert(ams, dig_analog)])
        row_out.extend([row[ft70d["tag"]]])
        row_out.extend(row[10:16])

        if row[1]:
            row_out.extend(["RX 00", "TX 00"])
        else:
            row_out.extend(["", ""])

        row_out.extend([power_convert(row[ft70d["tx_power"]])])
        row_out.extend(
            [row[ft70d["skip"]], row[ft70d["auto_step"]], row[ft70d["step"]]]
        )
        row_out.extend(row[21:53])
        csv_output.append(row_out)

with open("ft3d_format.csv", "w", newline="") as csv_out:
    csvwriter = csv.writer(csv_out, delimiter=",")
    csvwriter.writerows(csv_output)