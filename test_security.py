import unittest
from security import validar_password

class TestSecurity(unittest.TestCase):
    def test_password_curt(self):
        contrasenya = "12345"
        self.assertFalse(validar_password(contrasenya))

    def test_password_llarg(self):
        contrasenya = "contraseñaSegura123"
        self.assertTrue(validar_password(contrasenya))

if __name__ == "__main__":
    unittest.main()

