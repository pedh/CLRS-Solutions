"""
Complex multiplication.
"""

import random


def complex_multiply(real1, imag1, real2, imag2):
    """Complex multiplication."""
    sum1 = (real1 - imag1) * (real2 + imag2)
    sum2 = (real1 + imag1) * (real2 - imag2)
    sum3 = imag1 * real2
    result_real = (sum1 + sum2) / 2
    result_imag = (sum1 - result_real) + 2 * sum3
    return result_real, result_imag


def main():
    """The main function."""
    real1, imag1, real2, imag2 = (random.randint(-10, 10) for _ in range(4))
    print(real1, imag1, real2, imag2)
    result_real, result_imag = complex_multiply(real1, imag1, real2, imag2)
    print(result_real, result_imag)
    print(real1 * real2 - imag1 * imag2, real1 * imag2 + imag1 * real2)


if __name__ == "__main__":
    main()
