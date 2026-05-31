def square_root_bisection(number, tolerance=1e-3, max_iterations=20):
    if number == 0:
        print(f'The square root of {number} is {number}')
        return number
    if number == 1:
        print("The square root of 1 is 1")
        return 1
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')


    low = 0
    high = max(1, number)

    for i in range(max_iterations):
        mid = (low + high) / 2
        f_mid = mid ** 2 - number

        if f_mid == 0:
            # Exact root — rare but possible
            print(f'The square root of {number} is approximately {mid}')
            return mid
        elif f_mid < 0:
            # mid^2 is too small, root is in right half
            low = mid
        else:
            # mid^2 is too large, root is in left half
            high = mid

        if abs(high - low) <= tolerance:
            print(f'The square root of {number} is approximately {mid}')
            return mid

    print(f"Failed to converge within {max_iterations} iterations")
    return None