# This is a copy of What-Are-Variables.ipynb
# I am making a copy because not all programs can understand the Satyrn Notebook file
# Comments explain code to designers. Code explains comments to computers.

# This is your standard Hello World Program
# print("...") allows you to outpu to the program
print("Hello World!")

# variables can be different items
a = 1
b = 2

# variables can be strings of text

"c = "help! I am trappend in a variable!\")
"# variables can contain decimals if floated, or including a decimal point\n",
    "d = float(13.125)\n",
"e = 13.\n",
    "# variables can equal other variables, and different variables can have different values\n",
    "f = e\n",
    "# variables can contain math equations\n",
    "g = 10 * 2\n",
    "h = 10 / 2\n",
    "i = 10 + 2\n",
    "j = 10 - 2\n",
    "k = 1.5e4\n",
    "print(k)\n",
    "# variable can also calculate remainders\n",
    "remainder = 17 % 3\n",
    "print(remainder)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10010\n",
      "110\n"
     ]
    }
   ],
   "source": [
# variables can change forms\n",
    "a1 = (\"100\")\n",
    "b1 = (\"10\")\n",
    "# this variable will slam the strings together\n",
    "c = a1 + b1\n",
    "# this will create a number\n",
    "d = int(a1) + int(b1)\n",
    "print(c)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "today I ran 10 miles in 10 minutes!\n"
     ]
    }
   ],
   "source": [
    "# by themselves, variables are split into types, but they can be combined with printing if converted to strings\n",
    "a = \"10\"\n",
    "b = 10\n",
    "print(\"today I ran \" + a + \" miles in \" + str(b) + \" minutes!\")"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "# Variables are stored at the time they are created or updated, not at the end.\n",
    "a = 10\n",
    "b = a\n",
    "a = 5\n",
    "print(a)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Today's entree is a burrito the size of your head!\n",
      "It will cost: $16.47 with tax.\n",
      "$18.94 with a 15% tip. $18 would be nicer\n",
      "$19.76 with a 20% tip. $19 would be nicer\n"
     ]
    }
   ],
   "source": [
    "# here is an exercise for creating tips\n",
    "# Tax will be set to 8%\n",
    "# I will calculate a 15% and 20% tip\n",
    "entree = 15.25\n",
    "mealCost = entree * 1.08\n",
    "tax15 = mealCost * 1.15\n",
    "tax20 = mealCost * 1.2\n",
    "print(\"Today's entree is a burrito the size of your head!\")\n",
    "# I wanted to round the float, and had to look online. So, I skipped ahead and found out how to do this\n",
    "print(\"It will cost: $\" + str(round(mealCost,2)) + \" with tax.\")\n",
    "print(\"$\" + str(round(tax15,2)) +\" with a 15% tip. $\" + str(int(tax15)) + \" would be nicer\")\n",
    "print(\"$\" + str(round(tax20,2)) +\" with a 20% tip. $\" + str(int(tax20)) + \" would be nicer\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
