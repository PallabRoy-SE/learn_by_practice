def calculate_experience(start_year: int, current_year: int = 2026) -> str:
    return f"You have {current_year - start_year} years of experience."


print(calculate_experience(2022))
