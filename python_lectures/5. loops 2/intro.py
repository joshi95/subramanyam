"""
For loop version 2.

for ch in "ABCDEFGHIJ":
    print(ch)

ch will have values as ("A", "B", ... "J")


demonstration of while lop


break;
break is used inside a loop and it will break 
the nearest loop it is part of.

continue;
continue will skip the code below it and will
jump to the loop beginning.


"""

# for ch in "ASHWIN":
#     print("the character is ", ch)

# cnt = 0
# while cnt < 4:
#     print("hello")
#     cnt += 1


# A program to search for 5 in range(0, 1000)

# for x in range(0, 10):
#     if x == 5:
#         print("Found")
#         break


# for x in range(0, 10):
#     if x < 5:
#         print("will continue")
#         continue
#     print(x)


# for x in range(0, 4):
#     if x < 2:
#         continue
#     if x == 4:
#         break
#     print(x)




# cnt = 0
# while cnt < 10:
#       if cnt < 5:
#          cnt += 1
#          continue
#       if cnt == 7:
#          break 
#       print(cnt)
#       cnt += 1


# for i in range(10):
#    cnt = 0
#    while cnt < 10:
#       print(cnt)
#       cnt += 1
#    break



# cnt1 = 0
# while cnt1 < 5:
#     cnt2 = 0
#     while cnt2 < 5:
#          if cnt2 == 3:
#             break
#          if cnt2 == 0 or cnt2 == 1:
#             cnt2 += 1
#             continue
#          print(cnt2)
#          cnt2 += 1
#     cnt1 += 1

#leetcode

n = 3
no = 1
sum = 0
while no <= n:
   sum += no ** 3
   no += 1

print(sum)




i = 0
while i < n:
    while i < n / 2:
        i += 1
    i += 1