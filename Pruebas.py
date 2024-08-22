import unittest
import Libreria_Numeros_Complejos
import math

class TestLibComplex(unittest.TestCase):
    n1, n2= ((-1,2),(5,-9))
    n3, n4 = ((2.5,-9), (4,1))
    n5, n6 = ((5.25, 8), (6.8,2))

    def test_suma(self):
        prueba_1 = Libreria_Numeros_Complejos.suma(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], 4)
        self.assertAlmostEqual(prueba_1[1],-7)
        prueba_2 = Libreria_Numeros_Complejos.suma(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], 6.5)
        self.assertAlmostEqual(prueba_2[1],-8)
        prueba_3 = Libreria_Numeros_Complejos.suma(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], 12.05)
        self.assertAlmostEqual(prueba_3[1],10)
    
    def test_division(self):
        prueba_1 = Libreria_Numeros_Complejos.division(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], -0.2169811320754717)
        self.assertAlmostEqual(prueba_1[1], 0.009433962264150943)
        prueba_2 = Libreria_Numeros_Complejos.division(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], 0.05882352941)
        self.assertAlmostEqual(prueba_2[1],-2.264705882)
        prueba_3 = Libreria_Numeros_Complejos.division(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], 1.02906051)
        self.assertAlmostEqual(prueba_3[1],0.8738057325)

    def test_multiplicacion(self):
        prueba_1 = Libreria_Numeros_Complejos.multiplicacion(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], 13)
        self.assertAlmostEqual(prueba_1[1],19)
        prueba_2 = Libreria_Numeros_Complejos.multiplicacion(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], 19)
        self.assertAlmostEqual(prueba_2[1],-33.5)
        prueba_3 = Libreria_Numeros_Complejos.multiplicacion(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], 19.7)
        self.assertAlmostEqual(prueba_3[1],64.9)
    
    def test_modulo(self):
        self.assertAlmostEqual(Libreria_Numeros_Complejos.modulo(self.n1), (2.23606797749979))
        self.assertAlmostEqual(Libreria_Numeros_Complejos.modulo(self.n3), (9.340770846))
        self.assertAlmostEqual(Libreria_Numeros_Complejos.modulo(self.n5), (9.568829605))

    def test_resta(self):
        prueba_1 = Libreria_Numeros_Complejos.resta(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], -6)
        self.assertAlmostEqual(prueba_1[1],11)
        prueba_2 = Libreria_Numeros_Complejos.resta(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], -1.5)
        self.assertAlmostEqual(prueba_2[1],-10)
        prueba_3 = Libreria_Numeros_Complejos.resta(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], -1.55)
        self.assertAlmostEqual(prueba_3[1],6)

    def test_conjugado(self):
        prueba_1 = Libreria_Numeros_Complejos.conjugado(self.n1)
        self.assertAlmostEqual(prueba_1[0], -1)
        self.assertAlmostEqual(prueba_1[1],-2)
        prueba_2 = Libreria_Numeros_Complejos.conjugado(self.n3)
        self.assertAlmostEqual(prueba_2[0], 2.5)
        self.assertAlmostEqual(prueba_2[1], 9)
        prueba_3 = Libreria_Numeros_Complejos.conjugado(self.n5)
        self.assertAlmostEqual(prueba_3[0], 5.25)
        self.assertAlmostEqual(prueba_3[1],-8)

    def test_CartToPolar(self):
        prueba_1 = Libreria_Numeros_Complejos.cart_to_polar(self.n1)
        self.assertAlmostEqual(prueba_1[0], 2.23606797749979)
        self.assertAlmostEqual(prueba_1[1], 2.0344439357957027)
        prueba_2 = Libreria_Numeros_Complejos.cart_to_polar(self.n3)
        self.assertAlmostEqual(prueba_2[0], 9.340770846)
        self.assertAlmostEqual(prueba_2[1], -1.299849476)
        prueba_3 = Libreria_Numeros_Complejos.cart_to_polar(self.n5)
        self.assertAlmostEqual(prueba_3[0], 9.568829605)
        self.assertAlmostEqual(prueba_3[1], 0.9900399732)


    n7 = (8, math.pi/2)
    n8 = (-2, -math.pi/11)
    n9 = (5, -math.pi/6)
    
    def test_PolarToCart(self):
        prueba_1 = Libreria_Numeros_Complejos.polar_to_cart(self.n7)
        self.assertAlmostEqual(prueba_1[0], 0)
        self.assertAlmostEqual(prueba_1[1], 8)
        prueba_2 = Libreria_Numeros_Complejos.polar_to_cart(self.n8)
        self.assertAlmostEqual(prueba_2[0], -1.918985947)
        self.assertAlmostEqual(prueba_2[1], 0.5634651137)
        prueba_3 = Libreria_Numeros_Complejos.polar_to_cart(self.n9)
        self.assertAlmostEqual(prueba_3[0], 4.330127019)
        self.assertAlmostEqual(prueba_3[1], -2.5)


    def test_fase(self):
        self.assertAlmostEqual(Libreria_Numeros_Complejos.fase(self.n1), 2.0344439357957027)
        self.assertAlmostEqual(Libreria_Numeros_Complejos.fase(self.n3), -1.299849476)
        self.assertAlmostEqual(Libreria_Numeros_Complejos.fase(self.n5), 0.9900399732)
        
if __name__ == '__main__':
    unittest.main()