PORT: int = 8000
environment: str = "Development"
database_url: str = f"postgres://localhost:{PORT}/db"

print(f"Starting server in {environment} mode on port {PORT}...")
