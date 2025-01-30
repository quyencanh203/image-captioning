import torch

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda") # using gpu
    print("CUDA is available. Using GPU:", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu") # using cpu
    print("CUDA is not available. Using CPU")