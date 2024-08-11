f=open('myfiles3.txt','w')
lines=['line 1\n','line2\n','line3\n']
f.writelines(lines)
f.close()


# for efficiency use this instead of writelines()

# f=open('myfiles3.txt','w')
# lines=['line1','line2','line3']
# for line in lines:
#     f.write(line+"\n")
# f.close()