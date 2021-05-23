def fun(*argument,word):
    if word in argument:
        print(word, str("is present in this tuple"))

    else:
        print("this is not present in this tuple")

fun(2,3,4,5,5,7,word=5)
fun(1,42,3,word=5)
fun(23,54,55,7,word=55)
fun(2,33,24,235,5,7,word=52)
