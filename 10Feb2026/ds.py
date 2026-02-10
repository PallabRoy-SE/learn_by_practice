developer_profile: dict = {
    "name": "Pallab Roy",
    "experience_years": 4.5,
    "skills": ["Angular", "React", "Python"],
}

developer_profile.get("skills").append("FastAPI")

print(developer_profile.get("name"))

result = developer_profile.get("company")

if not result:
    result = "Looking for remote roles"

print(result)
