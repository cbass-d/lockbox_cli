S_BOX_ONE = [
b'\x0A', b'\x15', b'\x3F', b'\x90', b'\xFD', b'\x4B', b'\xAA', b'\x5A', b'\x22', b'\xA4', b'\xE7', b'\x46', b'\x96', b'\x44', b'\x97', b'\xC4',
b'\x6D', b'\xB9', b'\xD3', b'\x5C', b'\x9B', b'\x78', b'\x89', b'\x71', b'\x0D', b'\x33', b'\x2C', b'\x19', b'\x83', b'\x74', b'\x35', b'\x95',
b'\xC5', b'\xED', b'\x43', b'\xAE', b'\xE2', b'\x7E', b'\x30', b'\xAD', b'\x63', b'\x04', b'\xB7', b'\x6E', b'\x38', b'\xA9', b'\xDB', b'\x58',
b'\x23', b'\x24', b'\x1D', b'\x3B', b'\x28', b'\xA1', b'\xDF', b'\xE0', b'\x7F', b'\xB0', b'\x57', b'\x1E', b'\xBA', b'\x52', b'\x26', b'\x1C',
b'\xBB', b'\xD2', b'\xDC', b'\x61', b'\x05', b'\x37', b'\x94', b'\x45', b'\x17', b'\x3E', b'\x10', b'\x07', b'\x36', b'\x14', b'\xBF', b'\x6A', 
b'\x80', b'\xF5', b'\x4F', b'\x12', b'\x06', b'\xB6', b'\xEE', b'\xC2', b'\xD4', b'\x65', b'\xBD', b'\x6B', b'\x00', b'\x0F', b'\x32', b'\xAC',
b'\xE3', b'\xFE', b'\xCA', b'\xD0', b'\xDD', b'\xE1', b'\xFF', b'\x4A', b'\x2A', b'\xA0', b'\x5F', b'\x1A', b'\x02', b'\x0E', b'\xB2', b'\x56',
b'\x9E', b'\x40', b'\x2F', b'\x98', b'\xF9', b'\xF3', b'\xF6', b'\xCE', b'\x68', b'\x81', b'\x75', b'\xB5', b'\x6F', b'\xB8', b'\x53', b'\xA6',
b'\xE6', b'\xC6', b'\x6C', b'\x39', b'\x29', b'\x21', b'\x25', b'\x9D', b'\xC1', b'\x55', b'\x1F', b'\x3A', b'\xA8', b'\x5B', b'\xA2', b'\x5E',
b'\x9A', b'\xF8', b'\x73', b'\x0C', b'\xB3', b'\xD6', b'\x64', b'\x3D', b'\x91', b'\x7D', b'\xB1', b'\xD7', b'\xE4', b'\xC7', b'\xEC', b'\xC3',
b'\x54', b'\x9F', b'\xC0', b'\xD5', b'\xE5', b'\x47', b'\x16', b'\xBE', b'\xEA', b'\x7A', b'\x88', b'\xF1', b'\xF7', b'\x4E', b'\x92', b'\xFC',
b'\xCB', b'\x50', b'\x27', b'\x9C', b'\x41', b'\xAF', b'\x62', b'\x84', b'\x4D', b'\x13', b'\x86', b'\x4C', b'\x93', b'\x7C', b'\x31', b'\x2D',
b'\x99', b'\x79', b'\x09', b'\x8B', b'\x70', b'\x8D', b'\xC9', b'\x51', b'\xA7', b'\x66', b'\x3C', b'\x11', b'\x87', b'\xCC', b'\x69', b'\x01',
b'\x8F', b'\xC8', b'\xD1', b'\x5D', b'\x1B', b'\x82', b'\xF4', b'\xCF', b'\xE8', b'\x7B', b'\x08', b'\x0B', b'\x8A', b'\xF0', b'\x77', b'\xB4',
b'\xEF', b'\x42', b'\x2E', b'\x18', b'\x03', b'\x8E', b'\x48', b'\x2B', b'\x20', b'\xA5', b'\x67', b'\xBC', b'\xEB', b'\xFA', b'\x72', b'\x8C',
b'\x49', b'\xAB', b'\xDA', b'\xD8', b'\xD9', b'\x59', b'\xA3', b'\xDE', b'\x60', b'\x85', b'\xCD', b'\xE9', b'\xFB', b'\xF2', b'\x76', b'\x34'
]

S_BOX_TWO = [
b'\x31', b'\x2E', b'\x04', b'\xAB', b'\xC6', b'\x70', b'\x91', b'\x61', b'\x19', b'\x9F', b'\xDC', b'\x7D', b'\xAD', b'\x7F', b'\xAC', b'\xFF',
b'\x56', b'\x82', b'\xE8', b'\x67', b'\xA0', b'\x43', b'\xB2', b'\x4A', b'\x36', b'\x08', b'\x17', b'\x22', b'\xB8', b'\x4F', b'\x0E', b'\xAE',
b'\xFE', b'\xD6', b'\x78', b'\x95', b'\xD9', b'\x45', b'\x0B', b'\x96', b'\x58', b'\x3F', b'\x8C', b'\x55', b'\x03', b'\x92', b'\xE0', b'\x63',
b'\x18', b'\x1F', b'\x26', b'\x00', b'\x13', b'\x9A', b'\xE4', b'\xDB', b'\x44', b'\x8B', b'\x6C', b'\x25', b'\x81', b'\x69', b'\x1D', b'\x27',
b'\x80', b'\xE9', b'\xE7', b'\x5A', b'\x3E', b'\x0C', b'\xAF', b'\x7E', b'\x2C', b'\x05', b'\x2B', b'\x3C', b'\x0D', b'\x2F', b'\x84', b'\x51',
b'\xBB', b'\xCE', b'\x74', b'\x29', b'\x3D', b'\x8D', b'\xD5', b'\xF9', b'\xEF', b'\x5E', b'\x86', b'\x50', b'\x3B', b'\x34', b'\x09', b'\x97',
b'\xD8', b'\xC5', b'\xF1', b'\xEB', b'\xE6', b'\xDA', b'\xC4', b'\x71', b'\x11', b'\x9B', b'\x64', b'\x21', b'\x39', b'\x35', b'\x89', b'\x6D',
b'\xA5', b'\x7B', b'\x14', b'\xA3', b'\xC2', b'\xC8', b'\xCD', b'\xF5', b'\x53', b'\xBA', b'\x4E', b'\x8E', b'\x54', b'\x83', b'\x68', b'\x9D',
b'\xDD', b'\xFD', b'\x57', b'\x02', b'\x12', b'\x1A', b'\x1E', b'\xA6', b'\xFA', b'\x6E', b'\x24', b'\x01', b'\x93', b'\x60', b'\x99', b'\x65',
b'\xA1', b'\xC3', b'\x48', b'\x37', b'\x88', b'\xED', b'\x5F', b'\x06', b'\xAA', b'\x46', b'\x8A', b'\xEC', b'\xDF', b'\xFC', b'\xD7', b'\xF8',
b'\x6F', b'\xA4', b'\xFB', b'\xEE', b'\xDE', b'\x7C', b'\x2D', b'\x85', b'\xD1', b'\x41', b'\xB3', b'\xCA', b'\xCC', b'\x75', b'\xA9', b'\xC7',
b'\xF0', b'\x6B', b'\x1C', b'\xA7', b'\x7A', b'\x94', b'\x59', b'\xBF', b'\x76', b'\x28', b'\xBD', b'\x77', b'\xA8', b'\x47', b'\x0A', b'\x16',
b'\xA2', b'\x42', b'\x32', b'\xB0', b'\x4B', b'\xB6', b'\xF2', b'\x6A', b'\x9C', b'\x5D', b'\x07', b'\x2A', b'\xBC', b'\xF7', b'\x52', b'\x3A',
b'\xB4', b'\xF3', b'\xEA', b'\x66', b'\x20', b'\xB9', b'\xCF', b'\xF4', b'\xD3', b'\x40', b'\x33', b'\x30', b'\xB1', b'\xCB', b'\x4C', b'\x8F',
b'\xD4', b'\x79', b'\x15', b'\x23', b'\x38', b'\xB5', b'\x73', b'\x10', b'\x1B', b'\x9E', b'\x5C', b'\x87', b'\xD0', b'\xC1', b'\x49', b'\xB7',
b'\x72', b'\x90', b'\xE1', b'\xE3', b'\xE2', b'\x62', b'\x98', b'\xE5', b'\x5B', b'\xBE', b'\xF6', b'\xD2', b'\xC0', b'\xC9', b'\x4D', b'\x0F'
]

S_BOX_THREE = [
b'\x4A', b'\x55', b'\x7F', b'\xD0', b'\xBD', b'\x0B', b'\xEA', b'\x1A', b'\x62', b'\xE4', b'\xA7', b'\x06', b'\xD6', b'\x04', b'\xD7', b'\x84',
b'\x2D', b'\xF9', b'\x93', b'\x1C', b'\xDB', b'\x38', b'\xC9', b'\x31', b'\x4D', b'\x73', b'\x6C', b'\x59', b'\xC3', b'\x34', b'\x75', b'\xD5',
b'\x85', b'\xAD', b'\x03', b'\xEE', b'\xA2', b'\x3E', b'\x70', b'\xED', b'\x23', b'\x44', b'\xF7', b'\x2E', b'\x78', b'\xE9', b'\x9B', b'\x18',
b'\x63', b'\x64', b'\x5D', b'\x7B', b'\x68', b'\xE1', b'\x9F', b'\xA0', b'\x3F', b'\xF0', b'\x17', b'\x5E', b'\xFA', b'\x12', b'\x66', b'\x5C',
b'\xFB', b'\x92', b'\x9C', b'\x21', b'\x45', b'\x77', b'\xD4', b'\x05', b'\x57', b'\x7E', b'\x50', b'\x47', b'\x76', b'\x54', b'\xFF', b'\x2A',
b'\xC0', b'\xB5', b'\x0F', b'\x52', b'\x46', b'\xF6', b'\xAE', b'\x82', b'\x94', b'\x25', b'\xFD', b'\x2B', b'\x40', b'\x4F', b'\x72', b'\xEC',
b'\xA3', b'\xBE', b'\x8A', b'\x90', b'\x9D', b'\xA1', b'\xBF', b'\x0A', b'\x6A', b'\xE0', b'\x1F', b'\x5A', b'\x42', b'\x4E', b'\xF2', b'\x16',
b'\xDE', b'\x00', b'\x6F', b'\xD8', b'\xB9', b'\xB3', b'\xB6', b'\x8E', b'\x28', b'\xC1', b'\x35', b'\xF5', b'\x2F', b'\xF8', b'\x13', b'\xE6',
b'\xA6', b'\x86', b'\x2C', b'\x79', b'\x69', b'\x61', b'\x65', b'\xDD', b'\x81', b'\x15', b'\x5F', b'\x7A', b'\xE8', b'\x1B', b'\xE2', b'\x1E',
b'\xDA', b'\xB8', b'\x33', b'\x4C', b'\xF3', b'\x96', b'\x24', b'\x7D', b'\xD1', b'\x3D', b'\xF1', b'\x97', b'\xA4', b'\x87', b'\xAC', b'\x83',
b'\x14', b'\xDF', b'\x80', b'\x95', b'\xA5', b'\x07', b'\x56', b'\xFE', b'\xAA', b'\x3A', b'\xC8', b'\xB1', b'\xB7', b'\x0E', b'\xD2', b'\xBC',
b'\x8B', b'\x10', b'\x67', b'\xDC', b'\x01', b'\xEF', b'\x22', b'\xC4', b'\x0D', b'\x53', b'\xC6', b'\x0C', b'\xD3', b'\x3C', b'\x71', b'\x6D',
b'\xD9', b'\x39', b'\x49', b'\xCB', b'\x30', b'\xCD', b'\x89', b'\x11', b'\xE7', b'\x26', b'\x7C', b'\x51', b'\xC7', b'\x8C', b'\x29', b'\x41',
b'\xCF', b'\x88', b'\x91', b'\x1D', b'\x5B', b'\xC2', b'\xB4', b'\x8F', b'\xA8', b'\x3B', b'\x48', b'\x4B', b'\xCA', b'\xB0', b'\x37', b'\xF4',
b'\xAF', b'\x02', b'\x6E', b'\x58', b'\x43', b'\xCE', b'\x08', b'\x6B', b'\x60', b'\xE5', b'\x27', b'\xFC', b'\xAB', b'\xBA', b'\x32', b'\xCC',
b'\x09', b'\xEB', b'\x9A', b'\x98', b'\x99', b'\x19', b'\xE3', b'\x9E', b'\x20', b'\xC5', b'\x8D', b'\xA9', b'\xBB', b'\xB2', b'\x36', b'\x74'
]

S_BOX_FOUR = [
b'\xCA', b'\xD5', b'\xFF', b'\x50', b'\x3D', b'\x8B', b'\x6A', b'\x9A', b'\xE2', b'\x64', b'\x27', b'\x86', b'\x56', b'\x84', b'\x57', b'\x04',
b'\xAD', b'\x79', b'\x13', b'\x9C', b'\x5B', b'\xB8', b'\x49', b'\xB1', b'\xCD', b'\xF3', b'\xEC', b'\xD9', b'\x43', b'\xB4', b'\xF5', b'\x55',
b'\x05', b'\x2D', b'\x83', b'\x6E', b'\x22', b'\xBE', b'\xF0', b'\x6D', b'\xA3', b'\xC4', b'\x77', b'\xAE', b'\xF8', b'\x69', b'\x1B', b'\x98',
b'\xE3', b'\xE4', b'\xDD', b'\xFB', b'\xE8', b'\x61', b'\x1F', b'\x20', b'\xBF', b'\x70', b'\x97', b'\xDE', b'\x7A', b'\x92', b'\xE6', b'\xDC',
b'\x7B', b'\x12', b'\x1C', b'\xA1', b'\xC5', b'\xF7', b'\x54', b'\x85', b'\xD7', b'\xFE', b'\xD0', b'\xC7', b'\xF6', b'\xD4', b'\x7F', b'\xAA',
b'\x40', b'\x35', b'\x8F', b'\xD2', b'\xC6', b'\x76', b'\x2E', b'\x02', b'\x14', b'\xA5', b'\x7D', b'\xAB', b'\xC0', b'\xCF', b'\xF2', b'\x6C',
b'\x23', b'\x3E', b'\x0A', b'\x10', b'\x1D', b'\x21', b'\x3F', b'\x8A', b'\xEA', b'\x60', b'\x9F', b'\xDA', b'\xC2', b'\xCE', b'\x72', b'\x96',
b'\x5E', b'\x80', b'\xEF', b'\x58', b'\x39', b'\x33', b'\x36', b'\x0E', b'\xA8', b'\x41', b'\xB5', b'\x75', b'\xAF', b'\x78', b'\x93', b'\x66',
b'\x26', b'\x06', b'\xAC', b'\xF9', b'\xE9', b'\xE1', b'\xE5', b'\x5D', b'\x01', b'\x95', b'\xDF', b'\xFA', b'\x68', b'\x9B', b'\x62', b'\x9E',
b'\x5A', b'\x38', b'\xB3', b'\xCC', b'\x73', b'\x16', b'\xA4', b'\xFD', b'\x51', b'\xBD', b'\x71', b'\x17', b'\x24', b'\x07', b'\x2C', b'\x03',
b'\x94', b'\x5F', b'\x00', b'\x15', b'\x25', b'\x87', b'\xD6', b'\x7E', b'\x2A', b'\xBA', b'\x48', b'\x31', b'\x37', b'\x8E', b'\x52', b'\x3C',
b'\x0B', b'\x90', b'\xE7', b'\x5C', b'\x81', b'\x6F', b'\xA2', b'\x44', b'\x8D', b'\xD3', b'\x46', b'\x8C', b'\x53', b'\xBC', b'\xF1', b'\xED',
b'\x59', b'\xB9', b'\xC9', b'\x4B', b'\xB0', b'\x4D', b'\x09', b'\x91', b'\x67', b'\xA6', b'\xFC', b'\xD1', b'\x47', b'\x0C', b'\xA9', b'\xC1',
b'\x4F', b'\x08', b'\x11', b'\x9D', b'\xDB', b'\x42', b'\x34', b'\x0F', b'\x28', b'\xBB', b'\xC8', b'\xCB', b'\x4A', b'\x30', b'\xB7', b'\x74',
b'\x2F', b'\x82', b'\xEE', b'\xD8', b'\xC3', b'\x4E', b'\x88', b'\xEB', b'\xE0', b'\x65', b'\xA7', b'\x7C', b'\x2B', b'\x3A', b'\xB2', b'\x4C',
b'\x89', b'\x6B', b'\x1A', b'\x18', b'\x19', b'\x99', b'\x63', b'\x1E', b'\xA0', b'\x45', b'\x0D', b'\x29', b'\x3B', b'\x32', b'\xB6', b'\xF4'
]

# These are 1-indexed representations of the permutations. so number 1 = index 0, number 2 = index 1 and so forth
# FIRST_PHASE_P_BOX = [3*(i**3) % 17 for i in range(1, 17)]
FIRST_PHASE_P_BOX = [3, 7, 13, 5, 1, 2, 9, 6, 11, 8, 15, 16, 12, 4, 10, 14]

# FUNCTION_PHASE_P_BOX = [i**3 % 33 for i in range(1, 33)]
FUNCTION_PHASE_P_BOX = [1, 8, 27, 31, 26, 18, 13, 17, 3, 10, 11, 12, 19, 5, 9, 4, 29, 24, 28, 14, 21, 22, 23, 30, 16, 20, 15, 7, 2, 6, 25, 32]