luck_percentage_per_to_find_correct_letter = 98
luck_percentage_to_find_word_length = 97
access_tries_count = 20
successful_access_tries_count = 15
min_words_to_guess_captcha = 1
words_length = [4, 6]


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
    luck_percentage_per_to_find_correct_letter,
    luck_percentage_to_find_word_length,
    access_tries_count,
    successful_access_tries_count,
    min_words_to_guess_captcha,
    words_length,
):
    probability_to_find_all_words = 0
    for i in words_length:
        probability_to_find_all_words += (
            luck_percentage_to_find_word_length
            / 100
            * pow(luck_percentage_per_to_find_correct_letter / 100, i)
        )

    average_probability_to_find_one_word = probability_to_find_all_words / len(
        words_length
    )

    failed_decoding_percentage_in_captchas = binom_pmf(
        access_tries_count - successful_access_tries_count + 1,
        access_tries_count,
        1 - average_probability_to_find_one_word,
    )

    return failed_decoding_percentage_in_captchas


print(
    calculate_fail_captcha_decoding_probability(
        luck_percentage_per_to_find_correct_letter,
        luck_percentage_to_find_word_length,
        access_tries_count,
        successful_access_tries_count,
        min_words_to_guess_captcha,
        words_length,
    )
)
