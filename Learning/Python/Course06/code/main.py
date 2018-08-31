test1 = "Life is too short, %s %s %s"
result1 = test1 % "You need python."
result1 = test1 % ("You", "need", "python.")
print(result1)
test2 = "Life is too short, %s"
result2 = test2 % "10"
print(result2)
test3 = "Life is too short, %.2f"
result3 = test3 % 100.1234
print(result3)
test4 = "Life is too short, {} {} {}"
result4 = test4.format("You", "need", 10)
print(result4)
test5 = "\"Life is too short\",\n\'You need python.\'"
print(test5)