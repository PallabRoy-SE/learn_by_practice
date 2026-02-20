import requests
import json

BASE_URL = "https://api.github.com/users"


def fetch_git_profile(user_name: str):
    url = f"{BASE_URL}/{user_name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            file_data = {
                "name": data.get("name"),
                "public_repos": data.get("public_repos"),
                "followers": data.get("followers"),
            }
            with open("github_stats.json", "w") as file:
                json.dump(file_data, file, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except IOError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    user_name = input("Enter your GitHub username: ")
    fetch_git_profile(user_name)
