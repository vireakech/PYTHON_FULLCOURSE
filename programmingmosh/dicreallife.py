input_ = input("MOOD :")
{
    ":)" : "😊"
    , ":(" : "☹️"
    , ":D" : "😃"
    , ";)" : "😉"
}
word = input_
for word in word.split(" "):
    print(dic.get(word, word), end=" ")
