#CS112_A1_T2_2_20230723.py 
#Number scrabble : is played with the list of numbers between 1 and 9. Each player takes
#turns picking a number from the list. Once a number has been picked, it cannot be picked
#again. If a player has picked three numbers that add up to 15, that player wins the game.
#However, if all the numbers are used and no player gets exactly 15, the game is a draw.
# mustafa yasir omar taha
# 20230723

numbers = [1,2,3,4,5,6,7,8,9,]
fst = 0
scd = 0
while 1 > 0:
    print(numbers)
    fisrt = int(input("Player 1 choose a number : "))
    numbers.remove(fisrt)
    fst = fst + fisrt
    if fst == 15:
        print("\nPlayer1 is a winner\n")
        break
    if sum(numbers) == 0:
        print("\ndraw\n")
        break
    print(numbers)
    second = int(input("Player 2 choose a number: "))
    numbers.remove(second)
    scd = scd + second
    if scd == 15 :
        print("\nPlayer2 is a winner\n")
        break
    if sum(numbers) == 0:
        print("\ndraw\n")
        break