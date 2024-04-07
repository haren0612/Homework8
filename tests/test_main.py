from App import MainApp

def test_message():
    app = MainApp()
    assert app.get_greeting() == "Hello from inside a Docker container! Updated message for testing from github actions"