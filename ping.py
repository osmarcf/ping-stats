import os
import json
import csv
import time

urls = [
    'google.com',
    '8.8.8.8',
    '191.243.8.88',
    '192.168.55.1',
    '10.0.0.1'
]

interfaces = [
    'eth0',
    'wlan0'
]


while True:
    for url in urls:
        for interface in interfaces:
            registro = {}
            registro['interface'] = interface
            registro['ip'] = url
            registro['timestamp'] = int(time.time() * 1000)

            retorno = os.popen('ping -c 1 -W 1 -D -O ' + url + ' -I ' + interface).read()
            dados = retorno.split('\n')

            if dados[1] == '':
                registro['erro'] = 'Sem resposta'
            else:
                dados = dados[1].translate(None, '[]:')
                duracao = dados.split('time=')[1].split(' ')

                registro['duracao'] = duracao[0]
                registro['duracao_unidade'] = duracao[1]

            #with open('/tmp/dados_ping.json', 'a+') as arquivo_json:
            #    arquivo_json.write(json.dumps(registro) + '\r\n')

            with open('/tmp/dados_ping.csv', 'a+') as arquivo_csv:
                w = csv.DictWriter(arquivo_csv, registro.keys(), delimiter=';')
                w.writerow(registro)

    time.sleep(2)

