"""
PyTorch to RISC-V compilation using TVM Relax
"""

import torch
import torch.nn as nn
import tvm
from tvm import relax
from tvm.contrib import cc
from torch.export import export
from tvm.relax.frontend.torch import from_exported_program


# Define PyTorch model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 4)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(4, 1)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


# Create and export model
model = SimpleNN()
model.eval()
example_input = torch.randn(1, 2)
exported_program = export(model, (example_input,))

# Convert to TVM Relax IR
mod = from_exported_program(exported_program, keep_params_as_input=True)

# Compile for RISC-V
target = tvm.target.Target(
    "llvm -mtriple=riscv64-unknown-linux-gnu -mcpu=generic-rv64 -mattr=+m,+a,+f,+d"
)

with tvm.transform.PassContext(opt_level=3):
    ex = relax.build(mod, target=target)

# Export with RISC-V cross-compiler
cross_compile = cc.cross_compiler("riscv64-linux-gnu-g++")
ex.export_library("simple_nn_riscv.so", fcompile=cross_compile)

# Export LLVM IR
lib_mod = ex.mod
llvm_ir = lib_mod.get_source()
with open("simple_nn_riscv.ll", "w") as f:
    f.write(llvm_ir)
