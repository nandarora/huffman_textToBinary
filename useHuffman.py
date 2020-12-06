from huffmancalled import HuffmanCodingClass
import sys

path = "sampletest.txt"

huffman = HuffmanCodingClass(path)

output_path = huffman.compress()
print("Compressed file path: " + output_path)

decom_path = huffman.decompress(output_path)
print("Decompressed file path: " + decom_path)