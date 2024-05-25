tarefas = []

while True:
    novaTarefa = input( 'informa nova tarefa:')

    if novaTarefa != '':
        tarefas.append(novaTarefa)
        continue
    else:
        break

for tarefa in tarefas:
     print(tarefa)
     