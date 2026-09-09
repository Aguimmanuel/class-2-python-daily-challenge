""" TOLL GATE SHIFT CLOSER. 
A toll gate on the Port Harcourt-Aba expressway uses this program for the cashier's desk"""

fee, count, official_count = 0, 0, 0
while True:
    vehicle_type = input("Vehicle (car / bus / official / close): ")
    if vehicle_type == "car":
        fee+= 500
        count+= 1
    elif vehicle_type == "bus":
        fee+= 1000
        count+= 1
    elif vehicle_type == "official":
        print("Official vehicle passed free")
        count+= 1
        official_count+=1
    elif vehicle_type == "close":
        break

print(f"VEHICLES PASSED: {count}")
print(f"OFFICIAL VEHICLES: {official_count}")
print(f"REVENUE: N{fee:.2f}")
