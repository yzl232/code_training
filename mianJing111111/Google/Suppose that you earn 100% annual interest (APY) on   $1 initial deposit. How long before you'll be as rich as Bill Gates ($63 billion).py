# encoding=utf-8
# Suppose that you earn 100% annual interest (APY) on
  #  $1 initial deposit. How long before you'll be as rich as Bill Gates ($63 billion)

'''
 Taking just the information we are given and ignoring taxes etc. 100% annual (compound) interest is the same as doubling your investment every year. So for the first four years it would go like this:
$1, $2, $4, $8, $16, $32, ... Look familiar?

Therefore: 63 Billion = 2^x or x = log2(63 billion)
In an interview we wouldn't be able to throw this into a calculator so we would need to do it by hand.

We can estimate powers of 2 as powers of 1000:
2^10 ~= 1000^1
2^20 ~= 1000^2
etc.

Therefore 63 billion = 63 * 1000^3
or approximately = 63 * 2^30

We know that 64 is 2^6 so we can substitute that with the 63 to get:
2^6 * 2^30 which = 2^36
log2 of 2^36 is 36

Therefore you would have $63 billion after 36 years.

Now if we validate with the calculator we see that after 36 years we would actually have about $68/$69 billion. While if we only waited until 35 years we would only have $34 billion.

'''