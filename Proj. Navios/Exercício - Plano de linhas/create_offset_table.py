import csv


def build_ship_offsets_csv():
    table_data = {}

    # Open and read the raw data from cotas.txt
    with open("cotas.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:
                x_str, y_str, z_str = row[0], row[1], row[2]

                # Check if the column value is a whole number between 0 and 17
                # This guarantees exactly 18 data columns and filters out anomalies
                if z_str.isdigit() and 0 <= int(z_str) <= 17:
                    z_col = int(z_str)

                    if x_str not in table_data:
                        table_data[x_str] = {}

                    table_data[x_str][z_col] = y_str

    # Sort the row keys (X offsets) numerically rather than alphabetically
    sorted_x_keys = sorted(table_data.keys(), key=float)

    # Generate the exactly 18 column headers (0 to 17)
    columns = list(range(18))

    # Create and write to the output CSV file
    with open("ship_offsets_table.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        # Write the header row
        writer.writerow(["X_Offset"] + columns)

        # Write the structured data row by row
        for x in sorted_x_keys:
            output_row = [x]
            for col in columns:
                # Add the corresponding Y value, or an empty string if there's no data
                output_row.append(table_data[x].get(col, ""))
            writer.writerow(output_row)

    print(
        "Successfully generated 'ship_offsets_table.csv' with ~20 rows and 18 columns."
    )


if __name__ == "__main__":
    build_ship_offsets_csv()
