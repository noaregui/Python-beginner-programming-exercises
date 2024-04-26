def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(1,100):
        if i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0 & i%5==0:
            print("FizzBuzz")
        else:
            print(i)
# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
