numbers = [7,3,2,1]

target = 9  #[7,2]

new = []

for i in range(len(numbers)):

    for j in range(i+1,len(numbers)):

        if numbers[i] + numbers[j] == target:

            new.append(numbers[i])

            new.append(numbers[j])

print(new)
