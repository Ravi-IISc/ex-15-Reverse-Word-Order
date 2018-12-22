def reversing():

    user = input("Enter a word or sentence who you wannna reverse ")
    sentence = user.split(" ")
    sentence.reverse()
    rev = " ".join(sentence)
    print(rev)

reversing()

# or we can make it different

def rever():
    user = input("Enter a word or sentence who you wanna reverse ")
    sentence = user.split(" ")
    reve = sentence[::-1]
    reve2 = " ".join(reve)
    print(reve2)

rever()



