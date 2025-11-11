import sys

if len(sys.argv) != 2:
   system_name=sys.argv[0]
   temp= sys.argv[1]
else :
   system_name=sys.argv[0]
    temp = "25"
print(f"temperature: {temp}")
if temp < "15":
    print("Cold")
elif temp>=15 and temp<=30:
    print("Normal")
else:
    print("Hot")

