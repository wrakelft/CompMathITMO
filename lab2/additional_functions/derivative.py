import properties.properties as pr


def fabric_df(f):
    h = pr.h

    def df(x):
        return (f(x + h) - f(x - h)) / (2 * h)

    return df


def d_phi(func, lambda_):
    return lambda x: 1 + lambda_ * func(x)

