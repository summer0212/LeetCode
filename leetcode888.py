class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes) :
        sum_of_alice = sum(aliceSizes)
        sum_of_bob = sum(bobSizes)

        total = (sum_of_alice + sum_of_bob) 
        fair_deal = total // 2

        for box_alice_give in aliceSizes:
            remaining_alice = sum_of_alice - box_alice_give

            box_needed_from_bob = fair_deal - remaining_alice

            if box_needed_from_bob in bobSizes:
                return [box_alice_give,box_needed_from_bob]
            
object =  Solution()
print(object.fairCandySwap(aliceSizes = [1,2,5], bobSizes = [2,4]))

'''Logic discussion : 
I assume you are asking about the "Fair Candy Swap" question we were just discussing (where Alice and Bob trade boxes).

Here is the explanation as if we were sitting in a 7th-grade classroom.

1. The Story (The Question)

Imagine two friends, Alice and Bob. They went trick-or-treating on Halloween.

Alice has a bag of candy boxes. Some boxes have 2 candies, some have 5, etc.

Bob also has a bag of candy boxes.

The Problem:
Alice counts all her candies and realizes she has 20 candies total.
Bob counts his and realizes he has 30 candies total.

This isn't fair! Bob has more. They want to be fair so that they both represent the exactly same amount.

The Rule:
They are allowed to make exactly one trade.

Alice picks one box from her bag to give to Bob.

Bob picks one box from his bag to give to Alice.

The Goal:
Find which box Alice gives and which box Bob gives so that after the swap, they have the exact same number of candies.

2. Example Walkthrough

Let's look at the numbers:

Alice's Total: 20

Bob's Total: 30

Step 1: What is "Fair"?
If we put all the candy in a giant pile, there are 
20
+
30
=
50
20+30=50
 candies.
To be fair, each person should get half.

50
/
2
=
25
50/2=25

So, the target is: Alice needs to end up with 25. Bob needs to end up with 25.

Step 2: Who has too much?

Bob has 30, but he should have 25. He has 5 too many.

Alice has 20, but she should have 25. She has 5 too few.

Step 3: The Swap
Since Bob is "richer" by 5 candies, he needs to give Alice a box that is bigger than the one Alice gives him.
Bob needs to lose value, and Alice needs to gain value.

If Alice gives a box of 1 candy.

Bob must give a box of 6 candies.

Check: Bob loses 6, gains 1. Net loss = 5. He goes from 30 down to 25. Perfect!

3. The Simple Solution (Logic)

We don't need complex algebra. We can solve this like a puzzle.

The "Try Everything" Approach:

Imagine Alice holds up one of her boxes. She asks Bob a question.

Scenario:

Alice holds up a box with 2 candies.

She calculates: "Okay, I have 20 total. If I give away this 2, I go down to 18. But I want to reach 25. That means I need to get exactly 7 candies back from Bob."

She shouts to Bob: "Hey Bob! Do you have a box with 7 candies?"

Bob checks his bag:

If Bob says "No": Alice puts the '2' box down and picks up her next box to try again.

If Bob says "Yes": They make the trade! Alice gives 2, Bob gives 7. Done.

4. The Code (The "7th Grade" Version)

This code just does exactly what Alice did in the story above.

Calculate the "Fair Amount" they both need.

Alice picks up each of her boxes one by one.

She calculates what she needs from Bob.

She checks if Bob has it.

code
Python
download
content_copy
expand_less
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # 1. Count the totals
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        # 2. Find the total pile and divide by 2 to find the "Fair Goal"
        total_candies = sum_alice + sum_bob
        fair_goal = total_candies // 2  
        
        # 3. Alice tries each of her boxes
        for box_alice_gives in aliceSizes:
            
            # Alice thinks: "If I give this box away, I will have..."
            remaining_alice = sum_alice - box_alice_gives
            
            # "So, to reach the Fair Goal, I need to get..."
            box_needed_from_bob = fair_goal - remaining_alice
            
            # "Bob, do you have this box?"
            if box_needed_from_bob in bobSizes:
                # Yes! Return [Alice's Box, Bob's Box]
                return [box_alice_gives, box_needed_from_bob]

This logic is much easier to understand than the delta formula, right? It's just figuring out what you are missing to reach the goal!'''