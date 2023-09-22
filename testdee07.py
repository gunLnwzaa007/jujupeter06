# break

for x in range(5) :
    if x == 3 :
        break # ทำงานเมื่อไหร่ หยุดทำซํ้าทันที
    print("TEE")

print("--------------------------")
print("--------------------------")

# continue
for y in range(5) :
    if y == 3 :
        continue # ทำงานเมื่อไหร่ จบรอบนั้นไปรอบต่อไปทันที
    print(f"LEE {y}")