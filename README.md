# Serviço de Estacionamento (Parking Service)

Este é um sistema de gerenciamento de estacionamento desenvolvido em Django para fins de aprendizado técnico e evolução prática na linguagem Python.

---

## 📚 Sobre o Projeto
O projeto foi desenvolvido acompanhando as aulas do canal **PyCodeBr** no YouTube. O objetivo principal foi colocar em prática conceitos avançados de arquitetura web, automação de tarefas em segundo plano e containerização. 

Como este projeto envolveu conceitos que eu ainda não dominava (cerca de 80% do ecossistema utilizado era novo para mim), ele serviu como uma excelente base de estudo prático.

---

## 🛠️ Tecnologias e Conceitos Aprendidos
Ao longo do desenvolvimento, aprendi e apliquei:
* **Django & Django REST Framework:** Criação de rotas, views e modelagem de banco de dados (App de veículos, parking, customers, etc.).
* **Celery:** Configuração de filas de tarefas assíncronas para não bloquear a requisição do usuário.
* **Playwright (Web Scraping):** Automação com navegador em modo *headless* para buscar dados de veículos de forma externa e atualizar o banco de dados.
* **Docker & Docker Compose:** Criação de ambiente isolado multiplataforma para o servidor web e workers.
* **Boas Práticas:** Uso de linters (`.flake8`) e arquivos de isolamento (`.gitignore`, `.dockerignore`).

---
