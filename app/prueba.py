def convertir(content: str) -> str:
    result = []
    content2 = content.replace("            ","")
    try:
        for line in content2.split('\n- '):
            if line.strip():
                parts = line.split(":")
                name = parts[1].split('value')[0].strip()
                value = parts[2].strip().strip('"')
                if value=='http':
                    value = value + ':' + parts[3].strip().strip('"')
                    if parts[4]:
                        value = value + ':' + parts[4].strip().strip('"')
                result.append(f"{name}={value}")
    except Exception as e:
        return 'No pude convertir tu texto a variables de entorno :c'
    return '\n'.join(result)

cadena = """
- name: PORT
              value: "3010" 
            - name: NODE_ENV
              value: "dev" 
            - name: KUBERNETES_ENGINE
              value: "1"
            - name: LOGGING_TRANSPORTS_FILE
              value: "1"
            - name: LOGGING_TRANSPORTS_CONSOLE
              value: "1" 
            - name: LOGGING_TRANSPORTS_DAILY_ROTATE
              value: "1" 
            - name: LOGGING_LEVEL_FILE
              value: "debug" 
            - name: LOGGING_LEVEL_CONSOLE
              value: "debug" 
            - name: LOGGING_FILE_PATH
              value: "/var/log/nodejs/"
            - name: LOGGING_FILE_NAME
              value: "bomo-api-gateway" 
            - name: LOGGING_FILE_MAXSIZE
              value: "1000000" 
            - name: SUBGRAPH_APP
              value: "http://bomo-api-registro:3011/"
            - name: SUBGRAPH_SERVICIOS
              value: "http://bomo-api-trx:3012/"
            - name: SUBGRAPH_BACKOFFICE
              value: "http://bomo-api-backoffice:3013/"
            - name: SUBGRAPH_SEGURIDAD
              value: "http://bomo-api-seguridad:3014/"
"""

convertido = convertir(cadena)

print(convertido)