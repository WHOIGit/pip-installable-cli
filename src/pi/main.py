import sys
from decimal import Decimal, getcontext
import argparse

from tqdm import tqdm

def compute_pi(precision, progress=True):
    # Add a small buffer to the precision to account for potential rounding errors
    extra_precision = 5
    getcontext().prec = precision + extra_precision
    
    C = 426880 * Decimal(10005).sqrt()
    L = 13591409
    X = 1
    M = 1
    K = 6
    S = L
    iter_range = range(1, precision + extra_precision)
    if progress:
        iter_range = tqdm(iter_range, desc="Calculating Pi", file=sys.stderr)
    for i in iter_range:
        M = M * (K ** 3 - 16 * K) // (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = C / S
    return pi

def main():
    parser = argparse.ArgumentParser(description="Calculate Pi to a specified number of decimal places.")
    parser.add_argument("digits", type=int, help="Number of decimal places to calculate Pi to")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show progress bar")
    args = parser.parse_args()

    if args.digits <= 0:
        parser.error("Number of digits must be a positive integer")

    progress = args.verbose

    pi = compute_pi(args.digits, progress)

    # Convert to string and trim to the requested number of decimal places
    pi_str = f"{pi:.{args.digits + 1}f}"
    pi_trimmed = pi_str[:-1]  # Remove the last digit

    print(pi_trimmed)

if __name__ == "__main__":
    main()