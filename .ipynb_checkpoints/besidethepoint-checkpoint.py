import torch

def sample(batch_size, device):
    # Generate random values in batches directly on the GPU
    xb = torch.rand(batch_size, device=device) * 2 - 1
    yb = torch.rand(batch_size, device=device) * 2 - 1
    xr = torch.rand(batch_size, device=device) * 2 - 1
    yr = torch.rand(batch_size, device=device) * 2 - 1


    ## Something is wrong with the following checks!
    # squares = xb**2 - xr**2 + yb**2 - yr**2
    # dx = 2 * (xb - xr)
    # dy = 2 * (yb - yr)

    # # # Use vectorized conditional checks for cond
    # cond1 = (torch.abs(yb) < xb) & ((-dy <= squares - dx) & (squares - dx <= dy))
    # cond2 = (torch.abs(yb) < -xb) & ((-dy <= squares + dx) & (squares + dx <= dy))
    # cond3 = (torch.abs(xb) < yb) & ((-dx <= squares - dy) & (squares - dy <= dx))
    # cond4 = (torch.abs(xb) < -yb) & ((-dx <= squares + dy) & (squares + dy <= dx))

    b = (yr**2 - yb**2 + xr**2 - xb**2) / (2 * (yr - yb))
    m = -(xr - xb) / (yr - yb)

    # Use vectorized conditional checks for cond
    cond5 = (torch.abs(yb) < xb) & ((-1 <= m + b) & (m + b <= 1))
    cond6 = (torch.abs(yb) < -xb) & ((-1 <= -m + b) & (-m + b <= 1))
    cond7 = (torch.abs(xb) < yb) & ((-1 <= (1 - b) / m) & ((1 - b) / m <= 1))
    cond8 = (torch.abs(xb) < -yb) & ((-1 <= (-1 - b) / m) & ((-1 - b) / m <= 1))

    breakpoint()

    # Combine conditions
    cond = cond1 | cond2 | cond3 | cond4

    return torch.sum(cond).item()  # Count how many True values

# Run trials in batches
batch_size = 5 * 10**8  # Adjust batch size for memory constraints
trials = 0
successes = 0

device = torch.device("mps")  # Use Metal Performance Shaders on M-series Mac
resp = ""

print("starting loop")
while resp != "finish":
    try:
        successes += sample(batch_size, device)
        trials += batch_size
    except KeyboardInterrupt:
        resp = input(" finished? ")

# Calculate the ratio of successes
print(f"trials {trials} successes {successes}")
print(successes / trials)
