import unittest

from group_diagram_combination import main


class CombinationTests(unittest.TestCase):
    def test_known_spanning_tree_counts(self):
        self.assertEqual(main([1], 0), [[]])
        self.assertEqual(len(main([1, 1], 1)), 1)
        self.assertEqual(len(main([2, 1], 1)), 2)
        self.assertEqual(len(main([1, 1, 1], 2)), 3)
        self.assertEqual(len(main([2, 2, 1], 2)), 20)

    def test_every_result_has_requested_edges_and_all_factors(self):
        for method in main([2, 2, 1], 2):
            self.assertEqual(len(method), 2)
            factors = {endpoint[0] for edge in method for endpoint in edge}
            self.assertEqual(factors, {1, 2, 3})

    def test_rejects_invalid_counts(self):
        for edge_count in (True, -1, 1.5):
            with self.assertRaisesRegex(ValueError, "edge_count"):
                main([1, 1], edge_count)
        with self.assertRaisesRegex(ValueError, "component counts"):
            main([1, 0], 1)


if __name__ == "__main__":
    unittest.main()
