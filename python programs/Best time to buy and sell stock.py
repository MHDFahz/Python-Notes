price=[0,7,2,4,5,3,0,6,8,9,1,6,0]
print(price)
if not price:
    print("0")
else:
    ans=0
    mini=price[0]
    for i in range(1,len(price)):
        if price[i]==0:
            pass
        elif mini==0:
            mini=price[i]
        elif price[i]<mini:
            mini=price[i]
        else:
            ans=max(ans,price[i]-mini)
    print(ans)