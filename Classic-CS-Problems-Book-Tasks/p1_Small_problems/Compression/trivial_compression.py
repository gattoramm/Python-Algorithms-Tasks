class CompressGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # начальная метка
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # сдвиг влево на 2 бита
            if nucleotide == 'A':  # поменять 2 последних бита на 00
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError('Invalid Nucleotide:{}'.format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # -1 чтобы исключить метку
            bits: int = self.bit_string >> i & 0b11
            # получить только 2 значимых бита
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b011:
                gene += 'T'
            else:
                raise ValueError('Invalid Nucleotide:{}'.format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = \
        "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print('original is {} bytes'.format(getsizeof(original)))
    compressed: CompressGene = CompressGene(original)
    print('compressed is {} bytes'.format(getsizeof(compressed)))
    print(compressed)
    print('original and decompressed are the same: {}'.format(original == compressed.decompress()))
