# You have:
# Initial power power
# Array monsters[] (each monster has some power)
# Rule:
# You can defeat a monster only if your current power ≥ monster power
# After defeating it, your power increases by monster power
# Question:
# Can you defeat all monsters?

# 🔹 Greedy Idea
# Fight weakest monsters first
# Sorting ensures you gain power gradually
# If you can’t defeat the weakest → you can’t defeat any stronger one

def can_defeat_all(monsters, power):
    # Sort monsters by power (weakest first)
    monsters.sort()

    for m in monsters:
        if power < m:
            return False   # Cannot defeat this monster
        power += m         # Gain power after defeating

    return True

# Time Complexity: O(n log n) (due to sorting)
# Space Complexity: O(1)

# A little upgraded version of this question

# A hero has initial experience E. 
# There are N monsters with Power[i] and Bonus[i]. You can only defeat a monster if E >= Power[i]. 
# When you defeat it, E = E + Bonus[i]. Find the max number of monsters you can defeat.

def maxMonstersDefeated(E, Power, Bonus, N):
    # Step 1: Combine Power and Bonus
    monsters = list(zip(Power, Bonus))
    
    # Step 2: Sort monsters by Power
    monsters.sort(key=lambda x: x[0])

    count = 0

    # Step 3: Try defeating monsters
    for power, bonus in monsters:
        if E >= power:
            E += bonus
            count += 1
        else:
            break

    return count

print(maxMonstersDefeated(10, [5, 15, 10], [5, 10, 5], 3))  # Output: 2
#Time complexity: O(N log N) due to sorting
