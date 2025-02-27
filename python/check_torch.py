import os
import torch

# read environment variables
SLURM_ARRAY_TASK_ID = os.getenv('SLURM_ARRAY_TASK_ID')
print(f"SLURM_ARRAY_TASK_ID={SLURM_ARRAY_TASK_ID}")

# even if check is calling "cuda", the function works for CUDA and ROCm devices
if torch.cuda.is_available():
    print(f"TORCH CUDA device name: {torch.cuda.get_device_name(0)}")
    print(f"TORCH CUDA device count: {str(torch.cuda.device_count())}")
else:
    print("TORCH device name: " + "[CPU]")

print("Run TORCH test...")

x = torch.rand(5, 3)
print(x)
