"""Compute the utility value of monetary quantities under prospect theory

"""
from functools import partial


def power_utility_loss_aversion(z, ɣ, λ):
    """Return the utility evaluation of a monetary quantity z under power
    utility with utility curvature parameter ɣ and loss aversion
    parameter λ.

    """

    out = z ** (1 - ɣ) if z >= 0 else -λ * (-z) ** (1 - ɣ)

    return out


# Define the characteristics of the individual.
power_coefficient = 0.5
loss_aversion_coefficient = 2.0

# Define this individual's utility.
individuals_utility = partial(
    power_utility_loss_aversion, ɣ=power_coefficient, λ=loss_aversion_coefficient
)

# Define the monetary payoffs.
payoffs = [500, -550]

# Set up the calculation of the utility values via list comprehension.
out = [individuals_utility(payoff) for payoff in payoffs]

# Carry out the computations and print them to the screen.
for item in out:
    print(item)
