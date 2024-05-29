# Módulo 6 - Ponderada 3 - Turtlebot teleoperado pt2
## 🔍 Descrição
Este projeto é uma extensão da atividade anterior (Turtlebot Teleoperado Pt. 1), que agora inclui uma interface de usuário capaz de exibir a imagem vista por uma câmera em tempo real. O sistema foi implementado para funcionar tanto com um robô real quanto com um ambiente simulado, permitindo a transmissão de um arquivo de vídeo qualquer no caso da simulação.
## 💻 Estrutura do projeto
- **sender.py**: Código responsável pela captura de vídeo, cálculo e publicação da latência e FPS.
- **interface.html**: Interface web para controle do Turtlebot e exibição do vídeo em tempo real.
- **teleop_node.py**: Código de teleoperação que envia comandos de velocidade para o Turtlebot.
- **turtlebot_controller.py**: Controlador que recebe e publica comandos de velocidade e possui um serviço para parar o robô.
## ⚙️ Instrução de execução
### Pré-requisitos
- Ubuntu
- ROS 2
- Webots
- Python
- Uma câmera conectada ao sistema
### Instalação
1) Clonagem do repositório <br/>
`git clone https://github.com/lidiamariano/Mod6Pond3`
2) Instação das Dependências <br/>
`pip install -r requirements.txt`
### Execução
1) Vá até o caminho relativo de onde está o código <br/>
`cd src`
2) Abra a seguinte página html no navegador <br/>
`interface.html`
3) Rodar o ROSbridge para conectar com o WebSocket <br/>
`ros2 launch rosbridge_server rosbridge_websocket_launch.xml`
4) Rodar o sender.py, ainda na página src
`python3 sender.py`
5) Abrir o Webots pelo comando <br/>
`ros2 launch webots_ros2_turtlebot robot_launch.py`




