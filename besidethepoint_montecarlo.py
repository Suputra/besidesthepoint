import torch

def sample(batch_size, device):
    # Generate random values in batches directly on the GPU
    x = torch.rand(batch_size, device=device) * 0.5
    y = torch.rand(batch_size, device=device) * 0.5
    swap = y>x

    x[swap], y[swap] = y[swap], x[swap]

    integral1 = torch.sqrt()


    return torch.sum(cond).item()  # Count how many True values

# Run trials in batches
batch_size = 5 * 10**8  # Adjust batch size for memory constraints


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
