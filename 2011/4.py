items = list(map(int, input().split()))
patients = list(map(int, input().split()))
items_p = [items[i] for i in range(1, 8, 2)]
items_n = [items[i] for i in range(0, 8, 2)]
patients_p = [patients[i] for i in range(1, 8, 2)]
patients_n = [patients[i] for i in range(0, 8, 2)]


def put_blood(item, patient):
    itemo = list(item)
    arc = list(patient)
    patient[0] = patient[0] - item[0]
    left_o = -(patient[0]) if patient[0] < 0 else 0

    patient[1] = patient[1] - item[1]
    if patient[1] > 0:
        patient[1] = patient[1] - left_o
        left_o = -(patient[1]) if patient[1] <= 0 else 0
    left_a = -(patient[1]) if patient[1] <= 0 else 0

    patient[2] = patient[2] - item[2]
    if patient[2] > 0:
        patient[2] = patient[2] - left_o
        left_o = -(patient[2]) if patient[2] <= 0 else 0
    left_b = -(patient[2]) if patient[2] <= 0 else 0

    patient[3] = patient[3] - item[3] - left_a - left_b - left_o
    final = [patient[i] if patient[i] > 0 else 0 for i in range(4)]
    number = [arc[i] - final[i] for i in range(4)]
    print('original i:', itemo)
    print('original p:', arc)
    print('number:', number)
    print('final:', final)
    return sum(number), final


number, lst = put_blood(items_p, patients_p)
for i in range(4):
    patients_n[i] = patients_n[i] + lst[i]

ans, lists = put_blood(items_n, patients_n)
print(lists)
print(ans + number)