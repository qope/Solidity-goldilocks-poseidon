# Solidity-Goldilocks-Poseidon

Solidity implementation of Poseidon hash on Goldilocks field, which is compatible with plonky2.

## Test

```
forge test
```

Result

```
Running 1 test for test/Poseidon.t.sol:PoseidonTest
[PASS] testPoseidon() (gas: 3827852)
Test result: ok. 1 passed; 0 failed; finished in 11.89ms
```

## Contract Size
```
forge build --sizes
```
