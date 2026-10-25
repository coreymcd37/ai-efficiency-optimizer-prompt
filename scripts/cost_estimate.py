#!/usr/bin/env python3
"""Estimate the cost of a batch AI job: items x tokens x price per token.

Prices are never built in. Pass the figures you verified on the provider's
official pricing page (see references/pricing-verification.md).

Example:
    python scripts/cost_estimate.py --items 2000 --input-tokens 400 \
        --output-tokens 60 --input-price 0.50 --output-price 1.50 --per 1000000
"""

import argparse
import sys


def positive(value: str) -> float:
    """Parse a non-negative number for argparse."""
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value!r} is not a number")
    if number < 0:
        raise argparse.ArgumentTypeError(f"{value!r} must be zero or more")
    return number


def ratio(value: str) -> float:
    """Parse a fraction between 0 and 1 for argparse."""
    number = positive(value)
    if number > 1:
        raise argparse.ArgumentTypeError(f"{value!r} must be between 0 and 1")
    return number


def cost(items, input_tokens, output_tokens, input_price, output_price, per):
    """Return the cost for one scenario."""
    return items * (input_tokens * input_price + output_tokens * output_price) / per


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Low / expected / high cost estimate for a batch AI job. "
            "Uses the formula: items x tokens per item x price per token. "
            "You supply the prices; verify them on the provider's official pricing page."
        )
    )
    parser.add_argument("--items", type=positive, required=True, help="number of items to process")
    parser.add_argument("--input-tokens", type=positive, required=True, help="expected input tokens per item")
    parser.add_argument("--output-tokens", type=positive, default=0, help="expected output tokens per item (default: 0)")
    parser.add_argument("--input-price", type=positive, required=True, help="price per --per input tokens")
    parser.add_argument("--output-price", type=positive, default=0, help="price per --per output tokens (default: 0)")
    parser.add_argument("--per", type=positive, default=1_000_000, help="token count the prices refer to (default: 1000000)")
    parser.add_argument("--low", type=positive, default=0.7, help="multiplier for the low estimate (default: 0.7)")
    parser.add_argument("--high", type=positive, default=1.5, help="multiplier for the high estimate (default: 1.5)")
    parser.add_argument("--escalate", type=ratio, default=0,
                        help="share of items sent to a stronger model, 0-1 (default: 0)")
    parser.add_argument("--escalate-input-price", type=positive, default=0, help="stronger model's input price per --per tokens")
    parser.add_argument("--escalate-output-price", type=positive, default=0, help="stronger model's output price per --per tokens")
    parser.add_argument("--currency", default="$", help="currency symbol for the output (default: $)")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    if args.per == 0:
        print("error: --per must be greater than zero", file=sys.stderr)
        return 2
    if args.low > args.high:
        print("error: --low must not be greater than --high", file=sys.stderr)
        return 2

    base = cost(args.items, args.input_tokens, args.output_tokens,
                args.input_price, args.output_price, args.per)
    extra = cost(args.items * args.escalate, args.input_tokens, args.output_tokens,
                 args.escalate_input_price, args.escalate_output_price, args.per)
    expected = base + extra
    c = args.currency

    print(f"Items: {args.items:g}  |  Tokens per item: {args.input_tokens:g} in, {args.output_tokens:g} out")
    print(f"Base model:       {c}{base:,.4f}")
    if args.escalate:
        print(f"Escalated ({args.escalate:.0%}): {c}{extra:,.4f}")
    print(f"Low      (x{args.low:g}): {c}{expected * args.low:,.4f}")
    print(f"Expected (x1):   {c}{expected:,.4f}")
    print(f"High     (x{args.high:g}): {c}{expected * args.high:,.4f}")
    print("Prices are the ones you supplied. Record the source and date you checked them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
