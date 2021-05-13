
import random
import pyautogui
st=input("enter ur name:")
pas=pyautogui.password("enter ur password:")
gs=""
cl=list("0123456789")
while True:
    gs=list(st)+random.sample(cl,3)
    print("<=========>"+str(gs)+"<========>")
    if gs==list(pas):
        print("your password:"+"".join(gs))
        break

