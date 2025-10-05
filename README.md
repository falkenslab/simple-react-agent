Simple ReAct Agent
===================

Descripción
-----------
- Agente minimalista que implementa el patrón [ReAct](https://arxiv.org/pdf/2210.03629) (Reason + Act) sobre modelos de OpenAI.
- Usa la API de Chat Completions para razonar en bucle y ejecutar acciones disponibles.
- Incluye dos acciones de ejemplo: `calculate` (evalúa expresiones aritméticas) y `average_dog_weight` (devuelve el peso medio aproximado de una raza).

Requisitos
----------
- Python 3.12 o superior.
- Una clave válida de OpenAI en la variable de entorno `OPENAI_API_KEY`.
- Gestor de dependencias (elige uno):
  - `pip` (estándar) o
  - `uv` (opcional, si lo usas en tu flujo)

Descarga
--------
1) Clonar el repositorio:

   - Git
     - `git clone https://github.com/falkenslab/simple-react-agent.git`
     - `cd simple-react-agent`

Instalación
-----------
2) Crear y activar un entorno virtual:

   - Windows (PowerShell)
     - `py -3.12 -m venv .venv`
     - `./.venv/Scripts/Activate.ps1`

   - macOS/Linux (bash/zsh)
     - `python3.12 -m venv .venv`
     - `source .venv/bin/activate`

3) Instalar dependencias:

   - Con pip
     - `pip install -e .`

   - Con uv (opcional)
     - `uv pip install -e .`

Configuración de la API Key
---------------------------
Establece la variable de entorno `OPENAI_API_KEY` antes de ejecutar:

- Windows (PowerShell):
  - `$env:OPENAI_API_KEY = "tu_api_key"`

- macOS/Linux (bash/zsh):
  - `export OPENAI_API_KEY="tu_api_key"`

También puedes guardar la clave en un archivo `.env` (no se carga automáticamente por el código; expórtala en tu sesión si la usas).

Ejecución
---------
El paquete instala un comando de consola `react`. Pásale la pregunta como argumento:

- `react "¿Cuánto pesa un Scottish Terrier y un Border Collie?"`

Si el comando `react` no está disponible en tu PATH, ejecuta el módulo directamente:

- `python -m react "¿Cuánto pesa un Scottish Terrier y un Border Collie?"`

Acciones disponibles (demo)
---------------------------
- `calculate`: ejecuta expresiones aritméticas de Python (usa sintaxis de punto flotante si procede).
  - Ejemplo interno de uso del agente: `ACTION: calculate: 4 * 7 / 3`
- `average_dog_weight`: devuelve un peso medio aproximado para una raza conocida.
  - Ejemplo interno: `ACTION: average_dog_weight: Border Collie`

Solución de problemas
---------------------
- `openai` sin credenciales: asegúrate de definir `OPENAI_API_KEY` en el entorno activo.
- `react` no encontrado: activa el entorno virtual o usa `python -m react`.
- Proxy/firewall: si tu entorno restringe red, verifica que puedes salir a `api.openai.com`.

Licencia
--------
Consulta el repositorio para detalles de licencia y contribución.
