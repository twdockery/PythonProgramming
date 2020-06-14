#tyler Dockery for CSC121  6/13/2020  twdockery@waketech.edu
"""
The Democrat and Republican candidates for presidential election have 5 debates.
After each debates a sample of registered voters are polled to see who has won that debate.
Write a Python program to do the followin:

In each of the 5 debates, ask the user to enter the percentage of voters who think the Democrat candidate has won
and the percentage of voters who think the Republican candidate has won.
If the difference is within 3 percent, the debate is statistically tied.
If one candidate beats the other person by more than 3 percent, that candidate is the winner of that debate.
Display the winner of each debate or report a tie.

After all 5 debates, display the number of debates each candidate has won.
Compare these numbers and report which candidate has won more debates, or they have won the same number of debates.

example:
Debate 1 :
What percentage of people think Democrat's candidate has won? 42
What percentage of people think Republican's candidate has won? 45
It is statistically a tie
"""
r_wins = 0
d_wins = 0

for each_debate in range(5):
    print("debate ", each_debate + 1, " :")
    d = int(input("What percentage of people think Democrat's candidate has won? "))
    r = int(input("What percentage of people think Republican's candidate has won? "))
    if r >= d + 4:   # equal to 4 means first party win
        r_wins += 1
        print("Republican's candidate has won this debate")

    elif d >= r + 4:    # equal to 4 means first party win
        d_wins += 1
        print("Democrat's candidate has won this debate")
    else:
        print("It is statistically a tie")

print("")
print("Number of debates Democrat's candidate has won: ",d_wins)
print("Number of debates Republican's candidate has won: ",r_wins)

if r_wins > d_wins:
    print("The Republicans have won the most debates")
elif d_wins > r_wins:
    print("The Democats have won the most debates")
else:
    print("The two candidates have won the same number of debates")

print("")