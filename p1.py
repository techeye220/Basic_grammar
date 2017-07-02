import string
st="00:00:00"
et="00:00:10"
sh=(int)(st[0]+st[1])-(int)(et[0]+et[1])
sm=(int)(st[3]+st[4])-(int)(et[3]+et[4])
ss=(int)(st[6]+st[7])-(int)(et[6]+et[7])
print (sh*3600+sm*60+ss)*(-1)