# Dependency injection

def greet(name: str, print_fn = print):
    greeting_message: str = f"Hi, {name}!"
    print_fn(greeting_message)
    
def greet2(name: str):
    print(f"Hi, {name}!")