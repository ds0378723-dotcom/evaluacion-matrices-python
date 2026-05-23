# Módulo: Función para calcular el total de horas y clasificar la jornada
def analizar_jornada_laboral(matriz_horas, umbral_estandar=40):
    """
    Calcula el total de horas semanales por recurso y clasifica su jornada.
    """
    resultados = []
    
    for fila in matriz_horas:
        nombre = fila[0]
        # Sumamos las horas de Lunes a Viernes (posiciones 1 a 5)
        total_horas = sum(fila[1:])
        
        # Lógica de negocio: Clasificación según el umbral
        if total_horas > umbral_estandar:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
            
        resultados.append({
            "nombre": nombre,
            "total_horas": total_horas,
            "clasificacion": clasificacion
        })
        
    return resultados

# Desarrollo: Creación de la matriz con 4 recursos
# Estructura: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
matriz_recursos = [
    ["Ana Gómez", 8, 9, 8, 8, 9],       # 42 horas -> Sobretiempo
    ["Carlos Ruiz", 8, 8, 7, 8, 8],     # 39 horas -> Horario Estándar
    ["María López", 9, 10, 8, 9, 8],    # 44 horas -> Sobretiempo
    ["Juan Pérez", 8, 8, 8, 8, 8]       # 40 horas -> Horario Estándar
]

# Ejecución del módulo
reporte_semanal = analizar_jornada_laboral(matriz_recursos)

# Salida: Impresión de resultados con formato limpio
print(f"{'Recurso':<15} | {'Horas Semanales':<15} | {'Clasificación'}")
print("-" * 50)
for registro in reporte_semanal:
    print(f"{registro['nombre']:<15} | {registro['total_horas']:<15} | {registro['clasificacion']}")
