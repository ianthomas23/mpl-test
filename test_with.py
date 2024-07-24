# Test with import of matplotlib

from contourpy import contour_generator
import matplotlib.pyplot as plt

print("START")
cont_gen = contour_generator(z=[[0, 1], [2, 3]])
try:
    cont_gen.filled(2.0, 1.0)
except Exception as e:
    print("EXCEPTION HANDLER", e)
print("END")
