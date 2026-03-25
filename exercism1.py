def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    product = temperature * neutrons_produced_per_second
    threshold_min = threshold - (0.1 * threshold)
    threshold_max = threshold + (0.1 * threshold)

    if product < (0.9 * threshold):
        return "LOW"
    elif (threshold_min < product < threshold_max):
        return "NORMAL"
    else:
        return "DANGER"
    
result =fail_safe(10, 901, 10000)
print(result)