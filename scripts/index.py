FAST_PARTIAL_ROUND_INITIAL_MATRIX = [
    ["0x80772dc2645b280b", "0xdc927721da922cf8", "0xc1978156516879ad", "0x90e80c591f48b603",
     "0x3a2432625475e3ae", "0x00a2d4321cca94fe", "0x77736f524010c932", "0x904d3f2804a36c54",
     "0xbf9b39e28a16f354", "0x3a1ded54a6cd058b", "0x42392870da5737cf", ],
    ["0xe796d293a47a64cb", "0xb124c33152a2421a", "0x0ee5dc0ce131268a", "0xa9032a52f930fae6",
     "0x7e33ca8c814280de", "0xad11180f69a8c29e", "0xc75ac6d5b5a10ff3", "0xf0674a8dc5a387ec",
     "0xb36d43120eaa5e2b", "0x6f232aab4b533a25", "0x3a1ded54a6cd058b", ],
    ["0xdcedab70f40718ba", "0x14a4a64da0b2668f", "0x4715b8e5ab34653b", "0x1e8916a99c93a88e",
     "0xbba4b5d86b9a3b2c", "0xe76649f9bd5d5c2e", "0xaf8e2518a1ece54d", "0xdcda1344cdca873f",
     "0xcd080204256088e5", "0xb36d43120eaa5e2b", "0xbf9b39e28a16f354", ],
    ["0xf4a437f2888ae909", "0xc537d44dc2875403", "0x7f68007619fd8ba9", "0xa4911db6a32612da",
     "0x2f7e9aade3fdaec1", "0xe7ffd578da4ea43d", "0x43a608e7afa6b5c2", "0xca46546aa99e1575",
     "0xdcda1344cdca873f", "0xf0674a8dc5a387ec", "0x904d3f2804a36c54", ],
    ["0xf97abba0dffb6c50", "0x5e40f0c9bb82aab5", "0x5996a80497e24a6b", "0x07084430a7307c9a",
     "0xad2f570a5b8545aa", "0xab7f81fef4274770", "0xcb81f535cf98c9e9", "0x43a608e7afa6b5c2",
     "0xaf8e2518a1ece54d", "0xc75ac6d5b5a10ff3", "0x77736f524010c932", ],
    ["0x7f8e41e0b0a6cdff", "0x4b1ba8d40afca97d", "0x623708f28fca70e8", "0xbf150dc4914d380f",
     "0xc26a083554767106", "0x753b8b1126665c22", "0xab7f81fef4274770", "0xe7ffd578da4ea43d",
     "0xe76649f9bd5d5c2e", "0xad11180f69a8c29e", "0x00a2d4321cca94fe", ],
    ["0x726af914971c1374", "0x1d7f8a2cce1a9d00", "0x18737784700c75cd", "0x7fb45d605dd82838",
     "0x862361aeab0f9b6e", "0xc26a083554767106", "0xad2f570a5b8545aa", "0x2f7e9aade3fdaec1",
     "0xbba4b5d86b9a3b2c", "0x7e33ca8c814280de", "0x3a2432625475e3ae", ],
    ["0x64dd936da878404d", "0x4db9a2ead2bd7262", "0xbe2e19f6d07f1a83", "0x02290fe23c20351a",
     "0x7fb45d605dd82838", "0xbf150dc4914d380f", "0x07084430a7307c9a", "0xa4911db6a32612da",
     "0x1e8916a99c93a88e", "0xa9032a52f930fae6", "0x90e80c591f48b603", ],
    ["0x85418a9fef8a9890", "0xd8a2eb7ef5e707ad", "0xbfe85ababed2d882", "0xbe2e19f6d07f1a83",
     "0x18737784700c75cd", "0x623708f28fca70e8", "0x5996a80497e24a6b", "0x7f68007619fd8ba9",
     "0x4715b8e5ab34653b", "0x0ee5dc0ce131268a", "0xc1978156516879ad", ],
    ["0x156048ee7a738154", "0x91f7562377e81df5", "0xd8a2eb7ef5e707ad", "0x4db9a2ead2bd7262",
     "0x1d7f8a2cce1a9d00", "0x4b1ba8d40afca97d", "0x5e40f0c9bb82aab5", "0xc537d44dc2875403",
     "0x14a4a64da0b2668f", "0xb124c33152a2421a", "0xdc927721da922cf8", ],
    ["0xd841e8ef9dde8ba0", "0x156048ee7a738154", "0x85418a9fef8a9890", "0x64dd936da878404d",
     "0x726af914971c1374", "0x7f8e41e0b0a6cdff", "0xf97abba0dffb6c50", "0xf4a437f2888ae909",
     "0xdcedab70f40718ba", "0xe796d293a47a64cb", "0x80772dc2645b280b", ],
]

INDENT = '    '


def loop_each_c(c, prefix=''):
    r = 1
    tmp = prefix + f'if (r == {r}) return {FAST_PARTIAL_ROUND_INITIAL_MATRIX[r - 1][c - 1]};'
    for r in range(2, 12):
        tmp += prefix + f'else if (r == {r}) return {FAST_PARTIAL_ROUND_INITIAL_MATRIX[r - 1][c - 1]};'

    return tmp


def make_function_inner(prefix=''):
    c = 1
    tmp = prefix + f'if (c == {c}) ' + '{' \
        + loop_each_c(c, prefix=prefix + INDENT)
    for c in range(2, 12):
        tmp += prefix + '} ' + f'else if (c == {c})' + ' {' \
            + loop_each_c(c, prefix=prefix + INDENT)

    tmp += prefix + '}' \
        + prefix + 'revert("illegal argument");'

    return tmp


def make_function(prefix=''):
    tmp = prefix + 'function getFastPartialRoundInitialMatrix(uint256 r, uint256 c) private pure returns (uint256 x) {' \
        + make_function_inner(prefix=prefix + INDENT) \
        + prefix + '}'

    return tmp


if __name__ == '__main__':
    tmp = make_function(prefix='\n' + INDENT) + '\n'

    print(tmp)
