// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../contract/GoldilocksField.sol";
import "../contract/Poseidon.sol";

contract PoseidonTest is Test {
    Poseidon poseidon;

    function setUp() public {
        poseidon = new Poseidon();
    }

    function testHashN() public {
        uint64[] memory input = new uint64[](1);
        input[0] = 1;
        uint64[] memory output = poseidon.hash_n_to_m_no_pad(input, 4);
        assertEq(output[0], 15020833855946683413);
        assertEq(output[1], 2541896837400596712);
        assertEq(output[2], 5158482081674306993);
        assertEq(output[3], 15736419290823331982);
    }
}
