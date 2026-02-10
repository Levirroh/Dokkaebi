# 📱 Projeto Dokkaebi:

Este documento consolida a visão estratégica, técnica e de escala para o sistema Dokkaebi, integrando monitoramento, automação e controle distribuído.

---

## 🏛️ 1. Arquitetura de Sistema (Multi-Agente)

O projeto deixa de ser um "app simples" para se tornar um sistema **Hub & Spoke** (Cubo e Raios), onde as responsabilidades são divididas em três camadas:

### A. O Orquestrador (Seu Celular Principal)
* **Função:** Interface de Controle (Frontend).
* **Tecnologia:** React Native (Expo) + Styled Components.
* **Comportamento:** Ativo. Ele detém a lista de IPs dos agentes e dispara requisições diretas para execução de comandos.
* **Armazenamento Local:** Usa `AsyncStorage` para salvar os perfis dos Agentes (Nome, IP Tailscale, Localização).

### B. Os Agentes (Celulares Antigos/Servidores de Execução)
* **Função:** Execução de Hardware e Sensores (Backend).
* **Tecnologia:** Python (FastAPI) rodando no Termux.
* **Comportamento:** Passivo/Reativo. Escuta comandos via API (ex: `/ligar-pc`, `/bateria`, `/camera`).
* **Independência:** Todos os agentes rodam o mesmo código base, facilitando o `git pull` e a manutenção.

### C. O Nó de Dados (Celular Banco de Dados)
* **Função:** Memória Central e Logs.
* **Tecnologia:** Python + SQLite (ou PostgreSQL no Termux).
* **Comportamento:** Centralizador. Recebe logs de todos os agentes e fornece o histórico para o Orquestrador.
* **Vantagem:** Permite gerar gráficos de performance e histórico de eventos sem sobrecarregar os agentes de execução.

---

## 🌐 2. Infraestrutura de Rede e Acesso

* **Tailscale (VPN Mesh):** Cria a rede virtual segura que une o PC, o Celular Principal e todos os Agentes, independente de estarem na mesma rede Wi-Fi.
* **P2P (Direct Request):** O comando sai do App direto para o IP do Agente alvo (baixa latência).
* **SSH Remoto:** Configuração de `sshd` no Termux para permitir manutenção do código via terminal de qualquer lugar do mundo.

---

## 🛠️ 3. Fluxo de Operação de um Comando

1.  **Ação:** Usuário clica em "Ligar PC" no App.
2.  **Comando:** App consulta o IP do `Agente_Casa` e envia um `POST /exec/wake-on-lan`.
3.  **Execução:** `Agente_Casa` recebe, executa o comando físico e responde `200 OK`.
4.  **Log:** Após a execução, o `Agente_Casa` envia silenciosamente um log para o `Celular_Banco`: *"Ação: Ligar PC | Status: Sucesso"*.

---

## 🚀 4. Roadmap de Implementação (Sábado e Além)

### Fase 1: Fundação (O que você fará sábado)
* Setup do ambiente Node e Python.
* Conexão básica via Tailscale entre 1 App e 1 Agente.
* Comando simples de leitura de bateria via API.

### Fase 2: Gestão de Frota
* Criação da tela de "Cadastro de Agentes" no App.
* Substituição de IPs fixos por variáveis dinâmicas salvas no celular.

### Fase 3: Inteligência Centralizada
* Implementação do Celular Banco de Dados.
* Criação de dashboards de histórico e status "Online/Offline" (Heartbeat).

---

## 📝 Notas de Engenharia
* **Modularidade:** Se um agente cair, o sistema continua funcionando para os outros.
* **Segurança:** Toda a comunicação é interna à VPN do Tailscale.
* **Escalabilidade:** Para adicionar um novo cômodo na automação, basta um celular velho e um `git pull`.