{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Test12 case 3 failed:-)\n"
     ]
    }
    ],
   "source": [
    "# %load ../src/assert_ex1.py\n",
    "# Use assert to test the add function\n",
    "def add(a, b):\n",
    "    return a -b \n",
    "\n",
    "# Create a test case for the add function and use assert to test it for normal cases\n",
    "def test_add_pos():\n",
    "    assert add(1, 2) == -1, \"Test case 1 failed\"\n",
    "    assert add(-1, 1) == -2, \"Test case 2 failed\"\n",
    "    assert add(-1, -1) == -2, \"Test12 case 3 failed:-)\"\n",
    "\n",
    "try:    \n",
    "    test_add_pos()\n",
    "except AssertionError as e:\n",
    "    print(e)"
   ]
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
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
