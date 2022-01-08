import unittest
from SearchTasks.dna_search import *


class DnaSearchTestCase(unittest.TestCase):
    def test_contains(self):
        gene_str: str = 'ACGTTGCGCTAGATCGCTAGCTAGCTGCGCGCTAGCGCATGAGCATCGCATAGCGCTAGAGCATCG' * 100
        acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
        self.assertTrue(linear_contains(string_to_gene(gene_str), acg))

    def test_not_contains(self):
        gene_str: str = 'AAAA' * 100
        acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
        self.assertEqual(linear_contains(string_to_gene(gene_str), acg), False)

    def test_binary_contains(self):
        gene_str: str = 'ACGTTGCGCTAGATCGCTAGCTAGCTGCGCGCTAGCGCATGAGCATCGCATAGCGCTAGAGCATCG' * 100
        acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
        self.assertTrue(binary_contains(string_to_gene(gene_str), acg))

    def test_binary_not_contains(self):
        gene_str: str = 'AAAA' * 100
        acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
        self.assertEqual(binary_contains(string_to_gene(gene_str), acg), False)

if __name__ == '__main__':
    unittest.main()
