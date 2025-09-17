def count_even_odd(*args):

    even_count = 0

    odd_count = 0

    for i in args:

        if i % 2 == 0:

            even_count += 1

        else:

            odd_count += 1

    print(f"{odd_count} odd nos are passed")

    print(f"{even_count} even nos are passed")

count_even_odd(1,2,3,4,5,6,7,8,9)