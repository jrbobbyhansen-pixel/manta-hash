"""Tests for manta-hash."""

import hashlib
import os
import tempfile
from manta_hash import compute_hash, compute_all, ALGORITHMS


def test_compute_hash_sha256():
    content = b"hello world"
    expected = hashlib.sha256(content).hexdigest()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        path = f.name
    try:
        result = compute_hash(path, "sha256")
        assert result == expected
    finally:
        os.unlink(path)


def test_compute_hash_md5():
    content = b"test data"
    expected = hashlib.md5(content).hexdigest()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        path = f.name
    try:
        result = compute_hash(path, "md5")
        assert result == expected
    finally:
        os.unlink(path)


def test_compute_all():
    content = b"hello"
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        path = f.name
    try:
        results = compute_all(path)
        for algo in ALGORITHMS:
            assert algo in results
            expected = ALGORITHMS[algo](content).hexdigest()
            assert results[algo] == expected
    finally:
        os.unlink(path)


def test_compute_hash_blake2b():
    content = b"blake2b test"
    expected = hashlib.blake2b(content).hexdigest()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        path = f.name
    try:
        result = compute_hash(path, "blake2b")
        assert result == expected
    finally:
        os.unlink(path)
