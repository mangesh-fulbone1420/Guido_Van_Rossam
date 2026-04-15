
a=["Maharashtra","Gujarat","Rajasthan","Punjab","Banglore"]
b=["Mumbai","Ahmedabad","Jaipur","Chandigarh","Banglore"]

res={state : capital for state,capital in zip(a,b)}
print("Dictionary Mapping:",res)