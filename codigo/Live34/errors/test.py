print(open('teste_win1252.txt', errors='strict').read())
print(open('teste_win1252.txt', errors='replace').read())
print(open('teste_win1252.txt', errors='ignore').read())
print(open('teste_win1252.txt', errors='surrogateescape').read())
print(open('teste_win1252.txt', errors='backslashreplace').read())