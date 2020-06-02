// 无符号数默认逻辑右移，左边0填充
uint32_t reverseBits(uint32_t n) {
	uint32_t res{ 0 };
	uint32_t x{ 1u << 31 };
	while (n) {
		if (n & 1) {
			res += x;
		}
		n = n >> 1;
		x = x >> 1;
	}
	return res;
}

int main() {
	std::cout << reverseBits(0u) << std::endl;
	return 0;
}
