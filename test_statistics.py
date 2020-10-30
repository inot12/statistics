#! /home/toni/.pyenv/shims/python3
"""
Created on Oct 29, 2020

@author:toni

"""

import unittest
import statistics as st


class TestStatistics(unittest.TestCase):
    """Test the module statistics.py."""
    
    def test_estimate(self):
        """Test estimate() for known input."""
        self.assertEqual(st.estimate(2, 5, 8), 5)  # general case
#         with self.assertRaises(ValueError):
#             st.estimate(0, 1, 5)
#             st.estimate(-1, 2, 8)
#         with self.assertRaises(ValueError):
#             st.estimate(5, 1, 9)
#             st.estimate(1, 9, 5)
        
    def test_stddev(self):
        """Test stddev() for known input."""
        self.assertEqual(st.stddev(2, 8), 1)  # general case
#         with self.assertRaises(ValueError):
#             st.stddev(0, 1)
#             st.stddev(-1, 2)
#         with self.assertRaises(ValueError):
#             st.stddev(5, 1)
        
    def test_probability(self):
        """Test probability() for known input."""
        tol = 1
        self.assertAlmostEqual(
            st.probability((1, 3, 12), (1, 1.5, 14), (3, 6.25, 11)),
            14.2, places=tol)
        
    def test_seq_stddev(self):
        """Test seq_stddev() for known input."""
        dt = 0.01
        self.assertAlmostEqual(
            st.seq_stddev((1, 12), (1, 14), (3, 11)),
            3.13, delta=dt)
        
    def test_final_estimate(self):
        """Test final_estimate() for known input."""
        dt = 0.05
        self.assertAlmostEqual(
            st.final_estimate((1, 3, 12), (1, 1.5, 14), (3, 6.25, 11)),
            17.33, delta=dt)


class TestStatisticsBadInput(unittest.TestCase):
    """Test for bad inputs."""
     
    def test_estimate_values(self):
        """estimate() should fail if one of the arguments less or equal 0."""
        with self.assertRaises(ValueError):
            st.estimate(0, 1, 5)
            st.estimate(-1, 2, 8)
             
    def test_estimate_order(self):
        """estimate() should fail if arguments not ordered from min to max."""
        with self.assertRaises(ValueError):
            st.estimate(5, 1, 9)
            st.estimate(1, 9, 5)
             
    def test_stddev_values(self):
        """stddev() should fail if one of the arguments less or equal 0."""
        with self.assertRaises(ValueError):
            st.stddev(0, 1)
            st.stddev(-1, 2)
     
    def test_stddev_order(self):
        """stddev() should fail if arguments not ordered from min to max."""
        with self.assertRaises(ValueError):
            st.stddev(5, 1)
            
    def test_final_estimate_input(self):
        """final_estimate() accepts only tuples of integers or floats."""
        with self.assertRaises(ValueError):
            st.final_estimate((1, 3, 12), (1, 1.5, 'a'), (3, 6.25, 11))

       
def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
