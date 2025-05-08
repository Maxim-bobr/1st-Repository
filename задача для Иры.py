nums = [13, 28, 34, 10, 31, 23, 39, 27, 35, 30, 41]
print("Изначальный список: ", nums)
for i in range(len(nums)):
  nums[i] -= 9
for i in range(len(nums)):
  if nums[i] % 2 == 0:
    nums[i] *= 3
  else:
    nums[i] += 5
print("Преобразованный список: ", nums)
list2 = ['Е', 'У', 'Ь', 'И', 'К', 'Н', 'Ю', 'Ч', 'М', 'П', 'Т',]
slov = {}
i = 0
while i < 11:
  slov.update({nums[i]: list2[i]})
  i +=1
print("Получаем словарь: ", slov)
print("Ответ: ", slov[24], slov[54], slov[12], slov[42], slov[6], slov[12], " - ", slov[26], slov[24], slov[96],
      slov[30], " ", slov[66], " ", slov[24], slov[78],  slov[12], slov[42], slov[6], slov[90],)

