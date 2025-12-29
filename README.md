# PyTorch to RISC-V Compiler

Cross-compilation toolchain for converting PyTorch neural networks to RISC-V machine code using Apache TVM.

## Requirements

**System:**
```bash
# Arch Linux
sudo pacman -S riscv64-linux-gnu-gcc llvm cmake

# Ubuntu/Debian
sudo apt-get install gcc-riscv64-linux-gnu llvm cmake
```

**Python:**
```bash
pip install torch apache-tvm-ffi
```

**TVM:**
```bash
git clone --recursive https://github.com/apache/tvm
cd tvm/build
echo "set(USE_LLVM ON)" >> ../cmake/config.cmake
cmake .. && make -j4
cd ../python && pip install -e .
```

## Installation

```bash
git clone <repository-url>
cd pytorch-riscv-compiler
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

**Outputs:**
- `simple_nn_riscv.so` - RISC-V binary
- `simple_nn_riscv.ll` - LLVM IR

**Verify:**
```bash
file simple_nn_riscv.so
riscv64-linux-gnu-objdump -d simple_nn_riscv.so | less
```

## Process Flow

```
1. Model Definition        → Define PyTorch neural network
2. Model Export           → Export to torch.export format
3. TVM Conversion         → Convert to TVM Relax IR
4. Target Configuration   → Configure RISC-V target (RV64IMAFDC)
5. Compilation            → Compile to LLVM IR (opt level 3)
6. Binary Generation      → Generate RISC-V shared library
```

## Target Configuration

```python
target = "llvm -mtriple=riscv64-unknown-linux-gnu -mcpu=generic-rv64 -mattr=+m,+a,+f,+d"
```

**Extensions:**
- `m` - Integer multiply/divide
- `a` - Atomic operations
- `f` - Single-precision float
- `d` - Double-precision float

 /usr/riscv64-linux-gnu ./program
```

**Hardware Targets:**
- SiFive Unmatched
- StarFive VisionFive 2
- Custom RISC-V systems


## Troubleshooting

**Build fails at 93%:** Reduce parallelism with `make -j2`

**Missing tvm_ffi:** Run `pip install apache-tvm-ffi`

**Cross-compiler not found:** Verify with `which riscv64-linux-gnu-g++`
