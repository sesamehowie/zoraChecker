def read_txt(filename: str) -> list:
    with open(filename, "r") as f:
        try:
            data = f.read().splitlines()
        except PermissionError:
            print(f"Cant read from file {filename} - lack of permission")
            data = []

        return data
