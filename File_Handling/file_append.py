import os
file = open("test2.txt",'a')

file.write("\nI am fine thank you!\n")
lines = ['hope you are doing okay\n',"Let me know if there's an issue\n"]
file.writelines(lines)

file.close()