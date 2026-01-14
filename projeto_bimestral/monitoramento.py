import psutil, platform, time

class MonitoraSistema:
    def __init__(self, intervalo):
        self.intervalo = intervalo # Tempo entre cada leitura

    # Responsável por retornar a quantidade de núcleos físicos e lógicos
    def dados_cpu(self):
        nucleos_fisicos = psutil.cpu_count(logical=False)
        nucleos_logicos = psutil.cpu_count()
        return f"Núcleos físicos: {nucleos_fisicos} núcleos \nNúcleos lógicos: {nucleos_logicos} núcleos"

    # Responsável por retornar a porcentagem usada e livre da memória RAM, além do seu total
    def dados_memoria_ram(self):
        memoria = psutil.virtual_memory()
        percent_used = memoria.used / memoria.total * 100
        percent_free = memoria.available / memoria.total * 100
        total = memoria.total
        return f"Memória RAM livre: {percent_free:.0f}% \nMemória RAM usada: {percent_used:.0f}% \nMemória RAM total (sempre 100%): {total}"
    
    # Responsável por retornar a porcentagem de espaço livre no disco
    def espaco_disco(self):
        disco = psutil.disk_usage('/')
        return f"{disco.percent:.0f}%"
    
    # Responsável por retornar nome e versão do sistema operacional. Utilizando módulo platform
    def sistema_operacional(self):
        name = platform.system()
        version = platform.release()
        return f"{name} {version}"
    
    def dados_ips():
        enderecos = psutil.net_if_addrs()
        for address in enderecos:
            print(address)
    
    def __str__(self):
        return f"===== Monitoramento ===== \n\n* Disco * \nEspaço livre no disco: {self.espaco_disco()} \n\n* Memória RAM * \n{self.dados_memoria_ram()} \n\n* CPU * \n{self.dados_cpu()} \n\n* Sistema Operacional * \n{self.sistema_operacional()}"
    
    # Inicia o monitoramento e pode ser parado pelo usuário
    def iniciar_monitoramento(self):
        while True:
            try:
                print("Exibindo dados dos PCs")
                print()
                print(str(self))
                time.sleep(self.intervalo)
            except KeyboardInterrupt:
                print()
                print("Monitoramento interrompido manualmente")