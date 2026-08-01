# manta-hash

Compute file hashes using multiple algorithms — md5, sha1, sha256, sha512, and blake2b.

Part of the [Manta](https://github.com/jrbobbyhansen-pixel) collection of zero-dependency Python CLI tools.

## Installation

```bash
pip install manta-hash
```

Or run directly:

```bash
python -m manta_hash --help
```

## Usage

```bash
# Compute SHA-256 hash (default)
manta-hash file.bin

# Use a specific algorithm
manta-hash -a md5 file.bin
manta-hash -a sha1 file.bin
manta-hash -a blake2b file.bin

# Compute all supported hashes at once
manta-hash --all file.bin
```

### Supported Algorithms

| Algorithm  | Description                        |
|------------|------------------------------------|
| `md5`      | 128-bit MD5 hash                   |
| `sha1`     | 160-bit SHA-1 hash                 |
| `sha256`   | 256-bit SHA-256 hash (default)     |
| `sha512`   | 512-bit SHA-512 hash               |
| `blake2b`  | BLAKE2b cryptographic hash         |

## API

```python
from manta_hash import compute_hash, compute_all

# Single algorithm
digest = compute_hash("file.bin", "sha256")

# All algorithms
results = compute_all("file.bin")
# => {"md5": "...", "sha1": "...", "sha256": "...", "sha512": "...", "blake2b": "..."}
```

## License

MIT — see [LICENSE](LICENSE).
