def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def binom_pmf(k, n, p):
    if k < 0 or k > n:
        return 0
    else:
        return binomial_coefficient(n, k) * (p**k) * ((1 - p) ** (n - k))


def calculate_fail_captcha_decoding_probability(
    luck_percentage_per_to_find_correct_word,
    words_in_captcha,
    access_tries_count,
    successful_access_tries_count,
):
    failed_decoding_percentage_per_captcha = 1 - pow(
        luck_percentage_per_to_find_correct_word / 100, words_in_captcha
    )

    failed_decoding_percentage_in_captchas = binom_pmf(
        access_tries_count - successful_access_tries_count + 1,
        access_tries_count,
        failed_decoding_percentage_per_captcha,
    )

    return failed_decoding_percentage_in_captchas


print(calculate_fail_captcha_decoding_probability(93, 2, 20, 2))
