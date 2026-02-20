try:
    count = 0
    with open("server.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                count += 1
    print(f"Fount {count} errors.")
except FileNotFoundError as e:
    print(f"Error: {e}")
