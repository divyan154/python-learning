# global vs nonlocal scope variable access

greeting = "Hello"

def japanese_greet():
    greeting = "こんにちは"
    def hindi_greeting():
        global greeting
        greeting = "namaste"
    hindi_greeting()    
    print(f"greeting in hindi is {greeting}")    

japanese_greet()    
print(f"greeting in hindi is {greeting}")  