#!/usr/bin/python3

# Autor: @rojosec

import subprocess
import argparse
import time

class discoverOS:
    # definiendo parametros
    def __init__(self):
        parser = argparse.ArgumentParser(description='discoverOS')
        parser.add_argument('-t',dest='target',help='dirección ip objetivo | target')
        self.argumento = parser.parse_args()
        

    # traza ICMP
    def trazaICMP(self):
        self.target = self.argumento.target
        self.captura = subprocess.run(['ping','-c 1',self.target],capture_output=True)
    
    
    def filtroCaptura(self):
        # Decodificacion de stdout, separandolo, y extrayendo el valor 'ttl'
        self.decodificarCaptura = self.captura.stdout.decode('utf-8').split()[12]
        

    def verificandoOS(self):
        # slicing a la cadena ttl para extraer el valor de este mismo y depues parsearlo a tipo entero 
        ttl = int(self.decodificarCaptura[-2:])
        
        # comparando ttl y obteniendo SO
        if ttl >= 63 and ttl <= 64 :
            print(f'[+] {self.target} ==> LINUX ')
        


if __name__ == '__main__':
    discover = discoverOS()
    discover.trazaICMP()
    discover.filtroCaptura()
    discover.verificandoOS()