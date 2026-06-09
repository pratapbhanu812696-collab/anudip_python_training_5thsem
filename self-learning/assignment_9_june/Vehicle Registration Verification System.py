# 20 Sample Registration Numbers
vehicles = [
    "MH12AB4589", "DL05XY9988", "KA03PQ1234", "UP16KL5566", "HR26AZ1122",
    "MH14CD7788", "DL01AA0001", "KA51EF9090", "UP32MN4455", "GJ01XX5544",
    "MH-12-AB-111", "DL2CA123", "KA047788", "UP15AB9", "GJ03YY8899",
    "HR10BB4455", "MH20VV2233", "DL03CC4455", "KA02KK8888", "UP80EE1234"
]

invalid_vehicles = []
state_report = {}

print("="*60)
print("         VEHICLE REGISTRATION SYSTEM")
print("="*60)

for plate in vehicles:
    # Basic Formatting clean check length must be 10 for standard format
    if len(plate) == 10:
        state_code = plate[0:2]
        district_code = plate[2:4]
        series = plate[4:6]
        v_num = plate[6:10]
        
        # Strict Rule Validation
        is_valid = (
            state_code.isalpha() and 
            district_code.isdigit() and 
            series.isalpha() and 
            v_num.isdigit()
        )
        
        if is_valid:
            # Count letters and digits
            letters = 4  # 2 state + 2 series
            digits = 6   # 2 district + 4 number
            
            # State-wise data tracker
            state_report[state_code] = state_report.get(state_code, 0) + 1
            
            print(f"Registration: {plate} [VALID]")
            print(f"  State: {state_code}, District Code: {district_code}, Series: {series}, Number: {v_num}")
            print(f"  Letters Count: {letters}, Digits Count: {digits}")
        else:
            invalid_vehicles.append(plate)
    else:
        invalid_vehicles.append(plate)

# Display Invalid Registrations
print("\n" + "="*40)
print("         INVALID REGISTRATIONS")
print("="*40)
for inv in invalid_vehicles:
    print(f"X {inv}")

# Challenge: State-wise report
print("\n" + "="*40)
print("         CHALLENGE STATE REPORT")
print("="*40)
for state, count in state_report.items():
    print(f"{state} -> {count} Vehicles")
print("="*40)
