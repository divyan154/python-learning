# args and kwargs

def student_info(*args,**kwargs):
    print(f"Args is {args}")
    print(f"Kwargs is {kwargs}")

student_info("Divyansh","32","male",weight=72,id=98,branch="mechanical")    
