class MainApp:
   def __init__(self) -> None:
       pass
   
   def get_greeting(self) -> str:
       return "Hello from inside a Docker container! Updated message for testing from github actions"

   def start(self) -> None:
        print("Hello from inside a Docker container!")
