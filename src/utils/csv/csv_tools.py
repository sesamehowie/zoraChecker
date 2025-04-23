import csv


def write_csv(
    file_name: str,
    data: list[list[str] | tuple[str]],
    header: list[str] | tuple[str] = ["address", "points"],
):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(header)
        writer.writerows(data)
