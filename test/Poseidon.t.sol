// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "../contract/Poseidon.sol";

contract PoseidonTest is Test, Poseidon {
    // Poseidon poseidon;

    function setUp() public {
        // poseidon = new Poseidon();
    }

    function testPoseidon() public {
        uint256[] memory input = new uint256[](1);
        input[0] = 1;
        uint256 gasBefore = gasleft();
        uint256[] memory output = _hash_n_to_m_no_pad(input, 4);
        uint256 gasAfter = gasleft();
        console.log("used gas: %d", gasBefore - gasAfter);
        assertEq(output[0], 15020833855946683413);
        assertEq(output[1], 2541896837400596712);
        assertEq(output[2], 5158482081674306993);
        assertEq(output[3], 15736419290823331982);
        // memo forge build --sizes
    }
}
