{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "368991bc",
   "metadata": {},
   "source": [
    "# QUESTION 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e316a6d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "def circ_area(r):\n",
    "    circ_area = math.pi * r ** 2\n",
    "    return circ_area\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abe2c182",
   "metadata": {},
   "outputs": [],
   "source": [
    "r = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "06913f94",
   "metadata": {},
   "outputs": [],
   "source": [
    "assert circ_area(r) == math.pi * r ** 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14a9b3cc",
   "metadata": {},
   "source": [
    "# QUESTION 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "6ed35ee7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def isAP(x):\n",
    "    if len(x) < 2:\n",
    "        return False\n",
    "    \n",
    "    d = x[1] - x[0]\n",
    "    \n",
    "    for i in range(2, len(x)):\n",
    "        if x[i] - x[i - 1] != d:\n",
    "            return False \n",
    "    \n",
    "    return True  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "72c7cc43",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = [1, 3, 5, 6, 9, 11, 13]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "333233f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "assert isAP(x) == False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0230779c",
   "metadata": {},
   "source": [
    "# Question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "809f08cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_grade(Marks, ClassAttendance, Totallectures):\n",
    "    \n",
    "    Score = 9/10 * Marks + 10 * (ClassAttendance/Totallectures)\n",
    "    grade = \"\"\n",
    "    \n",
    "    if 100 <= Score <= 80:\n",
    "        grade  = \"Distinction\"\n",
    "    elif 80 <= Score <= 50:\n",
    "        grade = \"pass\"\n",
    "    else :\n",
    "        grade = \"Fail\"\n",
    "        \n",
    "        result = {\"Score\":Score ,\"Remark\":grade}\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50a98849",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "0f741699",
   "metadata": {},
   "source": [
    "# QUESTION 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "ce4b8075",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "def polar2rect(r, theta):\n",
    "    \n",
    "    x = r * math.cos(theta)\n",
    "    \n",
    "    y = r * math.sin(theta)\n",
    "    \n",
    "    return (x , y)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b864d631",
   "metadata": {},
   "source": [
    "# QUESTION 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "de4dfbfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "def vect_dist(a, b):\n",
    "    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)\n",
    "    return distance\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23954941",
   "metadata": {},
   "source": [
    "# QUESTION 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "3d72414f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def line_intersect(l1, l2):\n",
    "    m1, c1 = l1\n",
    "    m2, c2 = l2\n",
    "    \n",
    "    if m1 - m2 == 0:\n",
    "        return None  \n",
    "    \n",
    "    x_intersect = (c2 - c1) / (m1 - m2)\n",
    "    y_intersect = m1 * x_intersect + c1\n",
    "    \n",
    "    return (x_intersect, y_intersect)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fe7cc49",
   "metadata": {},
   "source": [
    "# QUESTIONS 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "7c211fb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def list_intersect(A, B):\n",
    "    intersection = [element for element in A if element in B]\n",
    "    return intersection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af7fe4f6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7d996a3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
