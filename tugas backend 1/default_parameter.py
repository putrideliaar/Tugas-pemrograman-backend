# belajar default argumen value

def say_hello(first_name="budi", last_name=""):
    print(f"hello {first_name} - {last_name}")

say_hello("eko")
say_hello(last_name="kurniawan", first_name="eko")