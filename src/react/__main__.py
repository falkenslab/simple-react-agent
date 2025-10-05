import re
import sys
from .agent import Agent

def calculate(what):
    return eval(what)

def average_dog_weight(name):
    if name in "Scottish Terrier": 
        return("peso medio Scottish Terrier 9 kg")
    elif name in "Border Collie":
        return("peso medio Border Collie 17 kg")
    elif name in "Toy Poodle":
        return("peso medio Toy Poodle 3 kg")
    else:
        return("peso medio perro 23 kg")

known_actions = {
    "calculate": calculate,
    "average_dog_weight": average_dog_weight
}

prompt = """
    Te ejecutas en un bucle de THOUGHT, ACTION, PAUSE, OBSERVATION.
    Al final del bucle produces un ANSWER.
    Usa THOUGHT para describir tus pensamientos sobre la pregunta que te han hecho.
    Usa ACTION para ejecutar una de las acciones disponibles - luego devuelve PAUSE.
    OBSERVATION será el resultado de ejecutar esas acciones.

    Tus acciones disponibles son:

    calculate:
    e.g. calculate: 4 * 7 / 3
    Ejecuta la operación y devuelve el número - usa Python así que asegúrate de usar sintaxis de punto flotante si es necesario

    average_dog_weight:
    e.g. average_dog_weight: Collie
    Devuelve el peso promedio de un perro de la raza indicada.

    Sesión de ejemplo:

    Question: Cuánto pesa un bulldog?
    THOUGHT: Debería buscar el peso de los perros usando average_dog_weight
    ACTION: average_dog_weight: Bulldog
    PAUSE

    Luego serás llamado de nuevo con esto:

    OBSERVATION: Un bulldog pesa 23 kg

    Y al final deberías responder con esto:

    ANSWER: Un bulldog pesa 23 kg
""".strip()

# Expresión regular para buscar si en la respuesta hay una acción a ejecutar
action_re = re.compile("^ACTION: (\\w+): (.*)$")

def ask(question, max_turns=5):
    i = 0
    bot = Agent(prompt)
    next_prompt = question
    while i < max_turns:
        i += 1
        result = bot(next_prompt)
        print(result)
        actions = [
            action_re.match(a) 
            for a in result.split('\n') 
            if action_re.match(a)
        ]
        if actions:
            # There is an action to run
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception("Acción desconocida: {}: {}".format(action, action_input))
            print(" -- ejecutando {} {}".format(action, action_input))
            observation = known_actions[action](action_input)
            print("OBSERVATION:", observation)
            next_prompt = "OBSERVATION: {}".format(observation)
        else:
            return

def main():
    question = sys.argv[1] # ejemplo: "¿Cuánto pesa un Scottish Terrier y un Border Collie?"
    ask(question)

if __name__ == "__main__":
    main()
