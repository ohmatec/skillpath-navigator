from app import create_app

app = create_app()

print("✅ Flask App Loaded")

if __name__ == '__main__':
    app.run(debug=True)