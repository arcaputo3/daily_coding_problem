"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive)
with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).

What if we wanted to create a rand7() function using rand5()?
"""

# Get random functions
import numpy as np
# Plotting
import matplotlib.pyplot as plt


def rand7():
    """ Returns integer from 1 to 7 with uniform probability. """
    return np.random.randint(1, 8)


def rand5():
    """ Returns integer from 1 to 5 with uniform probability.
        Also returns number of iterations taken. """
    x = rand7()
    count = 1
    while x > 5:
        x = rand7()
        count += 1
    return x, count


def true_rand5():
    """ Returns integer from 1 to 5 with uniform probability. """
    return np.random.randint(1, 6)


def rand7_w5():
    """ Returns integer from 1 to 7 with uniform probability
        using true_rand5().
    Idea: Create a grid:
         1   2   3   4   5
       -------------------
    1 |  2   3   4   5   6
    2 |  3   4   5   6   7
    3 |  4   5   6   7   8
    4 |  5   6   7   8   9
    5 |  6   7   8   9   10

    Divide grid into unique areas of 3.
    Create 7 events denoting unique areas.
    Resample if z lands in 7 (denoting 4/25 event not covered).
    """
    x, y = true_rand5(), true_rand5()
    z = x + y
    # Note that each mapping has 3 possibilities
    # out of a total 21 possibilities
    d = {
        # Upper left hand corner: 1
        2: 1,
        3: 1,
        # 4 diagonal: 2
        4: 2,
        # Lower left hand corner (one 5, two 6's): 3
        # Upper 5 diagonal: 4
        # Upper 6 diagonal: 5
        5: 3 if x == 4 else 4,
        6: 5 if x <= 3 else 3,
        # 8 diagonal: 6
        8: 6,
        # Lower right hand corner: 7
        9: 7,
        10: 7,
    }
    return d[z] if z in d else rand7_w5()


if __name__ == "__main__":
    # Test Case
    """
    Expected number of iterations of rand5:
    Here sum() represents sum from i = 0 to inf

    E   = (5/7) + 2(2/7)(5/7) + 3(2/7)^2(5/7) + ...
        = (5/7) * sum((i + 1)(2/7)^i)
        = (5/7) * 1/(1 - 2/7)^2
        = (5/7) * 1/(35/49)
        = (5/7) * (49/35)
        = 7/5

    Expected number of iterations of rand7_w5:

    E   = (21/25) + 2(4/25)(21/25) + 3(4/25)^2(21/25) + ...
        = (21/25) * sum((i + 1)(4/25)^i)
        = (21/25) * 1/(1 - 4/25)^2
        = (21/25) * 1/(441/625)
        = (21/25) * (625/441)
        = 25/21

    In fact, any remapping that has probability of success p
    is a geometric event with expected value 1/p .
    Therefore, runtime is O(1/p).
    """

    # Generate 10,000 random U(1, 5) and resp. counts
    iters_5 = np.array([rand5() for _ in range(10000)])
    mean_rand_5, mean_count_5 = np.mean(iters_5, axis=0)
    print(" rand5() ")
    print("Simulated Expected Value: ", mean_rand_5)
    print("Simulated Expected Iterations per run: ", mean_count_5)
    print("Actual Expected Value: ", sum(range(1, 6)) / 5)
    print("Actual Expected Iterations per run: ", 7 / 5)
    print()

    # Generate 10,000 random U(1, 7)
    iters_7 = np.array([rand7_w5() for _ in range(10000)])
    mean_rand_7 = np.mean(iters_7, axis=0)
    print(" rand7_w5() ")
    print("Simulated Expected Value: ", mean_rand_7)
    print("Actual Expected Value: ", sum(range(1, 8)) / 7)

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False,
                    bottom=False, left=False, right=False)
    plt.grid(False)
    ax1.hist(iters_5[:, 0], bins=5)
    ax1.set_title('rand5()')
    ax2.hist(iters_7, bins=7)
    ax2.set_title('rand7_w5()')
    plt.xlabel('Output')
    plt.ylabel('Count (10,000 Samples)')
    plt.show()
