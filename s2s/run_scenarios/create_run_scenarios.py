import numpy as np





def gen_fake_data():
    # First we generate the (x,y,z) tuples to imitate "real" data
    # Half of this will be in the + direction, half will be in the - dir.
    xy_max_error = 0.2

    # Generate the "real" x,y vectors
    x = np.linspace(min_x, max_x, dim_x)
    y = np.linspace(min_y, max_y, dim_y)

    # Apply an error to x,y
    x_err = (np.random.rand(*x.shape) - 0.5) * xy_max_error
    y_err = (np.random.rand(*y.shape) - 0.5) * xy_max_error
    x *= (1 + x_err)
    y *= (1 + y_err)

    # Generate fake z
    rows = []
    for ix in x:
        for iy in y:
            z = math.sqrt(ix**2 + iy**2)
            rows.append([ix,iy,z])

    mat = np.array(rows)
    return mat

gen_fake_data()
