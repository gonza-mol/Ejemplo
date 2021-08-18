Feature: Login en la pagina de tienda
  Como usuario  accedo a la pagina de tienda con usuario y contraseña válida

  Scenario: login en pagina de tienda correcta
    Given Pagina web
    When ingreso "usuario" y contraseña "password"
    Then login válido