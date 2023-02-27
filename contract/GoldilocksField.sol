// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

library F {
    uint64 constant ORDER = 18446744069414584321;

    function mul(uint64 a, uint64 b) internal pure returns (uint64 res) {
        assembly {
            res := mulmod(a, b, ORDER)
        }
    }

    function square(uint64 a) internal pure returns (uint64) {
        return mul(a, a);
    }

    function add(uint64 a, uint64 b) internal pure returns (uint64 res) {
        assembly {
            res := addmod(a, b, ORDER)
        }
    }

    function sub(uint64 a, uint64 b) internal pure returns (uint64 res) {
        assembly {
            res := addmod(a, sub(ORDER, b), ORDER)
        }
    }
}
