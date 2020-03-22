import random

HIGHEST_NUMBER = 45
LOWEST_NUMBER = 1

desired_number_of_picks = int(input("How many quick picks? "))
quick_picks = []
for quick_pick in range(desired_number_of_picks):
    # current_pick_line = [random.randint(1, 10) for number in range(6) if number not in ????]
    current_pick_line = []
    random_test = []
    print([random.randint(1, 10) for number in range(6) if number not in random_test])
    current_pick_line = [random.randint(1, 10) for number in range(6) if number not in current_pick_line]
    # i = 0
    # for number in range(6):
    #     random_number = random.randint(1,10)
    #     if random_number not in current_pick_line:
    #         current_pick_line.append(random_number)
    #         break
    # while i < 6:
    #     random_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    #     if random_number not in current_pick_line:
    #         current_pick_line.append(random_number)
    #         i += 1
    print(current_pick_line)