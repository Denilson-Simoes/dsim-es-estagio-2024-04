import unittest
import cirt

class TestCalculaSalarioBaseAposFaltas__SalarioBaseAposFaltas(unittest.TestCase):

    def test_verifica_se_retorna_algum_valor__(self):
        #Arrange
        resultado_calculado = None
        #Assert
        resultado_calculado = cirt.calcula_salario_base_apos_faltas(100000,10,22)
        #Act
        self.assertIsNotNone(resultado_calculado, "Erro! A Funcionalidade nao retorna nada!")
    def test_verifica_se(self):
        #Arrange
        resultado_esperado = 54545.45
        #Assert
        resultado_calculado = cirt.calcula_salario_base_apos_faltas(100000,10,22)
        #Act
        self.assertEqual(resultado_esperado, resultado_calculado, "Erro! Os valores devem ser iguais!")
    def test_calcula_salario_base_apos_faltas(self):
        #Arrange
        resultado_esperado = 0
        #Assert
        resultado_calculado = cirt.calcula_salario_base_apos_faltas(100000,10,22)
        #Act
        self.assertNotEqual(resultado_esperado, resultado_calculado, "Erro! Os valores nao devem ser iguais")

class TestCalculaSubsidioDeAlimentacaoTotal__SubsidioDeAlimentacaoTotal(unittest.TestCase):

    def test_verifica_se_retorna_algum_valor__(self):
        #Arrange
        resultado_calculado = None
        #Assert
        resultado_calculado = cirt.calcula_subsidio_de_alimentacao(1000,22)
        #Act
        self.assertIsNotNone(resultado_calculado, "Erro! A Funcionalidade nao retorna nada!")
    def test_verifica_se(self):
        #Arrange
        resultado_esperado = 22000.00
        #Assert
        resultado_calculado = cirt.calcula_subsidio_de_alimentacao(1000,22)
        #Act
        self.assertEqual(resultado_esperado, resultado_calculado, "Erro! Os valores devem ser iguais!")
    def test_calcula_salario_base_apos_faltas(self):
        #Arrange
        resultado_esperado = 0
        #Assert
        resultado_calculado = cirt.calcula_subsidio_de_alimentacao(1000,22)
        #Act
        self.assertNotEqual(resultado_esperado, resultado_calculado, "Erro! Os valores nao devem ser iguais")

class TestCalculaSubsidioDeTransporteTotal__SubsidioDeTransporteTotal(unittest.TestCase):

    def test_verifica_se_retorna_algum_valor__(self):
        #Arrange
        resultado_calculado = None
        #Assert
        resultado_calculado = cirt.calcula_subsidio_de_transporte(1200,22)
        #Act
        self.assertIsNotNone(resultado_calculado, "Erro! A Funcionalidade nao retorna nada!")
    def test_verifica_se(self):
        #Arrange
        resultado_esperado = 26400.00
        #Assert
        resultado_calculado = cirt.calcula_subsidio_de_transporte(1200,22)
        #Act
        self.assertEqual(resultado_esperado, resultado_calculado, "Erro! Os valores devem ser iguais!")
    def test_calcula_salario_base_apos_faltas(self):
        #Arrange
        resultado_esperado = 0
        #Assert
        resultado_calculado = cirt.calcula_subsidio_de_transporte(1200,22)
        #Act
        self.assertNotEqual(resultado_esperado, resultado_calculado, "Erro! Os valores nao devem ser iguais")

class TestCalculaDescontosDaSegurancaSocial__DescontosDaSegurancaSocial(unittest.TestCase):

    def test_verifica_se_retorna_algum_valor__(self):
        #Arrange
        resultado_calculado = None
        #Assert
        resultado_calculado = cirt.calcula_descontos_da_seguranca_social(100000.00,30000.00,30000.00,20000.00)
        #Act
        self.assertIsNotNone(resultado_calculado, "Erro! A Funcionalidade nao retorna nada!")
    def test_verifica_se(self):
        #Arrange
        resultado_esperado = 5400.00
        #Assert
        resultado_calculado = cirt.calcula_descontos_da_seguranca_social(100000.00,30000.00,30000.00,20000.00)
        #Act
        self.assertEqual(resultado_esperado, resultado_calculado, "Erro! Os valores devem ser iguais!")
    def test_calcula_salario_base_apos_faltas(self):
        #Arrange
        resultado_esperado = 0
        #Assert
        resultado_calculado = cirt.calcula_descontos_da_seguranca_social(100000.00,30000.00,30000.00,20000.00)
        #Act
        self.assertNotEqual(resultado_esperado, resultado_calculado, "Erro! Os valores nao devem ser iguais")

class TestCalculaImpostoSobreRendimentoDeTrabalho__IRT(unittest.TestCase):
    def test_verifica_se_retorna_algum_valor__(self):
        #Arrange
        resultado_calculado = None
        #Assert
        resultado_calculado = cirt.calcula_imposto_sobre_rendimento_de_trabalho(110000.00,30000.00,30000.00,10000.00)
        #Act
        self.assertIsNotNone(resultado_calculado, "Erro! A Funcionalidade nao retorna nada!")
    def test_verifica_se(self):
        #Arrange
        resultado_esperado = 597.87
        #Assert
        resultado_calculado = cirt.calcula_imposto_sobre_rendimento_de_trabalho(110000.00,30000.00,30000.00,10000.00)
        #Act
        self.assertEqual(resultado_esperado, resultado_calculado, "Erro! Os valores devem ser iguais!")
    def test_calcula_salario_base_apos_faltas(self):
        #Arrange
        resultado_esperado = 0
        #Assert
        resultado_calculado = cirt.calcula_imposto_sobre_rendimento_de_trabalho(110000.00,30000.00,30000.00,10000.00)
        #Act
        self.assertNotEqual(resultado_esperado, resultado_calculado, "Erro! Os valores nao devem ser iguais")

class TestCalculaSalarioLiquidoAposIncrementosEDescontos__SalarioLiquido(unittest.TestCase):
    def test_verifica_se_retorna_algum_valor__(self):
        #Arrange
        resultado_calculado = None
        #Assert
        resultado_calculado = cirt.calcula_salario_liquido_apos_incrementos_descontos(110000.00,25000.00,25000.00,10000.00,3,22)
        #Act
        self.assertIsNotNone(resultado_calculado, "Erro! A Funcionalidade nao retorna nada!")
    def test_verifica_se(self):
        #Arrange
        resultado_esperado = 150350.00
        #Assert
        resultado_calculado = cirt.calcula_salario_liquido_apos_incrementos_descontos(110000.00,25000.00,25000.00,10000.00,3,22)
        #Act
        self.assertEqual(resultado_esperado, resultado_calculado, "Erro! Os valores devem ser iguais!")
    def test_calcula_salario_base_apos_faltas(self):
        #Arrange
        resultado_esperado = 0
        #Assert
        resultado_calculado = cirt.calcula_salario_liquido_apos_incrementos_descontos(110000.00,25000.00,25000.00,10000.00,3,22)
        #Act
        self.assertNotEqual(resultado_esperado, resultado_calculado, "Erro! Os valores nao devem ser iguais")
