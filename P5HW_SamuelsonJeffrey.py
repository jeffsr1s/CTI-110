#Jeffrey Samuelson
#5/1/2025
#P5HW
#Make a game

'''
    character info in a dictionary
    Menu driven main
    create character
    display character
    game logic
    end game
'''
import random

#function for creation
def create_racecar():
    color = input("Enter a color to represent a racecar: ")
    number = int(input(f"Enter {color} racer's number: "))

    while True:  # Loop until a valid speed is entered
        speed = int(input(f"Enter {color} racer number {number}'s top speed: "))
        if speed > 210:
            print(f"🚨 {color} racecar will crash due to excessive speed! Try again.")
        else:
            break  # Exit loop once a valid speed is entered

    racecar = {'color': color, 'number': number, 'speed': speed}
    print(f"{color} racecar has been created!")
    return racecar

#function for display
def display_racecars(racecars):
    print("\n------ALL RACECARS------")
    for racecar in racecars:
        print(f"Color: {racecar['color']}, Number: {racecar['number']}, Top Speed: {racecar['speed']}")

#function for game loop
def race(racecars, num_laps):
    print("\n------RACE STARTING------")

    total_distances = {racecar["color"]: 0 for racecar in racecars}  # Track total distance

    for lap in range(1, num_laps + 1):
        print(f"\n🏁 LAP {lap} 🏁")
        
        for racecar in racecars:
            roll = random.randint(1, 6)  # Simulates a dice roll
            distance = roll * racecar["speed"]  # Higher speed multiplies dice value
            total_distances[racecar["color"]] += distance  # Add lap distance
            
            print(f"{racecar['color']} (#{racecar['number']}) rolls {roll} → Lap Distance: {distance} → Total: {total_distances[racecar['color']]}")

    # Determine the winner based on total distance after all laps
    winner = max(total_distances, key=total_distances.get)
    print(f"\n🏆 The winner is {winner} with {total_distances[winner]} total distance!")

#main function
def main():
    racecars = []
    
    while True:
        print("\n=== RACE GAME MENU ===")
        print("1. Create a racecar")
        print("2. Display racecars")
        print("3. Start a race")
        print("4. End game")
        
        choice = input("Choose an option: ")

        if choice == "1":
            racecars.append(create_racecar())
        elif choice == "2":
            display_racecars(racecars)
        elif choice == "3":
            if len(racecars) < 2:
                print("Need at least 2 cars to race!")
            else:
                num_laps = int(input("Enter the number of laps for this race: "))  # Ask for laps
                race(racecars, num_laps)
        elif choice == "4":
            print("Game Over. Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")

#call the main
if __name__ == "__main__":
    main()

'''
    Tried this a number of ways without while true and couldn't make it work as intended. a normal for loop
    would have worked but then I would have determined the laps instead of getting a lap number.
    I also needed the main to run until end game was chosen. So even after a race you can race again, add a car
    and race again or end. I worked on this for many hours trying different game types before I landed here
    just trying to satisfy the conditions created.
'''
