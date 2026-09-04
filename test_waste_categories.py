import unittest
from src.waste_categories import CLASS_TO_BIN, COMPOSTABLE, RECYCLABLE, bin_for_detected_class

class WasteCategoryTests(unittest.TestCase):
    def test_all_six_paper_classes_are_mapped(self): self.assertEqual(set(CLASS_TO_BIN), {"electronic", "glass", "metal", "organic", "paper", "plastic"})
    def test_recognized_categories(self):
        self.assertEqual(bin_for_detected_class("organic"), COMPOSTABLE); self.assertEqual(bin_for_detected_class("glass"), RECYCLABLE)
    def test_unknown_is_not_a_detector_category(self):
        with self.assertRaises(KeyError): bin_for_detected_class("unknown")
if __name__ == "__main__": unittest.main()
