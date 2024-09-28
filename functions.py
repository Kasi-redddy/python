def calculate_total(exp):
    total=0
    for i in exp:
        total=total+i
    return total
kasi_exp=[123,456,234,564]
joe_exp=[675,324,65,87]

kasis_total=calculate_total(kasi_exp)
joes_total=calculate_total(joe_exp)


print("kasi's total exp:",kasis_total)
print("joes total exp:",joes_total)   